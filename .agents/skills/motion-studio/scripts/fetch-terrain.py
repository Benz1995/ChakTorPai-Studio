"""Fetch a bounded Mapzen Terrarium area and export a sampled, geographic height grid.

Requires Pillow; uses only documented public AWS Terrain Tiles, without credentials.
Raw downloads and provenance are retained. No satellite imagery or Google tiles.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

def tile_xy(lon, lat, zoom):
    n = 2 ** zoom
    return (lon+180)/360*n, (1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bounds', type=float, nargs=4, required=True, metavar=('WEST','SOUTH','EAST','NORTH'))
    p.add_argument('--zoom', type=int, default=12)
    p.add_argument('--grid', type=int, default=65)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--landmark', type=float, nargs=2, metavar=('LAT','LON'))
    a = p.parse_args()
    west,south,east,north = a.bounds
    if not (-180 <= west < east <= 180 and -85 <= south < north <= 85):
        p.error('Bounds must be ordered and within Web Mercator coverage')
    if not (0 <= a.zoom <= 15 and 9 <= a.grid <= 257):
        p.error('zoom 0..15; grid 9..257')
    if a.landmark and not (south <= a.landmark[0] <= north and west <= a.landmark[1] <= east):
        p.error('Landmark must lie inside bounds')
    x0,y0 = tile_xy(west,north,a.zoom)
    x1,y1 = tile_xy(east,south,a.zoom)
    xmin,xmax,ymin,ymax=math.floor(x0),math.floor(x1),math.floor(y0),math.floor(y1)
    count=(xmax-xmin+1)*(ymax-ymin+1)
    if count>16:
        p.error(f'Area needs {count} tiles; maximum 16 per invocation. Reduce extent/zoom.')
    a.out.mkdir(parents=True,exist_ok=True)
    raw=a.out/'terrain-source';raw.mkdir(exist_ok=True)
    mosaic=Image.new('RGB',((xmax-xmin+1)*256,(ymax-ymin+1)*256))
    receipts=[]
    for ty in range(ymin,ymax+1):
        for tx in range(xmin,xmax+1):
            url=f'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{a.zoom}/{tx}/{ty}.png'
            dest=raw/f'{a.zoom}-{tx}-{ty}.png'
            cached=dest.exists()
            if not cached:
                with urlopen(Request(url,headers={'User-Agent':'BigO-TerrainStudy/1.0'}),timeout=30) as r:
                    data=r.read(2_000_001)
                if len(data)>2_000_000: raise ValueError('Unexpected tile size')
                tile=Image.open(io.BytesIO(data));tile.load()
                if tile.size!=(256,256):raise ValueError('Unexpected tile dimensions')
                dest.write_bytes(data)
            data=dest.read_bytes()
            tile=Image.open(io.BytesIO(data)).convert('RGB')
            if tile.size!=(256,256):raise ValueError('Invalid cached tile')
            mosaic.paste(tile,((tx-xmin)*256,(ty-ymin)*256))
            receipts.append({'url':url,'file':str(dest.resolve()),'sha256':hashlib.sha256(data).hexdigest(),'reused_local_file':cached})
            print(f'Tile {len(receipts)}/{count}',flush=True)
    def height(lon,lat):
        x,y=tile_xy(lon,lat,a.zoom)
        # Pixel centres are half a pixel into each cell. Interpolate decoded metres,
        # never interpolate the RGB representation across byte boundaries.
        x=(x-xmin)*256-.5;y=(y-ymin)*256-.5
        ix,iy=math.floor(x),math.floor(y);fx,fy=x-ix,y-iy
        def sample(dx,dy):
            r,g,b=mosaic.getpixel((max(0,min(mosaic.width-1,ix+dx)),max(0,min(mosaic.height-1,iy+dy))))
            return r*256+g+b/256-32768
        return (sample(0,0)*(1-fx)+sample(1,0)*fx)*(1-fy)+(sample(0,1)*(1-fx)+sample(1,1)*fx)*fy
    grid=[[round(height(west+(east-west)*x/(a.grid-1),north-(north-south)*y/(a.grid-1)),2) for x in range(a.grid)]for y in range(a.grid)]
    flat=[h for row in grid for h in row]
    if not all(math.isfinite(h) and -500<h<9000 for h in flat):raise ValueError('Invalid or void heights')
    if max(flat)-min(flat)<10:raise ValueError('Unexpectedly flat terrain')
    lat=(north+south)/2
    result={'bounds':{'west':west,'south':south,'east':east,'north':north},'grid_size':a.grid,'heights_m':grid,
      'width_m':(east-west)*111320*math.cos(math.radians(lat)),'depth_m':(north-south)*111320,
      'source_zoom':a.zoom,'source_pixel_spacing_m_approx':156543.03392*math.cos(math.radians(lat))/2**a.zoom,
      'min_height_m':min(flat),'max_height_m':max(flat),
      'provenance':{'dataset':'Mapzen Terrain Tiles on AWS','accessed_utc':datetime.now(timezone.utc).isoformat(),
      'source_date':'Mixed source acquisition dates; exact local vintage not verified','vertical_datum':'Not independently verified for the served regional mosaic',
      'encoding':'R*256+G+B/256-32768 metres','resampling':'Bilinear decoded heights on a regular latitude/longitude grid; no synthetic terrain added',
      'attribution':'Mapzen / Terrain Tiles on AWS; SRTM and GMTED2010 terrain data courtesy of the U.S. Geological Survey',
      'docs':['https://registry.opendata.aws/terrain-tiles/','https://github.com/tilezen/joerd/blob/master/docs/formats.md','https://github.com/tilezen/joerd/blob/master/docs/attribution.md'],
      'tiles':receipts}}
    if a.landmark:
        result['landmark']={'lat':a.landmark[0],'lon':a.landmark[1],'sampled_height_m':round(height(a.landmark[1],a.landmark[0]),2)}
    (a.out/'terrain-grid.json').write_text(json.dumps(result,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('heights_m','provenance')},ensure_ascii=True))

if __name__=='__main__':main()
