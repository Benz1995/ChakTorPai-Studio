---
name: motion-chatterbox
description: Prepare or integrate Chatterbox voiceovers for supported languages in this content project. Use for an explicit Chatterbox voice request or provider comparison; retain the existing F5-TTS path for Thai unless a verified Thai-capable checkpoint is supplied.
---

# Chatterbox voiceovers

Read [project integration](../motion-studio/references/project-integration.md) and the [render contract](../motion-studio/references/render-contract.md). Check [upstream verification](references/upstream.json) before selecting a model.

## Choose a model that supports the requested language

- Upstream provides separate English, Turbo/Nano, and multilingual variants. Select an explicit checkpoint and pin the compatible package/runtime rather than assuming their APIs and language support are interchangeable.
- The multilingual language list verified on 2026-10-26 does **not** include Thai (`th`). Do not pass an invented Thai language ID or claim Thai readiness from the word multilingual.
- For this project's Thai narration, retain the existing F5-TTS-THAI provider. A different Thai-capable fork/checkpoint is a separate candidate that needs its own source, model-card, and sample verification.
- Use a reference recording whose speaker and usage are covered by the user's existing permission. Reuse established permission; resolve a missing speaker/source permission only when it affects the requested voice.

## Prepare a bounded local run

1. Inspect existing Python environments, model cache, torch/CUDA compatibility, RAM/VRAM, and competing F5/SDXL jobs before loading another model.
2. Use a separate environment or service for an experimental provider so its dependency versions do not destabilize the working local TTS/image environment.
3. Record model/checkpoint identity, package version, selected language, reference-file hash, exact narration text, and synthesis parameters.
4. Start with one short representative scene. Listen for language, name pronunciation, identity, unwanted continuation, repetition, and pauses before batching.
5. Preserve the original generated audio, then produce the delivery format expected by the app and probe its actual duration.

## Connect to Content Studio when requested

- The current `VoiceProvider` union and provider registry contain `elevenlabs`, `local`, and `mock`; Chatterbox is not registered merely because this skill exists.
- For a one-off delivery, upload the generated audio through the existing scene-audio endpoint and keep its source receipt beside the asset.
- A reusable integration needs an explicit provider adapter in `server/tts`, a distinct provider ID in shared types, health/status reporting, and the existing `SynthResult` contract.
- Return the actual generated MP3 path; let the existing server duration probe determine scene timing.
- Populate `audioText` with the script that produced the audio. Do not label synthesized speech as current after the script changes.
- Chatterbox audio alone does not establish per-word timestamps. Keep estimated captions or add a separately verified transcription/alignment stage.
- Keep generated watermarking intact. Model/software licensing and the permission to use a reference voice are separate inputs.

## Verify observable output

- Decode the whole audio and verify nonzero duration and the expected channel/sample format.
- Listen to the whole short sample and representative final scenes; technical decoding and ASR do not prove voice quality.
- Check the first/last spoken word against the scene lead-in/tail and inspect captions at speech boundaries.
- Report model availability, generated audio, listening review, and final render as distinct outcomes.

## Sources

[Chatterbox README and supported languages](https://github.com/resemble-ai/chatterbox/blob/master/README.md), [source license](https://github.com/resemble-ai/chatterbox/blob/master/LICENSE).
