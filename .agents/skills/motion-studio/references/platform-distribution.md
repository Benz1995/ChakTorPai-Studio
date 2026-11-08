# Platform distribution and retention

Use this when a request is about reach, "ให้ AI ดันฟีด", hooks, length, calls to action,
or why a clip did or did not spread. Plan for it before writing the script, check it
before rendering, and read real analytics after posting. Keep three kinds of claims
apart: what platforms state, what creators observe, and folklore with exact numbers.

## What platforms actually state

| Claim | Status | Source |
| --- | --- | --- |
| Recommendations are personalised from interactions (likes, shares, comments, follows, watching), video information (captions, sounds, hashtags) and lower-weighted device/account settings | Stated by TikTok | [TikTok: How TikTok recommends videos #ForYou](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you/) |
| Top Instagram signals are watch time, likes per reach and sends per reach; sends matter slightly more for non-followers, likes for followers | Stated by Adam Mosseri, Jan 2025 | [Social Media Today](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/) |
| Posts that ask for likes, comments, shares, votes or tags to game ranking ("engagement bait") are demoted; Pages that repeat it are demoted further | Stated by Meta | [Meta: Fighting Engagement Bait](https://about.fb.com/news/2017/12/news-feed-fyi-fighting-engagement-bait-on-facebook/) |
| Reposting others' videos without meaningful edits or credit reduces distribution and monetization; commentary, reactions and a new angle are exempt | Stated by Meta, Jul 2025 | [TechCrunch](https://techcrunch.com/?p=3027715), [MediaNama](https://www.medianama.com/2025/07/223-meta-cracks-down-on-unoriginal-facebook-content/) |
| YouTube Studio reports Shorts "viewed vs. swiped away" | Real metric; targets quoted online are unofficial | [Streamlabs guide](https://streamlabs.com/content-hub/post/youtube-shorts-algorithm) |

Consistent with these: a clip is first shown to a limited audience and keeps spreading
while those viewers keep watching and interacting. Follower count is not listed as a
ranking input, so small accounts can reach non-followers when retention is strong.

## Folklore to not repeat as fact

Creator videos often state fixed rounds ("300–500 → 3,000 → 10,000 viewers"), fixed
completion thresholds ("15% for 1–30 s, 12% for 1 min, 8% for 1–2 min, 5% above"),
"likes must exceed 15% of viewers", "you compete only with clips of the same keyword,
posting time and length", and a fixed engagement ranking with comments always first.
No platform publishes these numbers, and Instagram's own statement puts sends/shares
above likes for reaching new people. Treat them as one creator's rules of thumb.
Never promise a reach outcome; describe what the clip is built to do.

Prompts such as "กด 1 ถ้าเห็นด้วย", "พิมพ์ 9 ในคอมเมนต์", "แชร์ให้ครบ 10 คน" or
"แท็กเพื่อน 3 คน" are engagement bait on Meta surfaces. Do not write them into scripts,
captions or on-screen text, even when a reference video recommends them.

## Turn it into production rules

1. **Stop the scroll in the first 1–2 seconds.** Open on the strongest image and say the
   core promise or conflict immediately (no greeting, no logo intro). On-screen text
   must be readable at frame 0. Recap: start from the most surprising beat, then go
   back in time.
2. **Keep an open loop.** State a question early and pay it off near the end; reveal
   one new fact or visual every few seconds. A long static shot or a looping clip is
   where viewers swipe away.
3. **Choose length from content density.** Cut sentences that do not move the story.
   A shorter clip watched to the end beats a longer one abandoned halfway; do not pad
   to reach a duration.
4. **Earn real interactions.** End with something worth reacting to: a genuine
   question about the content ("ถ้าเป็นมีมิ จะยอมให้พ่อทดสอบเจ้าชายไหม?"), a reason
   to send it ("ส่งให้เพื่อนที่พ่อหวงลูกสาวแบบนี้"), or a reason to save (a list, a
   how-to, a part 2). Ask once, naturally, and never ask for a specific token.
5. **Be original.** Recaps, highlights and reactions need new narration, your own
   structure and judgement, and credit to the source. Raw re-uploads of others'
   footage are reduced. Check platform rules and rights before publishing.
6. **Package for the feed.** Burned-in Thai captions (most people watch muted), text
   inside the 9:16 safe area (clear of the right-side buttons and bottom caption
   area), loudness about −14 LUFS with true peak below −1 dBTP, and a cover frame
   that states the topic.
7. **Measure after posting.** Read viewed-vs-swiped (Shorts) or 3-second views, average
   watch time and percentage viewed, shares/sends per reach, saves, comments and
   follows from reach. Change one thing per post (hook line, first shot, length) and
   compare. A local export says nothing about distribution until analytics exist.

## Check before rendering

Run the measurable part of these rules against a content:

```powershell
cd content-studio
npx tsx scripts/retention-check.ts <contentId>
```

It reports hook timing, the first-scene length, scenes that hold one visual too long
or loop recap footage, engagement-bait phrases, the ending, captions, originality
reminders for recap/highlight templates and, when a finished render exists, its
loudness and true peak. Warnings are prompts for judgement, not reach predictions;
fix what applies, then re-check. Creative fit still needs human viewing.
