---
name: motion-animejs
description: "Choreograph sequenced DOM, SVG, text, and object motion with Anime.js, using paused seekable timelines for exported content."
---

# Anime.js choreography

Use for coordinated entrances, staggered typography, SVG motion, and timelines with many related cues.
For a few simple React transforms, existing Remotion interpolation may be sufficient.

Read [project integration](../motion-studio/references/project-integration.md) and [render contract](../motion-studio/references/render-contract.md).
Read [upstream evidence](references/upstream.json) before selecting the package/API version.

## Decide where it belongs

Anime.js is an optional dependency. Inspect the existing package tree before adding it for the specific task.
Use a scoped adapter around a content layer rather than letting a timeline mutate the whole application DOM.

- Upstream README currently documents v4 ES-module APIs. Check the installed major before using v3-style examples.
- Separate timing/choreography data from DOM setup so a composition can be inspected and adapted.
- Assign one owner to each animated transform or style. React and Anime.js must not overwrite the same property independently.
- Scope selectors to the composition's own root; parallel previews can contain repeated class names.

## Build an export-safe timeline

Create a paused timeline and drive it from the requested frame, not elapsed browser time.
For Anime.js v4, `timeline.seek(time, muteCallbacks)` accepts milliseconds.

- Convert the current scene time with `timeMs = frame / fps * 1000`; account for any scene start offset exactly once.
- Use `autoplay: false` and seek to the required time for every captured frame.
- Use muted callbacks for render seeking when callbacks would trigger sounds, requests, or unrelated state changes.
- Keep keyframe starts, delays, and stagger order explicit; seed any variation outside the timeline.
- Avoid callback-driven appending, DOM-dependent random selection, and live playback loops in an exported composition.
- Initialize after the scoped elements exist, finish seeking before capture, and release timeline/style ownership on unmount.
- If an adapter cannot meet that lifecycle reliably, bake frames or express the approved motion with frame-driven values.

## Choreography choices

Use a dominant cue, then stagger secondary elements to preserve reading order.
Reserve overshoot and path complexity for the focal element.
For Thai captions and product text, animate containers or grapheme-safe text units rather than splitting Unicode code units.

Keep narration and sound events in the audio timeline.
A visual timeline callback is not a reliable way to encode a sound into MP4.

## Verification

Inspect a stagger midpoint, an overlap, the final settled state, and a backward seek.
Compare the same frame after different seek orders to detect accumulated transforms or callback side effects.
Check React preview remounts do not leave duplicate timelines or mutate adjacent preview cards.

Run project type checking for integration code and render a short sample through the intended export engine.
Record the version and adapter path used, along with editable choreography data and the output file.

## Source boundary

The checked Anime.js repository is MIT licensed.
The upstream seek documentation is linked in the provenance file; recheck versioned APIs when updating the dependency.
