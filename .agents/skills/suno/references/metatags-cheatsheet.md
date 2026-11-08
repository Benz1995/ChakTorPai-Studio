# Suno Metatags Cheatsheet (community conventions)

Suno publishes no official tag specification. These tags come from community practice on earlier models and
are still widely used on v6 (Nov 2026); confirm each by listening. Elyndraze avoids choir, belting, whisper
outros and heavy backing vocals (brand/BRAND.md), so several tags below are listed for completeness only.
Delivery cues inside a section tag are written either after a colon or a dash; keep them short so they are not sung.

---

## 1. Structural Tags (Section Control)

Place each tag on its own line in the Lyrics box. Always enclose in brackets `[ ]`.

| Metatag | Purpose | Example |
| :--- | :--- | :--- |
| `[Intro]` | Sets up the introductory atmosphere and instrumentation. | `[Intro - Soft electric piano, warm vinyl crackle]` |
| `[Verse 1]` / `[Verse 2]` | Storytelling section, typically lower dynamic intensity. | `[Verse 1 - Acoustic guitar and subtle bass]` |
| `[Pre-Chorus]` | Builds tension and harmonic lift leading toward the hook. | `[Pre-Chorus - Rising drum rolls, swelling synths]` |
| `[Chorus]` / `[Hook]` | The melodic and emotional centerpiece. High energy. | `[Chorus - Full band, stadium reverb, vocal harmonies]` |
| `[Bridge]` | Contrasting section in rhythm, melody, or emotional tone. | `[Bridge - Stripped down, floor tom and whisper vocal]` |
| `[Interlude]` | Short instrumental passage between sections. | `[Interlude - Smooth funky slap bass lick]` |
| `[Guitar Solo]` | Dedicated instrumental solo section. | `[Guitar Solo - Emotional blues bends, high register]` |
| `[Synth Solo]` | Synthesizer or keyboard solo lead. | `[Synth Solo - 80s analog pitch-bent lead]` |
| `[Drop]` | Massive bass drop in EDM / Dance / Modern Pop. | `[Drop - Punchy 808 sub-bass, heavy four-on-the-floor]` |
| `[Breakdown]` | Strips away all percussion, leaving pads or single instruments. | `[Breakdown - Ambient pads only, no drums]` |
| `[Build]` / `[Build-up]` | Accelerates tempo, snare rolls, and riser effects. | `[Build-up - Fast snare crescendo, rising filter sweep]` |
| `[Outro]` | Concluding section winding down the arrangement. | `[Outro - Acoustic guitar strumming slow, fading ambient]` |
| `[Big Finish]` | Dramatic, powerful final climax right before the end. | `[Big Finish - Power chords ring out with cymbals]` |
| `[Drum Kick Stop]` | Specific clean drum strike finish. | `[Drum Kick Stop]` |
| `[End]` | Hard stop command signaling the AI to terminate audio. | `[End]` |

---

## 2. Vocal Performance & Styling Tags

Use these to guide timbre, emotion, and singing technique:

### Vocal Range & Gender
- `[Male Vocal]`
- `[Female Vocal]`
- `[Duet]`
- `[Male and Female Unison]`
- `[Boyband Harmonies]`
- `[Choir Vocals]`

### Vocal Delivery & Technique
- `[Belted Vocals]` – Powerful, chest-voice projection for climaxes
- `[Falsetto]` – High, airy, head-voice singing
- `[Whisper]` or `[Breathy Vocal]` – Intimate, close-mic ASMR-like texture
- `[Spoken Word]` – Spoken narration without singing pitch
- `[Call and Response]` – Lead vocal line followed by echoing backing vocals
- `[Ad-libs]` – Improvisational vocal runs, hums, or chants
- `[Acapella]` – Vocals isolated without background instruments
- `[Backing Vocals: (word)]` – Secondary vocalists singing specific harmony words

---

## 3. Formatting Rules to Prevent Accidental Singing

If you write instructions like `(Sing loudly)` or `[Chorus: Sing with passion]`, Suno might literally speak or sing the words "Sing with passion".

To prevent this:
1. **Use double slashes `//` or hyphens `-`:**
   - ✅ `[Chorus // High energy, massive drums]`
   - ✅ `[Verse 1 - Soft acoustic guitar only]`
   - ❌ `[Chorus: Please sing this part very loud]`
2. **Backing vocals syntax:**
   - Use parentheses inside the lyric line for harmonies:
     ```text
     จะกอดเธอเอาไว้ (กอดเธอไว้)
     ไม่ให้เธอไปไหน (ไม่ให้ไป)
     ```
3. **Sound effect cues:**
   - `[Gasp]`
   - `[Laughter]`
   - `[Sigh]`
   - `[Finger Snap]`
