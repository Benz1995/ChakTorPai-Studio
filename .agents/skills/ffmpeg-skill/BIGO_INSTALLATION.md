# BigO installation receipt

Installed from [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) at commit `1c37ad1cae49f1127cc82919ba9e73bb1f330c65`, upstream package version `2.17.2`, MIT license, on 2026-10-26 (Asia/Bangkok).

The official Codex `skill-installer/scripts/install-skill-from-github.py` helper installed the pinned repository root as `ffmpeg-skill`. The upstream `SKILL.md`, `README.md`, scripts, templates, references, license and MCP source are preserved. This local note and `installation-receipt.json` record the installation separately.

Copies are available at `C:/Users/usEr/.codex/skills/ffmpeg-skill` and `B:/ChatGPT/BigO/.agents/skills/ffmpeg-skill`. A project Claude entrypoint delegates to the canonical project copy. Existing `motion-ffmpeg` and `flowmusic-sfx` skills were not overwritten.

The skill covers 42 local FFmpeg editing/inspection tools: cuts, joins, captions, reframing, audio processing, loudness, delivery checks and exports. Its MCP source advertises 12 core tools by default, with the full set available through its documented configuration. Installing source does not register or start that MCP server.

Validation: upstream skill/instructions, package lifecycle metadata, installer and execution-wrapper sources were inspected; no credential collection, remote execution directive or unexpected network client was found in the reviewed entrypoints. This was a scoped static review, not a full security audit. Both skill copies passed the Codex skill validator in UTF-8 mode and their installed file manifests matched. Python, FFmpeg and ffprobe already exist on PATH; they were not installed or changed.

No upstream installer, editing script, doctor, ASR model download or MCP process was executed for this installation. Use `python` instead of `python3` for raw script examples on this Windows setup. The skill is discoverable on the next conversation turn.
