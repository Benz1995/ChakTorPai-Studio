---
name: flowmusic-sfx
description: Generate, reconcile, check and import FlowMusic Space sound effects into BigO Content Studio, including existing scheduled queue runs. Use for FlowMusic SFX requests and the local sound-library queue; this workflow produces procedural Space synthesis, not Lyria songs.
---

# FlowMusic SFX operator

Operate `B:/ChatGPT/BigO/content-studio` through its local sound API/MCP and the normal FlowMusic UI. Read [the sound-library contract](../../../content-studio/docs/sound-library.md) when API fields or states are needed. The app owns its catalog, jobs and imported media; do not edit their JSON directly.

## Queue and authorization

For a scheduled run, read `GET /api/sounds/worker-status` and `/api/sounds/jobs` first. Status contains `enabled`, optional `automationId`, `intervalMinutes: 5`, `maxPerRun: 6`, `providerPageUrl`, and optional `lastRunAt`, `lastCompletedAt`, `lastError`. Respect `enabled` and the six-job budget; if disabled or no eligible jobs exist, use GET only and finish quietly without opening a browser. Do not create another automation, enable a disabled worker, or change its schedule from a replayed heartbeat. A directly requested one-off task uses its own explicit scope.

Use `PUT /api/sounds/worker-status` to write `lastRunAt` only when starting a real eligible run, `lastCompletedAt` only when that run actually finishes, and an observed `lastError` when applicable. Use UTC ISO timestamps. Clear `lastError` with `null` after a successful run, not merely after a successful status read. Preserve `enabled` and `automationId`; never manufacture heartbeat/completion evidence.

Handle only queued jobs in these categories, with `targetSeconds` from 0.05 to 10: `whoosh`, `impact`, `click`, `success`, `glitch`, `riser`. Map the `success` category to the factory's **chime** card. Unsupported requests stay queued for a suitable operator; do not silently change their intent. Process one job at a time, within the run budget.

The current verified Space is **v9**, with a native **Collection** selector. Use **Original 6** for the category mappings above. A job explicitly tagged `preset:<key>` can select the matching card in **New 20** instead; verify its visible key before using it. The new keys are `whoosh_swipe`, `whoosh_whip`, `whoosh_air`, `whoosh_reverse`, `impact_punch`, `impact_sub`, `impact_metal`, `impact_crunch`, `click_tap`, `click_toggle`, `click_key`, `click_pop`, `success_coin`, `success_levelup`, `success_quest`, `success_sparkle`, `glitch_tick`, `glitch_stutter`, `glitch_databurst`, `glitch_zap`. Keep the job's category and explicit intent; do not substitute a generic original preset for a named new recipe. Scheduled runs still have the six-job limit; a direct request for a larger batch uses its explicit requested count.

Reuse existing `requestKey` identities. Read job receipts and any existing ready asset before acting. Never reclaim or regenerate `dispatching`, `submitted`, `downloading`, `qc` or `uncertain` work. Reconcile its known result instead. Expired leases are eligible only when the core API confirms no provider dispatch occurred.

## Open the verified factory

The setup factory is the private FlowMusic Space reached from:
`https://www.flowmusic.app/session/67a56d7e-e836-4c7c-8ee1-a0a20dbfff6d`.
Prefer an updated stable `providerPageUrl` from the worker configuration or the current observed UI. Verify the signed-in Chrome account is **Astra Elysia** before external actions.

All real website navigation, inspection, clicks, filling and download actions use the documented **Cua** browser APIs, including its documented locator API. Initialize/read their current documentation before use. Do not use standalone Playwright, CDP, external network endpoints, or copied browser cookies to control FlowMusic.

The embedded preview can be `about:blank` while BrowserUse pauses its document. If needed, read the iframe URL from the observed UI and open that exact URL in a fresh tab in the same Chrome session through Cua. Keep it in private runtime variables only: its query can contain a JWT. Never print it, save it, put it in job metadata, or share it. Use the stable FlowMusic page for provenance.

FlowMusic Spaces rejected external/localhost backend calls and token-exchange automation. Do not add, inject or disguise a bridge to bypass that boundary. This operator uses ordinary UI controls and the local app separately. Do not publish/share the Space, purchase credits, subscribe, or switch providers as part of a queue run.

## One auditable download

1. Inspect the current factory controls. Use **v4 or later**, which applies linked stereo headroom before PCM encoding. v3 Impact produced 102 clipped samples; keep its evidence, but do not use it as a standard. The verified v9 component exposes Original 6 and New 20 collections, with `article[data-preset="<key>"]`, labelled **Duration** and **Seed** number inputs, global seed `42`, and **Download WAV**. Select the appropriate collection before finding a card. If the UI differs, inspect it before relying on the filename formula. For private preview tabs use `playwright.domSnapshot()` or read-only DOM observations, which omit the private URL; `getAXState()` can print the iframe URL/token in its automatic metadata.
2. Claim the queued job through `claim_sound_job` or `POST /api/sounds/jobs/:id/claim` with `{}`. Retain its returned `attemptId`. Choose a numeric card seed deterministically from the job/attempt identity, within the observed UI range. Set the card duration and seed through Cua, then read their actual values back.
3. For verified v4/v9, predict the exact download name:
   `` `${preset}_${String(Number(duration))}s_seed${Number(cardSeed) + 42}_48k.wav` ``.
   Probe only that known path in `C:/Users/usEr/Downloads` before clicking. If it exists, reconcile its matching receipts, timestamp and hash first. Do not overwrite or relabel an unexplained file; before dispatch, a different unused supported seed may be chosen and recorded.
4. Persist a **dispatching** receipt before the single Download WAV click. Include the selected preset, actual duration, card/global seeds, exact expected filename and stable provider page in the receipt message. This intent is the recovery record if the UI operation becomes ambiguous.
5. Click Download WAV once through Cua, then read the updated UI. Do **not** use `waitForEvent('download')`: in the observed session the WAV downloaded but that wait timed out and reset the tool kernel. Check the specific predicted file with bounded filesystem probes instead; compare against the pre-click baseline, require a fresh completed file and stable size, and probe/decode it. Do not scan unrelated downloads or click again because a tool wait timed out.
6. Only after fresh-file evidence, record **submitted** with the matching `attemptId`, stable `providerPageUrl` and `providerMode: 'space-synthesis'`. Import the actual file using `import_flowmusic_sound` or multipart `POST /api/sounds/jobs/:id/import`: field `file`, and `metadata` JSON containing those identities and provenance. Omit `providerResultId` when the Space exposes no native result ID; do not invent one from a filename. Read back the resulting ready asset and QC before taking another job.

The local bookkeeping helper `content-studio/scripts/flowmusic-operator.ts` can prepare an observed recipe with `prepare <jobId> <actualSeed> --preset <visibleKey> --space-version <actualVersion> --brief`, then `import <jobId> --brief` after the single UI download. It does not operate FlowMusic. Import retains job tags and a completed re-import reconciles with GETs without uploading or sending another provider receipt. Preserve the recorded actual version: the 20-recipe request started as v5 but the provider completed it through incremental edits as v9.

If anything is unknown after dispatch, record **uncertain** when possible and stop this attempt. Never regenerate it automatically. Before dispatch, missing login/quota may become `needs_login`/`quota_blocked` only through admissible core transitions; otherwise leave queued work unchanged and record the worker issue. A successful click, file name or provider receipt alone is not a ready asset.

## Verify and report

Use the existing [earshot skill](../earshot/SKILL.md) for sound measurements and prompt-match evidence before describing quality. Core import must probe and fully decode the audio, preserve its master/stereo, and store SHA/provenance/QC. Earshot scores are model evidence, not human listening or copyright approval.

After import require an explicit `qc.clippedSamples: 0` for automatic use. A v4 Impact trial measured -3.7 dBTP and zero clipped samples; that is evidence for that file only. The library retains defective imports for provenance, with attachment and automatic selection blocked.

The verified setup whoosh was downloaded as `C:/Users/usEr/Downloads/whoosh_1.2s_seed1379_48k.wav` and matched the tested whoosh description at `z +4.04`; that historical check does not approve future sounds. Recheck each imported result.

Call these assets **FlowMusic Space procedural effects / space-synthesis**, not Lyria-generated recordings. Report completed assets and meaningful failures or required user action; stay quiet when the queue or blocked state has not changed. Do not send external messages.
