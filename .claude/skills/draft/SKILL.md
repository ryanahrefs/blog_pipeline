---
name: draft
description: Expand an outline into a full article draft
argument-hint: [outline-file]
allowed-tools: Read, Write
---

# Draft Skill

Expand a structured outline into a complete article draft, following Ahrefs-style content guidelines.

**Important**: This skill uses section-by-section drafting to ensure consistent quality throughout. Each H2 section is written independently with minimal context, preventing quality degradation in later sections.

## Input

**Outline file path** - Path to the outline file (from `/outline` skill)

---

## Style Reference

Before drafting, read `./reference/style-reference.md` to calibrate voice and tone. If no style reference exists, proceed with default guidelines.

The style reference provides a gold-standard example of the voice, rhythm, and patterns to emulate. You'll extract a compact Style Card from it in Phase 0.

---

## Core Writing Principles

When expanding the outline into a full draft:

1. **Specific examples for every point** - Never make a claim without illustrating it
2. **First-person experiences** - Use "I" and "We", include anecdotes
3. **Include opinions** - Take a stance, don't be wishy-washy
4. **Be detailed and exhaustive** - Cover topics thoroughly
5. **MECE structure** - Mutually exclusive sections, collectively exhaustive coverage
6. **BLUF principle** - Bottom Line Up Front, state the key point immediately
7. **Humor and personality** - Be human, not robotic
8. **Avoid exaggerated language** - No "mastery of data", "revolutionary", "game-changing"
9. **Reference Ahrefs naturally** - Mention relevant tools/features when they genuinely help

---

## Style Guidelines

### Voice and Tone
- Write in **first person** (I/We)
- Use **American English** (optimize, not optimise)
- **Casual tone** - Start sentences with "But..." or "So..." when it flows naturally
- **No swearing** or questionable language (sucks, jerk, etc.)
- Be direct, not formal

### Sentence and Paragraph Structure
- **One thought per sentence**
- **Max 3 lines per paragraph** (keeps content scannable)
- **Avoid fluff** - Cut throat-clearing phrases like "If you've ever wondered..."
- **Simple language** - "seen" not "misconstrued"

### Length
- Target: **1,000-3,000 words** (based on outline word count targets)
- **As short as possible** - Educate simply, don't pad for word count
- Exclude details only 1% of readers care about

### Subheadings
- Use **H2-H6** hierarchy
- **Sentence case** ("What is bounce rate?" not "What Is Bounce Rate?")
- **One point per heading** (not "What is X, why it matters, and how to do it")
- **Under 15 words**
- **Never place subheadings back-to-back** - Add intro text between heading and subheading

---

## Content Structure

### Introduction (Under 100 words)

Use the **PAS formula**: Problem → Agitate → Solution

1. **Problem**: State the pain point or challenge
2. **Agitate**: Emphasize why it matters or what happens if ignored
3. **Solution**: Preview what the article will teach them

Example:
> Most websites get zero traffic from Google. That's not an exaggeration—96.55% of pages get no organic search traffic at all. But here's the thing: it doesn't have to be that way. In this guide, I'll show you exactly how to do SEO in 2026, step by step.

### Body Sections

Use the **inverted pyramid** for each section:
1. **Need to know** first (the essential point)
2. **Nice to know** second (supporting details, context)

#### Writing Definitions

Format: `[Term] [abbreviation if needed] [conjunction] [definition in 1-3 sentences]`

> **What is bounce rate?**
> Bounce rate is the percentage of visitors that take no further action after landing on a webpage, like clicking through to another page, leaving a comment, or adding an item to their cart.

If more explanation needed, expand below the definition.

#### Writing Explanations

Always explain **what** AND **why**:

> Install an image compression plugin like ShortPixel. This reduces file sizes without visible quality loss, which improves page speed—a confirmed Google ranking factor.

Not just:
> ~~Install an image compression plugin.~~

#### Writing Answers

For sections that answer a question, use this format:

`[Part of question] [conjunction] [brief answer]. [Further explanation]`

> **Why is SEO important?**
> SEO is important because higher rankings usually lead to more organic traffic. This is because 65.9% of searchers click one of the top three organic results.

Don't force this format if it feels unnatural.

#### Using Examples

Every major point needs a concrete example:

> Backlinks don't last forever. We lost 847 referring domains to ahrefs.com in the past 7 days alone—that's just how the web works. Old pages get deleted, sites shut down, and webmasters change their minds.

Examples should be:
- Specific (real numbers, real sites)
- Relevant to the point being made
- From personal experience when possible

#### Screenshots and Visuals

When a screenshot would help:
- Note where it should go: `[SCREENSHOT: Description of what to show]`
- If showing an Ahrefs report, note: `[SCREENSHOT: Site Explorer > Backlinks report for example.com]`
- For custom illustrations, describe: `[ILLUSTRATION: Flowchart showing X → Y → Z]`

---

## Ahrefs Product References

Naturally reference Ahrefs tools when they genuinely help the reader:

| Tool | When to Reference |
|------|-------------------|
| Site Explorer | Analyzing competitors, checking backlinks, viewing organic keywords |
| Keywords Explorer | Keyword research, search volume, keyword difficulty |
| Site Audit | Technical SEO issues, crawl errors |
| Rank Tracker | Monitoring keyword positions |
| Content Explorer | Finding popular content, link prospecting |
| Ahrefs Webmaster Tools | Free site audits for site owners |

**How to reference:**
> To find your competitors' top pages, go to Site Explorer, enter their domain, and check the "Top pages" report. You'll see which pages drive the most organic traffic.

**Don't:**
- Force mentions where they don't fit
- Sound like an advertisement
- Claim Ahrefs is the only solution

---

## Conclusion

### Final Thoughts Section

Write a short conclusion (under 150 words) that:
1. Summarizes the core takeaway
2. Provides one actionable next step or extra insight

End every post with:

> Got questions? Ping me [on Twitter](https://twitter.com/[author-handle]).

---

## Workflow: Section-by-Section Drafting

This workflow prevents quality degradation by writing each section independently with minimal context.

### Phase 0: Style Calibration

Before writing, read `./reference/style-reference.md` and extract a compact **Style Card**:

#### Extract from the reference:

1. **Voice markers** (3 examples):
   - How first-person is used (e.g., "I've tested this on 50+ sites...")
   - Casual phrasing patterns (e.g., starting sentences with "But..." or "So...")
   - Opinion signals (e.g., "Here's the thing:")

2. **BLUF examples** (2 examples):
   - Copy two section openers that lead with the main point

3. **Transition patterns** (2 examples):
   - How sections connect to each other

4. **Specificity markers** (2 examples):
   - How numbers, names, and details are woven in

5. **Anecdote structure** (1 example):
   - A complete first-person anecdote showing the pattern

#### Create Style Card:

Write a ~200-word Style Card summarizing these patterns. This card will be referenced when writing each section.

Example Style Card format:
> **Voice**: First-person, casual ("I've found...", "Here's the thing:"),
> starts sentences with conjunctions. Direct opinions stated as fact.
>
> **BLUFs**: "[Example BLUF from reference]" — notice how [pattern].
>
> **Transitions**: Uses [pattern], e.g., "[example]"
>
> **Specificity**: Numbers in context ("3x more traffic"), named tools,
> time frames ("in the past 7 days").
>
> **Anecdote pattern**: Setup (what I did) → Result (what happened) →
> Lesson (what it means for you).

If no style reference file exists, skip this phase and proceed with default guidelines.

### Phase 1: Setup

1. **Read the outline** to understand:
   - Target keyword and word count
   - Thesis and key points
   - Section structure and BLUFs
   - Evidence placeholders to expand

2. **Extract article metadata** to keep in mind throughout:
   - Keyword
   - Thesis statement
   - Target word count
   - Voice/tone notes

3. **Create the draft file** with metadata header:
   ```markdown
   # [Article Title]

   **Target Keyword**: [keyword]
   **Word Count**: [in progress]
   **Status**: Drafting

   ---
   ```

### Phase 2: Section-by-Section Drafting

**Critical**: Write each H2 section as an independent unit. Do NOT load the entire growing draft while writing. Each section should receive your full attention as if it were the only section.

For each H2 section in the outline:

1. **Ground in reference**: Quote ONE passage from the style reference that exemplifies what this section needs most:
   - For tip/how-to sections → quote an anecdote or specific example
   - For definition sections → quote a BLUF opener
   - For explanation sections → quote a what+why passage

   This forces meaningful engagement with the reference voice before writing.

2. **Load context**:
   - Style Card (~200 words from Phase 0)
   - Article metadata (keyword, thesis)
   - This section's outline content (BLUF, sub-points, evidence)
   - Previous section's last paragraph (for transition continuity)
   - Next section's header and BLUF (for foreshadowing)

3. **Write the complete section** matching the voice and patterns from your quoted passage and Style Card:
   - Open with the BLUF (need to know first)
   - Include at least one specific example (number, name, or personal experience)
   - Use first-person voice ("I", "We", "I've found that...")
   - Add screenshot/illustration notes where helpful
   - Target the section's word count from outline
   - Keep paragraphs under 3 lines

4. **Append the completed section** to the draft file

5. **Move to the next section**

### Phase 3: Introduction & Conclusion

**Write the introduction AFTER body sections**:
- Now you know what the article actually covers
- Use PAS formula (under 100 words)
- Insert at the top of the draft

**Write the conclusion LAST**:
- Can synthesize the full article
- Include "Final thoughts" and Twitter CTA
- Under 150 words

### Phase 4: Assembly Review

After all sections are written:

1. **Read the complete draft** from start to finish
2. **Check transitions** between sections:
   - Do they flow naturally?
   - Add transition sentences if needed
3. **Verify consistency**:
   - Consistent terminology throughout
   - Voice doesn't shift between sections
   - No contradictions
4. **Update metadata**:
   - Final word count
   - Status: "First Draft"

---

## Per-Section Quality Requirements

Each section MUST include:
- [ ] BLUF in first 1-2 sentences
- [ ] At least one specific example (number, name, or personal experience)
- [ ] First-person voice ("I", "We", "I've found that...")
- [ ] Connection to article thesis or previous section
- [ ] No paragraphs over 3 lines

**If a section feels thin**, add:
- A personal anecdote ("When I first tried this...")
- A specific data point ("In our analysis of 1,000 sites...")
- A counterargument and response ("You might think X, but actually...")
- A "here's what this means in practice" explanation
- A common mistake to avoid

**Quality check**: The 9th section should be as rich as the 1st. If later sections feel rushed, you're not following the section-by-section approach correctly.

---

## Output

Save the draft to `./4-drafts/[keyword-slug].md`:

```markdown
# [Article Title]

**Target Keyword**: [keyword]
**Word Count**: [actual count] / [target]
**Status**: First Draft

---

[Full article content in markdown...]

---

## Draft Notes

**Screenshots needed:**
- [List of screenshots to capture]

**Illustrations needed:**
- [List of custom graphics to create]

**Fact-check:**
- [List of claims that need source verification]

**Questions for review:**
- [Any uncertainties or alternative approaches to discuss]
```

---

## Example Usage

```
/draft ./3-outlines-annotated/pinterest-seo.md
```

---

## Reference: Ahrefs Blog Examples

Study these posts for tone and style:

1. **"SEO Is the Worst It's Ever Been (And It's Still Your Best Marketing Channel)"** - Strong opinion backed by data, conversational, witty, BLUF

2. **"How to Analyze a Sudden Traffic Drop"** - Step-by-step, exhaustive, empathetic tone, references tools at point of use

3. **"63% of Websites Receive AI Traffic"** - Data-driven, key findings bulleted upfront, explains what findings mean for readers

---

## Quality Checklist

Before finalizing, verify:

| Check | Requirement |
|-------|-------------|
| Examples | Every major point has a specific example |
| Voice | First-person (I/We) throughout |
| Opinions | Clear stance taken, not wishy-washy |
| Fluff | No throat-clearing, no filler |
| Paragraphs | Max 3 lines each |
| Subheadings | Sentence case, under 15 words, one point each |
| Language | No exaggerated words (revolutionary, game-changing) |
| Ahrefs | References are natural and helpful |
| Length | Within target word count |
| Intro | Under 100 words, uses PAS |
| Conclusion | Has "Final thoughts" and Twitter CTA |
| Consistency | Later sections as rich as earlier ones |
