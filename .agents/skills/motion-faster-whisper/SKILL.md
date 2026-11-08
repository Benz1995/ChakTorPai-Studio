---
name: motion-faster-whisper
description: Transcribe recorded or generated narration with faster-whisper and prepare reviewed caption sidecars or timing data for Content Studio. Use for ASR, not as a claim of forced alignment or automatic approval of the authored script.
---

# faster-whisper captions

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). Upstream runtime and license sources are in [upstream.json](references/upstream.json).

## Establish transcript ownership

- For an unknown recording, ASR produces a draft transcript from the sound.
- For generated narration with an authored script, preserve that script and compare ASR against it; do not overwrite intentional wording, names, numbers, or pronunciation spellings automatically.
- `word_timestamps=True` produces recognized-word timing. It does not force-align an arbitrary supplied script to the audio.
- Keep the original transcript, reviewed text, timestamps, model/settings, and source-audio hash so corrections remain traceable.

## Run within the available resources

1. Inspect existing environments and cached models before downloading or loading another model. Keep an experimental ASR runtime separate from the working local F5/SDXL environment when dependency requirements conflict.
2. Select a multilingual model for Thai; do not select an English-only checkpoint based only on speed. Models already on this machine are listed in `content-studio/local-asr/README.md`: `thonburian-whisper-th-large-v3` (Thai fine-tune, best for Thai), `large-v3` and `large-v3-turbo`. Run them through `content-studio/scripts/recap-transcribe.py` (`--probe` shows the device and cached models; `RECAP_ASR_MODEL=<name>` picks one; `RECAP_ASR_DEVICE=cpu` when CUDA fails, e.g. missing `cublas64_12`). To check **how numbers and names were spoken** use Thonburian: `large-v3-turbo` writes digits ("11.11"), so it cannot show whether the voice said "สิบเอ็ดสิบเอ็ด" or "สิบเอ็ดจุดหนึ่งหนึ่ง". Narration checks are covered in [thai-voiceover](../thai-voiceover/SKILL.md).
3. Select CPU/GPU and compute type from measured RAM/VRAM and compatible CTranslate2/CUDA/cuDNN versions. Verify current upstream requirements before installing.
4. Set the known language when appropriate, enable word timestamps when needed, and choose VAD deliberately for the recording rather than stripping meaningful pauses blindly.
5. Iterate the returned segment generator to completion; receiving the generator is not a completed transcription.
6. Serialize segments/words to a sidecar with time units, source duration, language, model identity, and all options that affect the result.

## Map to this project correctly

- `Scene.words` contains `{text,start,end}` in seconds relative to the start of the scene voice audio, not absolute composition time.
- Transcribing scene audio separately avoids accidentally adding a previous scene or transition offset. For a full mixed track, retain explicit scene offsets and validate the mapping.
- Remotion already adds the narration lead-in; do not add it a second time to scene-relative word timestamps.
- The current content-update endpoint preserves server-owned audio fields; posting a `words` array in ordinary `update_content` does not establish an ASR import feature.
- Deliver reviewed SRT/VTT/JSON sidecars for one-off work. A reusable app integration needs a validated caption-import endpoint or adapter that updates words and matching audio/script provenance together.
- Thai ASR token boundaries can differ from `Intl.Segmenter` boundaries. Align reviewed tokens explicitly instead of assigning timings by array index.
- Keep segment times ordered and within the actual audio; handle punctuation, silence, repetitions, and missing/extra recognized words explicitly.

## Verify observable output

- Listen while inspecting captions at the beginning, fast phrases, proper names/numbers, long pauses, and the final spoken word.
- Check monotonic starts, `end >= start`, positive cue duration, and bounds against probed audio duration.
- Inspect caption wrapping and Thai combining marks in representative rendered frames.
- Report ASR output, text review, timing review, and rendered captions separately. Successful inference alone is not caption approval.

## Sources

[faster-whisper README](https://github.com/SYSTRAN/faster-whisper/blob/master/README.md), [license](https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE).
