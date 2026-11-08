# ChatGPT image prompts for PolyTale

Send one prompt per message in the series' ChatGPT conversation and wait for each image.
If ChatGPT offers "which do you prefer", pick the one closer to the character sheet.
Regenerate once, with a stronger "keep identical" line, when identity drifts or text appears.

## Style line (start of every prompt)

```text
Same dark low-poly chibi 3D style and the same character designs as the approved character
images above (faceted low-poly shapes, big heads, small bodies, cinematic moody light,
teal shadows with warm highlights). Vertical 9:16. No text, no letters, no numbers, no logos,
no UI anywhere.
```

## Full frame (push shots)

```text
<style line> Full-frame image. <Place, time of day, light>. <Who is where, doing what, facing
which way, expression>. <Camera: close-up / medium / wide, eye level / low angle>. Keep faces
clear of the bottom third (subtitles go there).
```

## Plate (background without characters)

```text
<style line> Background plate only: <the same place as image N>, with NO main characters.
<Background people/props if any>. Leave the foreground <road/floor> empty where the
characters will be composited. Same camera and light as image N.
```

## Pose layers (run / walk / gesture)

```text
<style line> Transparent PNG background. Only <characters>, <action> toward the camera,
<pose phase A: which leg/arm forward>. Characters fill about the bottom 55% of the frame,
centred, feet inside the frame.
```
then
```text
Same transparent layer, identical framing, scale and position as pose A. Only the legs and
arms swing to the opposite phase: <pose phase B>. Same character designs.
```
Check: alpha bounding boxes of A and B within a few px (left, top, bottom).

## Character layer (standing, for reveal shots)

```text
<style line> Transparent PNG background. Only <character>, full body, <pose, facing,
expression>, standing at <left/centre/right> of the frame, feet at about 70–80% of the
frame height. Layer for compositing.
```

## Prop / effect layer

```text
<style line> Only <prop, e.g. a huge low-poly mushroom cloud with glowing orange core>,
isolated on a fully transparent background (transparent PNG). Same faceted low-poly style
as the characters.
```
If it comes back opaque, ask once more for transparency; then accept pure black and key it.

## Series "วันที่ 0" character notes

Teen boy: spiky dark low-poly hair, olive-green jacket, big backpack with bedroll, white
scarf-mask, bandaged right hand. Little brother: red knitted beanie with pompom, beige
jacket, green plush dinosaur. Dog: brown Thai dog, upright ears, dark collar.
