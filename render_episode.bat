@echo off
if "%~1"=="" (
    echo Usage: render_episode.bat ^<episode_dir^>
    echo Example: render_episode.bat series\day0\ep01
    pause
    exit /b 1
)
python scripts\render_episode.py %*
