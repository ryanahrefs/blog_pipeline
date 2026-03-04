---
name: update-claims
description: Find outdated claims and statistics in an extracted article and update with newer references
argument-hint: [extracted-file]
allowed-tools: Read, Write, WebSearch, WebFetch
---

# Update Claims Skill

Two-phase pipeline to extract factual claims from an article, then verify which are outdated and need updating.

## Input

**Extracted file path** - Path to the extracted article (e.g., `./update-pipeline/1-extracted/programmatic-seo.md`)

---

## Pipeline

### Phase 0: Check for Guidance

Before running the full audit:

1. **Extract the slug** from the input file path:
   - `./update-pipeline/1-extracted/programmatic-seo.md` → `programmatic-seo`

2. **Check for guidance file** at `./update-pipeline/0-guidance/[slug].md`

3. **If guidance exists:**
   - Read the priority level for `/update-claims`
   - **PRIORITY**: Run full analysis (default behavior)
   - **LOW**: Be conservative - only extract claims that are clearly outdated (6+ months old stats, obviously wrong numbers)
   - **SKIP**: Output minimal file:
     ```markdown
     # Claims Audit: [Article Title]

     **Skipped per guidance** - User selected goals that don't require claims audit.

     See `./update-pipeline/0-guidance/[slug].md` for context.
     ```
   - Include guidance summary in output header when running

4. **If no guidance file:** Run with default behavior (full analysis)

---

### Phase 1: Claims Extraction

Act as a **fact-checking expert**. Read the article and extract ALL factual claims that could become outdated, categorized as:

#### Claim Types

| Type | What to Extract | Examples |
|------|-----------------|----------|
| `PRODUCT_FEATURES` | Product names, features, UI descriptions, pricing, capabilities | "Ahrefs' Site Audit checks for 170+ issues", "Keywords Explorer shows parent topic" |
| `FACTS_STATS` | Statistics, data points, research findings, percentages, numbers | "Pinterest has 450 million users", "97% of searches are unbranded" |
| `TIME_SENSITIVE` | Relative time references, "currently", "as of", explicit dates | "last year Google announced", "currently the best practice is", "as of 2023" |

#### Extraction Rules

1. **Extract exact text** - Copy 20-50 words verbatim from the article
2. **Include context** - Capture enough surrounding text to understand the claim
3. **Note what needs verification** - What specific fact should be checked?

#### Output Format (Phase 1)

```json
{
  "article_title": "...",
  "last_modified": "YYYY-MM-DD",
  "article_age_months": N,
  "claims": [
    {
      "id": 1,
      "type": "FACTS_STATS",
      "text": "exact quote from article (20-50 words)",
      "needs_check": "Pinterest user count - verify current figure"
    },
    {
      "id": 2,
      "type": "PRODUCT_FEATURES",
      "text": "exact quote from article",
      "needs_check": "Ahrefs Site Audit issue count - may have changed"
    },
    {
      "id": 3,
      "type": "TIME_SENSITIVE",
      "text": "exact quote with 'last year' or date reference",
      "needs_check": "Date reference is now N years old"
    }
  ]
}
```

---

### Phase 2: Claims Verification

Act as a **content fact-checker**. For each extracted claim, determine if it's outdated and suggest updates.

#### Context Provided

- Current date: [today's date]
- Article last modified: [date from metadata]
- Article age: [N months]
- Full article content (for exact text matching)
- Claims extracted in Phase 1

#### Verification Process

For each claim:

1. **Search for current data:**
   ```
   WebSearch: [claim keywords] [current year] statistics
   ```

2. **Verify with primary sources** (in priority order):
   - Official sources (company newsrooms, documentation)
   - Ahrefs blog (`site:ahrefs.com/blog [keywords]`)
   - Primary research (Statista, official studies)
   - Reputable industry (Moz, Search Engine Journal)

3. **Classify the finding:**

   | Finding | Type | Action |
   |---------|------|--------|
   | New data available | `UPDATE_STAT` | Replace number + add citation |
   | Same stat, newer source | `REFRESH_SOURCE` | Update citation only |
   | Still accurate | `CURRENT` | No change needed |
   | Cannot verify | `FLAG` | Mark for manual review |
   | Should be removed | `REMOVE` | Suggest deletion |

#### Output Format (Phase 2)

```json
{
  "suggestions": [
    {
      "claim_id": 1,
      "type": "UPDATE_STAT",
      "title": "Pinterest user count outdated",
      "original": "Pinterest has over 450 million monthly active users",
      "suggestion": "Pinterest has over 498 million monthly active users",
      "source_url": "https://newsroom.pinterest.com/...",
      "source_date": "2025-Q4",
      "reasoning": "Pinterest's Q4 2025 earnings report shows 498M MAU, up from 450M"
    },
    {
      "claim_id": 2,
      "type": "CURRENT",
      "title": "Site Audit issue count",
      "original": "Site Audit checks for 170+ issues",
      "suggestion": null,
      "reasoning": "Verified on ahrefs.com/site-audit - still states 170+ checks"
    },
    {
      "claim_id": 3,
      "type": "FLAG",
      "title": "Relative date reference",
      "original": "Last year, Google announced...",
      "suggestion": "In 2023, Google announced...",
      "reasoning": "Convert relative date to absolute date for evergreen content"
    }
  ]
}
```

#### Critical Rule: Exact Text Matching

**The `original` field must be copied character-for-character from the article content.**

- No paraphrasing
- No adding context words
- For table cells, copy only cell content without row headers
- Match whitespace and punctuation exactly

This enables automated find-and-replace during the update phase.

---

## Search Strategies by Claim Type

| Claim Type | Search Pattern |
|------------|----------------|
| User/market stats | `[platform] users [current year] statistics` |
| Study references | `[topic] study [2025-2026] research` |
| Platform features | `[platform] [feature] documentation` |
| Pricing | `[tool] pricing [current year]` |
| Best practices | `[topic] best practices Google [current year]` |

---

## Source Priority

1. **Official sources** - Company newsrooms, official blogs, documentation
2. **Ahrefs blog** - `site:ahrefs.com/blog [claim keywords]`
3. **Primary research** - Statista, official studies, quarterly reports
4. **Reputable industry** - Moz, Search Engine Journal, HubSpot

**Excluded competitors (never link):**
- semrush.com
- backlinko.com
- explodingtopics.com
- searchengineland.com

---

## Output

Save to `./update-pipeline/2-update-claims/[slug].md`:

```markdown
# Claims Audit: [Article Title]

**Source**: ./update-pipeline/1-extracted/[slug].md
**Original URL**: [source URL]
**Audit Date**: [today]
**Last Modified**: [date]
**Article Age**: [X months]

---

## Summary

| Category | Count |
|----------|-------|
| Total claims extracted | [N] |
| `UPDATE_STAT` | [N] |
| `REFRESH_SOURCE` | [N] |
| `CURRENT` | [N] |
| `FLAG` | [N] |
| `REMOVE` | [N] |

---

## Claims Requiring Updates

### 1. [Title from suggestion]

**Type:** `UPDATE_STAT`

**Original:**
```
[exact text from article - character-for-character match]
```

**Suggested replacement:**
```
[updated text with corrected stat]
```

**Source:** [source name]
**Source URL:** [url]
**Source Date:** [date]

**Reasoning:** [why this needs updating]

---

### 2. [Title]

**Type:** `REFRESH_SOURCE`

**Original:**
```
[exact text]
```

**Suggested replacement:**
```
[same text with updated/added citation]
```

**Source:** [source]
**Reasoning:** [explanation]

---

## Flagged for Manual Review

### [Title]

**Type:** `FLAG`

**Original:**
```
[exact text]
```

**Issue:** [why this couldn't be automatically verified]

**Suggestion:** [recommendation for manual review]

---

## Recommended Removals

### [Title]

**Type:** `REMOVE`

**Original:**
```
[exact text]
```

**Reasoning:** [why this should be deleted - e.g., stat no longer trackable, claim outdated with no replacement]

---

## Claims Verified as Current

| # | Claim Summary | Type | Verified Source |
|---|---------------|------|-----------------|
| 1 | [brief description] | `CURRENT` | [source] |
| 2 | [brief description] | `CURRENT` | [source] |

---

## Extracted Claims (Full List)

For reference, all claims identified in Phase 1:

| ID | Type | Needs Check | Status |
|----|------|-------------|--------|
| 1 | `FACTS_STATS` | Pinterest user count | `UPDATE_STAT` |
| 2 | `PRODUCT_FEATURES` | Site Audit issue count | `CURRENT` |
| 3 | `TIME_SENSITIVE` | Relative date reference | `FLAG` |
```

---

## Example Usage

```
/update-claims ./update-pipeline/1-extracted/programmatic-seo.md
```

**Output**: `./update-pipeline/2-update-claims/programmatic-seo.md`

---

## Age Thresholds

Article age influences verification priority:

| Article Age | Verification Level |
|-------------|-------------------|
| 0-6 months | Spot check `FACTS_STATS` only |
| 6-12 months | Verify all `FACTS_STATS` + `PRODUCT_FEATURES` |
| 12-24 months | Full audit, all claim types |
| 24+ months | Full audit, assume most claims outdated |

---

## Claims to Skip

Not everything needs verification. Skip:

- **Evergreen definitions** - "SEO stands for Search Engine Optimization"
- **Logical statements** - "More traffic generally means more revenue"
- **Historical facts** - "Google launched Panda in 2011" (intentionally dated)
- **Opinions** - "In my experience..." or "I recommend..."
- **Process descriptions** - "Click the export button to download"

---

## Quality Checklist

| Check | Requirement |
|-------|-------------|
| Exact text | `original` fields match article character-for-character |
| All types covered | `FACTS_STATS`, `PRODUCT_FEATURES`, `TIME_SENSITIVE` all checked |
| Sources verified | Each `UPDATE_STAT` has source URL and date |
| No competitors | Sources exclude semrush, backlinko, etc. |
| Actionable output | Suggestions can be directly applied via find/replace |
