# Thumbnail Brief + A/B Concepts

This sub-skill produces a script-aware thumbnail design brief with three A/B test variants, a title-thumbnail-hook alignment audit, and niche-specific CTR benchmarks. It turns the video's real conflict, viewer stake, and promised outcome into a compact visual proposition that remains compelling without overpromising.

## Inputs Required

| Input | Required | Description |
|-------|----------|-------------|
| Video title | Yes | The chosen title (or top candidate) |
| Topic | Yes | Video subject for visual concept ideation |
| Channel niche | Yes | Content category for benchmark context |
| Full script/transcript | Strongly recommended | Read end-to-end when supplied; this is the source of the thumbnail's concrete conflict, stakes, mechanism, proof, and caveats |
| Visual style | No | Existing brand style (colors, face prominence, text style) |
| Channel size | No | Helps set realistic CTR targets (default: small) |
| Competitor thumbnails | No | URLs or descriptions of competitor thumbnails for differentiation |
| Analytics/reference thumbnail | No | Existing CTR, traffic source, audience, or a winning thumbnail to diagnose; never treat CTR alone as proof of quality |

## Automatic Trigger & Input Defaults

Run this sub-skill automatically when the user pastes or attaches a script/transcript and asks to create, generate, design, improve, or write a prompt for a YouTube thumbnail. The user does not need to type `/youtube thumbnail`.

When the request is script-first:

- Infer the topic, audience, emotional axis, and channel type from the script.
- Use the supplied title; if none is supplied, create a provisional working title and clearly label it.
- Default the channel tier to **small** and the goal to **Growth/CTR** unless the user gives different context.
- Ask only one targeted question when a missing fact would materially change the visual claim or brand treatment; otherwise proceed with explicit assumptions.
- Always return the image-generation prompts in English, even when the thumbnail text itself is Vietnamese. Preserve the exact Vietnamese overlay wording and diacritics inside the English prompt.

## Reference Files

- `references/thumbnail-ctr-guide.md`
- `references/script-thumbnail-alignment.md`
- `references/seo-playbook.md`

## DataForSEO Research (When Available)

Analyse competitor thumbnails with live YouTube SERP data:

1. **Competitor thumbnail scan**: Run `serp_youtube_organic_live_advanced` with the video's target keyword to retrieve top-ranking videos with their `thumbnail_url` fields. This shows what visual styles currently dominate the SERP for this keyword.
2. **Channel context**: Use `serp_youtube_video_info_live_advanced` on the top 3-5 videos to get channel names and subscriber counts — understand whether top thumbnails come from authority channels or small creators.
3. **Differentiation check**: Compare the primary brief against competitor thumbnail patterns to ensure visual distinctiveness in the search results page.

**Fallback:** If DataForSEO is unavailable, use WebSearch for `[keyword] youtube` and manually review thumbnail patterns.

## Thumbnail Generation (When NanoBanana MCP Available)

When the NanoBanana MCP server is configured, generate actual thumbnail images using the `generate_image` tool:

**Tool:** `generate_image`

**Recommended settings for YouTube thumbnails:**
- `aspect_ratio`: `"16:9"` (YouTube standard)
- `resolution`: `"4k"` (maximum quality for 1280×720 YouTube requirement)
- `model_tier`: `"nb2"` (default — best balance of speed and quality for production assets)
- `output_path`: user's project directory or `~/nanobanana-images/`

**Workflow:**
1. After generating the primary thumbnail brief, convert it into a detailed image generation prompt
2. Generate the primary thumbnail: call `generate_image` with a prompt derived from the brief (focal point, expression, text overlay, colour palette, composition, and the script-grounded visual claim all specified)
3. Generate each A/B variant: call `generate_image` with the variant's modified prompt
4. Present all 4 images (primary + 3 variants) to the user for review, followed by the exact English prompts used for each image
5. If the user requests refinements, update the relevant prompt and regenerate the affected image; preserve the one-variable A/B logic

**Prompt engineering tips for thumbnails:**
- Specify "YouTube thumbnail style" in the prompt
- Include text rendering instructions: `text "[WORD]" in bold white sans-serif with black stroke`
- Specify face expressions precisely: "genuine shocked expression with wide eyes and open mouth"
- Include background colour: "solid [colour] background" or "blurred [scene] background"
- Add "high contrast, vibrant colours, clean composition" for thumbnail aesthetics
- Mention "legible at small size" to encourage clear focal points
- For policy/news topics, label proposals, possible outcomes, and pending decisions accurately; never depict a proposal as an enacted guarantee
- Use one concrete visual consequence from the script (for example: money that cannot buy an equivalent home, staying versus moving, or a replacement home) instead of generic "big change" imagery when the script supports it

**Fallback:** If NanoBanana MCP is unavailable, deliver the text-based thumbnail brief and the English prompts.
The brief and English prompts must still be delivered; an unavailable image tool is not a reason to omit the prompts.

## English Image-Prompt Standard

Always provide a complete English prompt for the primary thumbnail and for Variants A, B, and C. If an image-generation tool is available, use these prompts verbatim and return the corresponding images. The exact Vietnamese words intended for on-image text may remain in Vietnamese inside quotation marks; all visual and technical instructions stay in English.

Each prompt must specify:

1. **Format and purpose**: professional YouTube thumbnail, 16:9, 1920×1080 master, designed to remain legible at 168×94px.
2. **Script-grounded story**: the concrete conflict, viewer stake, and visual thesis; never add a fact that is absent from the script.
3. **Focal subject**: identity or object, age/role when relevant, expression, gaze direction, gesture, wardrobe, and approximate frame share.
4. **Composition**: subject position, text block position, safe margins, visual hierarchy, depth, and eye-flow.
5. **Background**: one relevant scene or symbol, simplified or blurred behind the text, with no distracting secondary story.
6. **Typography**: exact line breaks and wording, bold condensed sans-serif, casing, text colours, stroke/shadow, contrast, and approximate size.
7. **Lighting and palette**: cinematic but credible lighting, exact hex colours from the brief, controlled saturation, and separation between subject, background, and text.
8. **Production constraints**: clean 16:9 crop, no watermark, no random text, no extra faces, no invented logos, no clutter, no graphic violence, and no misleading visual claim.
9. **Negative prompt**: a separate concise list of failure modes to avoid, including illegible text, misspellings, extra words, distorted faces/hands, weak contrast, and busy composition.

If the generator is unreliable at rendering Vietnamese text, still include the exact intended text in the prompt and add a **Text Overlay Production Spec** after it so the wording can be typeset without interpretation. Never silently replace, translate, or shorten the approved overlay copy.

## Parallel Agents

Not required. This skill runs as a single sequential workflow.

## Execution Steps

1. **Load references**: Read `references/thumbnail-ctr-guide.md`, `references/script-thumbnail-alignment.md`, and `references/seo-playbook.md` before generating output.
2. **Read the source**: If a script/transcript is supplied, read it end-to-end. Extract the core conflict, viewer stake, new mechanism or change, proof anchor, uncertainty/caveat, and emotional axis. If no script is supplied, mark the promise map as provisional and do not invent specific claims.
3. **Split the promise**: Analyse what the title already communicates, what the thumbnail should add, and what the opening 5–20 seconds must prove. Flag any absolute thumbnail/title wording when the script only supports a proposal, possibility, or conditional outcome.
4. **Choose the visual mode**: Select the story-led mode — authority + policy reversal, personal loss/gain, conflict/question, number/scale, or transformation. For policy/news, a large relevant subject plus a compact consequence/reversal is the default starting point; use a different mode when the script's strongest image is more concrete.
5. **Build the primary brief**: Specify one focal subject, spatial layout, exact copy, hex colours, contrast treatment, visual flow, mobile behaviour, and the one-sentence viewer inference. Anchor the copy in the script's strongest conflict or consequence, not in a generic conclusion.
6. **Create 3 A/B variants**: Each variant changes exactly ONE meaningful variable from the primary concept — copy route, focal subject, or visual treatment — and states the hypothesis, target segment, and retention risk.
7. **Generate assets when available**: If NanoBanana MCP is configured, generate the primary and three variants from the briefs. Otherwise deliver production-ready prompts and text specifications only.
8. **Audit before delivery**: Run title-thumbnail synergy, promise fidelity, mobile legibility, policy/claim accuracy, and post-click retention audits. Set benchmarks from `thumbnail-ctr-guide.md`; interpret CTR alongside AVD/APV and watch-time share, especially when browse or returning viewers dominate impressions.

## Output Template

````
## Title-Thumbnail Analysis

- **Title**: [the video title]
- **Title communicates**: [What information the title already provides]
- **Thumbnail must add**: [The complementary information/emotion the thumbnail needs to convey]
- **Information split**: [Title handles X, thumbnail handles Y — no overlap]

---

## Script Promise Map

- **Core conflict**: [The tension or contradiction driving the video]
- **Viewer stake**: [What the target viewer could lose, gain, protect, or decide]
- **New mechanism/change**: [The proposal, rule, event, or mechanism that changes the situation]
- **Proof anchor**: [The example, number, authority, document, or case that makes the promise credible]
- **Uncertainty/caveat**: [What is proposed, conditional, unresolved, or not guaranteed]
- **Emotional axis**: [Fear, relief, anger, hope, disbelief, urgency, or another dominant feeling]
- **Opening handoff**: [The exact fact, image, or question the first 5–20 seconds should use to pay off the thumbnail]

**Script-grounded visual thesis**: [One sentence: “The viewer clicks because ..., and the video must quickly show ...”]

---

## Primary Thumbnail Brief

### Focal Point
- **Primary subject**: [What the eye should hit first — face, object, result, etc.]
- **Position**: [Where in the frame — rule of thirds placement, e.g., "Subject right-third, looking left toward text"]
- **Size**: [How much of the frame the focal point occupies — e.g., "60% of frame"]

### Expression/Emotion (if face-based)
- **Target emotion**: [Specific emotion — not just "surprised" but "genuine disbelief with raised eyebrows and open mouth"]
- **Eye direction**: [Looking at camera, looking at object, looking at text]
- **Avoid**: [What NOT to do — e.g., "No fake surprise, no closed-mouth smiles"]

### Text Overlay
- **Text**: [2–5 words per line; 3–5 total is the default, while 6–7 short words are allowed only when they form a compact, highly legible two-line hierarchy]
- **Font style**: [Bold sans-serif, handwritten, etc.]
- **Font size**: [Relative to frame — must be legible at 168x94px mobile size]
- **Position**: [Where the text sits — must not overlap the face/focal point]
- **Color**: [High contrast against background — specify exact pairing]
- **Stroke/shadow**: [Outline specifications for legibility]

### Color Palette
- **Primary color**: [Hex code + name] — [Role: background/dominant]
- **Secondary color**: [Hex code + name] — [Role: accent/text]
- **Contrast color**: [Hex code + name] — [Role: pop element that draws eye]
- **Color psychology**: [Why these colors work for this niche/emotion]

### Composition
- **Layout**: [Rule of thirds grid description]
- **Negative space**: [Where and how much — needed for text and visual breathing room]
- **Depth**: [Foreground/background relationship, blur, etc.]
- **Visual flow**: [How the eye moves through the thumbnail — entry point to exit point]

### Mobile Legibility Check
- **At 168x94px**: [What must still be visible — focal point, text, key element]
- **Remove at small size**: [Elements that become noise on mobile]
- **Text size minimum**: [Must pass the "arm's length phone" test]

### DO NOT Include
- [Specific element to avoid and why]
- [Specific element to avoid and why]
- [Specific element to avoid and why]

---

## English Image-Generation Prompts

Return these prompts even when images are generated. The prompt must be complete enough to paste into an image model without additional explanation.

### Primary Prompt

```text
Create a professional, high-CTR YouTube thumbnail for a [niche] video about [topic]. The script's central conflict is [conflict], and the viewer's stake is [stake]. Show [focal subject] with [specific expression/gesture] occupying approximately [percentage] of the frame on the [left/right]. Use a clean 16:9 composition at 1920x1080: [describe subject placement], [describe text block placement], and [describe the eye-flow]. The background is [one relevant scene], simplified and softly blurred so it supports the story without competing with the text.

Render only the exact Vietnamese overlay text "[LINE 1]" on the first line and "[LINE 2]" on the second line. Use a bold condensed sans-serif, all caps, [text colour] with a [stroke/shadow specification], strong separation from the background, generous line spacing, and safe margins. Use this palette: [hex colours]. Use dramatic but credible lighting, a sharp focal subject, controlled saturation, strong warm-versus-dark contrast, and a polished editorial-news thumbnail aesthetic. The visual must communicate [one-sentence viewer inference] without claiming more than the script supports. Make the face, main words, and one context cue readable at 168x94px. No watermark, no extra text, no random letters, no invented logos, no collage, no clutter.
```

### Negative Prompt

```text
illegible typography, misspelled Vietnamese words, missing diacritics, extra words, tiny text, low contrast, cluttered composition, multiple competing focal points, distorted face, deformed hands, plastic expression, generic stock-photo look, excessive arrows or icons, random logos, watermark, oversaturated colours, flat lighting, misleading symbols, graphic violence
```

### Variant Prompts

Repeat the complete prompt for **Variant A**, **Variant B**, and **Variant C**. State the single variable changed from the primary concept in one line before each prompt, then include its full English prompt and negative prompt. Do not use shorthand such as “same as above” because each prompt must be independently executable.

### Text Overlay Production Spec

- **Approved wording**: [exact Vietnamese text with diacritics and line breaks]
- **Font direction**: [bold condensed sans-serif / approved brand font]
- **Colour and contrast**: [hex codes, stroke, shadow, opacity]
- **Placement and safe area**: [spatial coordinates or frame percentages]
- **Hierarchy**: [which line is dominant and why]
- **Post-production note**: [whether to typeset the words in Canva/Photoshop after generating the visual base]

---

## A/B Test Variants

### Variant A: [Concept Name]
- **What changes from primary**: [One specific variable — color, text, expression, composition]
- **Why test this**: [Hypothesis for why this might outperform]
- **Target segment**: [Who this variant appeals to more — new viewers, returning, search, browse]
- **Predicted CTR direction**: [Higher/Lower than primary and why]

### Variant B: [Concept Name]
- **What changes from primary**: [One specific variable]
- **Why test this**: [Hypothesis]
- **Target segment**: [Who this appeals to]
- **Predicted CTR direction**: [Higher/Lower and why]

### Variant C: [Concept Name]
- **What changes from primary**: [One specific variable]
- **Why test this**: [Hypothesis]
- **Target segment**: [Who this appeals to]
- **Predicted CTR direction**: [Higher/Lower and why]

### A/B Testing Protocol
- **Minimum test duration**: [Hours/days before statistical significance]
- **Primary metric**: Watch-time share when using YouTube's thumbnail test; CTR is the packaging diagnostic
- **Secondary metric**: AVD and average percentage viewed (to ensure clicks are fulfilled)
- **Sample size note**: [Minimum impressions before drawing conclusions]

---

## Title + Thumbnail Synergy Check

| Rule | Status | Detail |
|------|--------|--------|
| Information split (no duplication) | [PASS/FAIL] | [What title says vs what thumbnail shows] |
| Emotional alignment | [PASS/FAIL] | [Title tone matches thumbnail emotion] |
| Curiosity amplification | [PASS/FAIL] | [Together they create more curiosity than either alone] |
| Text overlap check | [PASS/FAIL] | [Thumbnail text does not repeat title words] |
| Mobile readability | [PASS/FAIL] | [Both title and thumbnail work at mobile size] |

**Synergy verdict**: [Strong/Moderate/Weak] — [one-sentence assessment]

[If FAIL on any rule: specific fix recommendation]

---

## Promise-Fidelity & Retention Audit

| Check | Status | Evidence / Fix |
|------|--------|----------------|
| A viewer can state the thumbnail's promise in one sentence | [PASS/FAIL] | [What the viewer is likely to infer] |
| The opening 5–20 seconds proves or advances that promise | [PASS/FAIL] | [Exact opening beat that pays it off] |
| The script supports the wording without a misleading guarantee | [PASS/FAIL] | [Proposal/conditional language or required correction] |
| The visual uses the script's strongest concrete conflict or consequence | [PASS/FAIL] | [What was chosen and what was rejected] |
| Click quality is judged with retention, not CTR alone | [PASS/FAIL] | [AVD/APV/watch-time-share signal to monitor] |

**Risk verdict**: [Low/Moderate/High] — [If CTR is likely to be strong but retention weak, explain the promise gap and rewrite the opening or thumbnail]

---

## Benchmark Context

| Metric | This Niche Benchmark | Target for This Video | Source |
|--------|---------------------|----------------------|--------|
| Average CTR | [X%] | [Y%] | thumbnail-ctr-guide.md |
| Top 10% CTR | [X%] | — | thumbnail-ctr-guide.md |
| CTR by channel size ([tier]) | [X%] | [Y%] | thumbnail-ctr-guide.md |

**What the thumbnail must achieve**: [Specific CTR target with context — e.g., "Minimum 5.5% CTR to outperform niche average; 8%+ to reach top quartile for this channel size"]
````

## Quality Criteria

- Text overlay must use 2–5 words per line; 6–7 total short words are permitted only in a compact two-line layout that passes the 168x94px mobile test
- Color palette must include exact hex codes, not just color names
- The primary brief must be specific enough for a designer to execute without follow-up questions
- Each A/B variant must change exactly ONE variable from the primary concept — not multiple changes
- The synergy check must evaluate all 5 rules and flag any failures with fixes
- If a script/transcript is supplied, it must be read end-to-end and represented in the Script Promise Map
- At least one concept must express the script's core conflict, viewer stake, or concrete consequence — not only an abstract conclusion
- Proposal, pending decision, and conditional outcome language must not be presented as a guaranteed enacted result
- Do not call a brief high-potential if promise fidelity or mobile legibility scores below 4/5 in the reference framework
- Mobile legibility must be explicitly addressed (168x94px test)
- The "DO NOT Include" section must contain at least 3 specific items
- Every primary/variant image must have a matching, independently executable English prompt and negative prompt
- English prompts must specify format, script-grounded subject, composition, exact overlay wording, typography, palette, lighting, production constraints, and text-rendering risks
- Exact Vietnamese overlay text must be preserved with diacritics; if the model may misrender it, include a post-production Text Overlay Production Spec
- CTR benchmarks must reference the thumbnail-ctr-guide.md with niche-specific numbers
- No thumbnail brief may suggest duplicating information already in the title
- All composition directions must use spatial language a designer can act on (not "make it look good" but "subject occupies right third, 3px white stroke on text")
