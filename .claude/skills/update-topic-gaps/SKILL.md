---
name: update-topic-gaps
description: Identify topic gaps by comparing article against current top-ranking content
argument-hint: [extracted-file]
allowed-tools: Read, Write, WebFetch, mcp__ahrefs__*
---

# Update Topic Gaps Skill

Analyze an extracted article against the current top-ranking content to identify topic gaps—sections or subtopics that competitors now cover but our article doesn't.

## Input

**Extracted file path** - Path to the extracted article (e.g., `./update-pipeline/1-extracted/programmatic-seo.md`)

---

## Why This Matters

The SERP evolves. Articles that ranked well when published may now lack coverage of:
- **New subtopics** that competitors have added
- **Questions** that People Also Ask now surfaces
- **Depth** that top-ranking pages now provide
- **Angles** that have emerged as important

This skill identifies what needs to be added to stay competitive.

---

## Workflow

### Phase 1: Understand the Current Article

1. **Read the extracted file**

2. **Extract article structure:**
   - Primary keyword (from title/URL)
   - All H2 and H3 headers
   - Major topics covered
   - Current word count

3. **Create topic inventory:**
   ```
   | Section | Topic | Subtopics Covered |
   |---------|-------|-------------------|
   | H2: Examples of programmatic SEO | Examples | Nomadlist, Zapier, Webflow, Wise |
   | H2: How to get started | Process | Find keywords, Build template, etc. |
   ```

---

### Phase 2: Analyze Current SERP

#### Step 1: Get Primary Keyword

Extract the primary keyword from the article's URL slug or title.

Example:
- URL: `programmatic-seo.md` → keyword: `programmatic seo`
- Title: "Keyword Research: The Beginner's Guide" → keyword: `keyword research`

#### Step 2: Pull SERP Overview

Call `mcp__ahrefs__serp-overview` with:
- `keyword`: Primary keyword
- `country`: "us"
- `select`: "position,url,title,domain_rating,traffic"
- `top_positions`: 10

**Note:** Skip our own URL (ahrefs.com) in the competitor list.

---

### Phase 3: Scrape Top Competitors

#### Step 1: Select Top 3 Competitors

From the SERP results, select the top 3 non-Ahrefs URLs to analyze.

**Prioritize:**
- High traffic pages
- Similar content type (guide vs. tool)
- Authoritative domains (DR 50+)

#### Step 2: Extract Competitor Structure

For each competitor URL, use WebFetch:

```
WebFetch: [competitor URL]
Prompt: Extract the complete heading structure from this article. List every H2 and H3 in order, formatted as:

## [H2 text]
### [H3 text]
### [H3 text]
## [H2 text]

Also note:
- Approximate word count
- Any unique sections or elements (calculators, tools, downloadable templates)
- Topics covered that seem distinct
```

**Record for each competitor:**
- Full H2/H3 structure
- Topics/themes covered
- Special elements
- Approximate word count

---

### Phase 4: Gap Analysis

#### Step 1: Build Topic Coverage Matrix

Create a comparison of topics across all articles:

```
| Topic | Our Article | Comp 1 | Comp 2 | Comp 3 | Gap? |
|-------|-------------|--------|--------|--------|------|
| Definition | ✓ | ✓ | ✓ | ✓ | No |
| Examples | ✓ | ✓ | ✓ | ✓ | No |
| Tools for pSEO | ✗ | ✓ | ✓ | ✗ | Yes (2/3) |
| Common mistakes | ✗ | ✓ | ✓ | ✓ | Yes (3/3) |
```

#### Step 2: Classify Gaps

| Coverage Pattern | Classification | Priority |
|------------------|----------------|----------|
| All 3 competitors cover, we don't | **CRITICAL GAP** | Must add |
| 2/3 competitors cover, we don't | **SIGNIFICANT GAP** | Should add |
| 1/3 competitors cover, we don't | **OPTIONAL GAP** | Consider adding |
| We cover, competitors don't | **DIFFERENTIATOR** | Keep/expand |

#### Step 3: Assess Gap Importance

For each gap, consider:
- Is this a core topic or tangential?
- Does it align with the article's intent?
- Would adding it require a new section or just a paragraph?
- Is it covered elsewhere on the Ahrefs blog? (internal link opportunity)

---

### Phase 5: Pull Related Questions

Call `mcp__ahrefs__keywords-explorer-matching-terms` with:
- `keywords`: Primary keyword
- `country`: "us"
- `select`: "keyword,volume"
- `order_by`: "volume:desc"
- `limit`: 20
- `terms`: "questions"

**Cross-reference questions against article content:**
- Which questions does the article answer?
- Which questions are NOT answered? (content gaps)
- Are there high-volume questions that deserve dedicated sections?

---

## Output

Save to `./update-pipeline/4-update-topic-gaps/[slug].md`:

```markdown
# Topic Gap Audit: [Article Title]

**Source**: ./update-pipeline/1-extracted/[slug].md
**Original URL**: [source URL]
**Audit Date**: [today]
**Primary Keyword**: [keyword]

---

## Current Article Structure

**Word Count**: [N] words
**H2 Sections**: [N]

| Section | Topic |
|---------|-------|
| H2: [header] | [topic] |
| H2: [header] | [topic] |

---

## SERP Analysis

**Keyword**: [keyword]
**Date**: [today]

### Top 10 Results

| Pos | Title | Domain | Traffic |
|-----|-------|--------|---------|
| 1 | [title] | [domain] | [traffic] |
| 2 | [title] | [domain] | [traffic] |
...

### Competitors Analyzed

1. **[Title]** - [domain]
   - URL: [url]
   - Word count: ~[N] words
   - Key sections: [list notable H2s]

2. **[Title]** - [domain]
   - URL: [url]
   - Word count: ~[N] words
   - Key sections: [list notable H2s]

3. **[Title]** - [domain]
   - URL: [url]
   - Word count: ~[N] words
   - Key sections: [list notable H2s]

---

## Topic Coverage Matrix

| Topic | Our Article | [Comp 1] | [Comp 2] | [Comp 3] | Status |
|-------|-------------|----------|----------|----------|--------|
| [topic] | ✓ | ✓ | ✓ | ✓ | Covered |
| [topic] | ✓ | ✓ | ✓ | ✗ | Covered |
| [topic] | ✗ | ✓ | ✓ | ✓ | **CRITICAL GAP** |
| [topic] | ✗ | ✓ | ✓ | ✗ | **SIGNIFICANT GAP** |
| [topic] | ✗ | ✓ | ✗ | ✗ | Optional |
| [topic] | ✓ | ✗ | ✗ | ✗ | Differentiator |

---

## Critical Gaps (All 3 Competitors Cover)

### 1. [Topic Name]

**What competitors cover:**
- [Comp 1]: [Brief description of their coverage]
- [Comp 2]: [Brief description]
- [Comp 3]: [Brief description]

**Recommended action:** Add new H2 section / Add subsection / Expand existing section

**Suggested heading:** "[Draft H2/H3]"

**Placement:** After "[existing section name]"

**Estimated addition:** [X] words

---

### 2. [Topic Name]

**What competitors cover:**
- [descriptions]

**Recommended action:** [action]

**Suggested heading:** "[heading]"

---

## Significant Gaps (2/3 Competitors Cover)

### 1. [Topic Name]

**Covered by:** [Comp 1], [Comp 2]

**Recommendation:** [Add / Consider / Skip]

**Notes:** [Why important or not]

---

## Questions Analysis

### High-Volume Questions Not Answered

| Question | Volume | Currently Answered? | Recommendation |
|----------|--------|---------------------|----------------|
| [question] | [vol] | No | Add FAQ / Add section |
| [question] | [vol] | Partially | Expand coverage |

### Questions Well Covered

| Question | Volume | Section |
|----------|--------|---------|
| [question] | [vol] | [where answered] |

---

## Depth Comparison

| Metric | Our Article | Comp Average | Gap |
|--------|-------------|--------------|-----|
| Word count | [N] | [N] | [+/- N] |
| H2 sections | [N] | [N] | [+/- N] |
| H3 sections | [N] | [N] | [+/- N] |
| Examples | [N] | [N] | [+/- N] |
| Images | [N] | [N] | [+/- N] |

**Depth assessment:** [Article is competitive / Needs expansion / Significantly shorter]

---

## Special Elements Gap

Elements competitors have that we don't:

| Element | Comp 1 | Comp 2 | Comp 3 | We Have? |
|---------|--------|--------|--------|----------|
| Calculator/tool | ✗ | ✓ | ✗ | ✗ |
| Downloadable template | ✓ | ✗ | ✓ | ✗ |
| Video embed | ✗ | ✓ | ✓ | ✗ |
| Checklist | ✓ | ✓ | ✓ | ✗ |

---

## Summary & Priorities

### Must Add (Critical Gaps)
1. [Topic] - [brief note]
2. [Topic] - [brief note]

### Should Add (Significant Gaps)
1. [Topic] - [brief note]

### Consider Adding (Optional)
1. [Topic] - [brief note]

### Differentiators to Preserve
1. [Topic we cover uniquely] - [why valuable]

---

## Estimated Update Scope

| Addition | Estimated Words | Priority |
|----------|-----------------|----------|
| [section name] | [N] words | Critical |
| [section name] | [N] words | Significant |
| **Total** | **[N] words** | |

**Current word count:** [N]
**Target word count:** [N] (competitive with top 3)
```

---

## Example Usage

```
/update-topic-gaps ./update-pipeline/1-extracted/programmatic-seo.md
```

**Output**: `./update-pipeline/4-update-topic-gaps/programmatic-seo.md`

---

## Reusing Patterns from /research

This skill reuses analysis patterns from the `/research` skill:
- SERP analysis workflow (Step 4-5 in /research)
- Competitor content extraction (Step 6 in /research)
- Gap identification methods (Step 7 in /research)

The key difference: `/research` builds from scratch for new content, while `/update-topic-gaps` compares existing content against current competitors.

---

## Quality Checklist

| Check | Requirement |
|-------|-------------|
| Keyword correct | Primary keyword matches article focus |
| Top 3 scraped | All 3 competitor structures extracted |
| Matrix complete | All topics from all sources compared |
| Gaps prioritized | Critical vs. significant vs. optional |
| Actionable | Each gap has clear recommendation |
| Scope estimated | Word count impact assessed |

---

## Limitations

- WebFetch may fail on some competitor sites (note which couldn't be scraped)
- Word counts are approximate
- SERP changes frequently; analysis is point-in-time
- Some "gaps" may be intentional editorial choices (note context)
