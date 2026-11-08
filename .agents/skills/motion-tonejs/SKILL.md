---
name: motion-tonejs
description: Design and render synthesized sound effects, musical cues, or rhythmic beds with Tone.js for this project's videos. Use offline audio assets for final Remotion output and live Web Audio only for an explicitly interactive preview.
---

# Tone.js sound design

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). Package and source details are in [upstream.json](references/upstream.json).

## Select the sound layer

- Use Tone.js for designed tones, impact/ping cues, synth motifs, and precisely scheduled effects.
- Build a cue sheet in seconds or frames from the composition timeline: scene start, narration lead-in, transition overlap, cue duration, and tail.
- Preserve narration intelligibility with deliberate gain and cue placement. A louder effect is not a substitute for a readable visual beat.
- Check whether a reusable existing recording already supplies the requested sound before adding a synth dependency.

## Render audio before video

1. Pin the installed `tone` version and use its current API. The upstream default development branch is not automatically the project's dependency version.
2. Use `Tone.Offline` with explicit duration, channel count, and sample rate to create a reusable audio buffer.
3. Create and schedule synths/effects within the offline callback. Schedule at explicit context times or use the offline context's transport.
4. Convert the resulting buffer to a real WAV or supported encoded asset; keep that file as the sound master used by both preview and final render.
5. Await sample loading and offline rendering before exposing the asset URL. Dispose nodes and restore/close contexts using the selected version's APIs.
6. For randomized/noise material, bake one approved master and retain its hash; an offline context alone does not seed every random source.

## Integrate with the current media contract

- The current project supports scene voice audio plus a global music URL/volume. It does not yet expose a general per-scene SFX track array.
- A finished background bed can use the existing music asset path. Do not replace scene narration with an effect-only file.
- Multiple independently timed effects need either a pre-mixed asset or an explicit typed audio-track feature shared by preview and export.
- Derive cue time from `sceneStartFrames` and the actual composition FPS, including transitions, rather than summing nominal scene durations.
- Do not expect headless video export to capture a live `AudioContext`, browser speakers, or a realtime Tone transport.
- For an interactive sound-preview button, start audio from the user's gesture and await `Tone.start()`; stop/dispose preview audio on route change.

## Verify observable output

- Probe the master for duration, sample rate, channel count, and codec; preserve enough tail for reverbs/delays without unintended trailing silence.
- Listen to sound design solo and under narration. Check clipping, sudden discontinuities, and masking of Thai consonants.
- Compare at least one cue near the start, a middle scene transition, and the final cue against frame-accurate video.
- Repeated renders should use the same baked audio master and cue sheet; seeking the video must not retrigger or duplicate a realtime synth.
- Distinguish original synthesis from third-party samples and preserve sample provenance when samples are used.

## Sources

[Tone.js README](https://github.com/Tonejs/Tone.js/blob/dev/README.md), [offline-render implementation](https://github.com/Tonejs/Tone.js/blob/dev/Tone/core/context/Offline.ts), [license](https://github.com/Tonejs/Tone.js/blob/dev/LICENSE.md).
