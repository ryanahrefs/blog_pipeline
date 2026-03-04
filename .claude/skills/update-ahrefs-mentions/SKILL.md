---
name: update-ahrefs-mentions
description: Find opportunities to mention new Ahrefs product features not in the original article
argument-hint: [extracted-file]
allowed-tools: Read, Write, WebFetch
---

# Update Ahrefs Mentions Skill

Analyze an extracted article to identify opportunities to mention new Ahrefs product features that weren't available when the article was originally published.

## Input

**Extracted file path** - Path to the extracted article (e.g., `./update-pipeline/1-extracted/programmatic-seo.md`)

---

## Philosophy

Articles age not just because stats get outdated, but because **new tools and features launch** that could help readers accomplish their goals better. This skill identifies where new Ahrefs capabilities could be naturally woven into existing content.

**Key principles:**
- Only suggest features launched AFTER the article's Last Modified date
- Mentions should feel helpful, not promotional
- Focus on features that genuinely solve problems discussed in the article
- Aim for 1-3 new mentions max per article

---

## Workflow

### Phase 0: Check for Guidance

Before running the full audit:

1. **Extract the slug** from the input file path:
   - `./update-pipeline/1-extracted/programmatic-seo.md` → `programmatic-seo`

2. **Check for guidance file** at `./update-pipeline/0-guidance/[slug].md`

3. **If guidance exists:**
   - Read the priority level for `/update-ahrefs-mentions`
   - **PRIORITY**: Run full analysis - identify all relevant new features
   - **LOW**: Be conservative - only suggest obvious, high-impact feature mentions (1 max)
   - **SKIP**: Output minimal file:
     ```markdown
     # Ahrefs Mentions Audit: [Article Title]

     **Skipped per guidance** - User selected goals that don't require Ahrefs mentions audit.

     See `./update-pipeline/0-guidance/[slug].md` for context.
     ```
   - Include guidance summary in output header when running

4. **If no guidance file:** Run with default behavior (full analysis)

---

### Phase 1: Understand the Article

1. **Read the extracted file**

2. **Note key metadata:**
   - Published date
   - Last Modified date
   - Topic/keyword focus

3. **Identify article themes:**
   - What problems does this article help solve?
   - What tools/methods does it currently recommend?
   - What Ahrefs products are already mentioned?

4. **Create existing mentions inventory:**
   ```
   | Product | Location | How It's Used |
   |---------|----------|---------------|
   | Keywords Explorer | Section 3 | Finding keywords |
   | Site Explorer | Section 5 | Competitor analysis |
   ```

---

### Phase 2: Check for New Features

#### Step 1: Fetch Ahrefs Changelog

Use WebFetch to check the Ahrefs changelog for features released after the article's Last Modified date:

```
WebFetch: https://ahrefs.com/big-data
Prompt: List all major feature announcements and product launches since [Last Modified Date]. For each, note the feature name, what it does, and launch date.
```

Also check:
```
WebFetch: https://ahrefs.com/blog/category/product-updates/
Prompt: List product updates and new features announced since [Last Modified Date].
```

#### Step 2: Cross-Reference with Product List

Review the Ahrefs Product Reference (below) and identify:
- Products not mentioned in the article that could be relevant
- Features within mentioned products that are new
- Entirely new products launched since article publication

---

### Phase 3: Identify Natural Insertion Points

For each potential new feature mention:

1. **Find relevant sections** in the article where the feature would help
2. **Draft natural integration** - How would you mention it in context?
3. **Assess fit** - Does it genuinely add value or feel forced?

**Good insertion points:**
- When article describes a manual process the feature automates
- When article mentions a limitation the feature solves
- When article discusses a topic the feature directly addresses
- When article recommends a workaround the feature eliminates

**Skip if:**
- The mention would feel forced or off-topic
- The feature doesn't genuinely help with the article's purpose
- Adding it would require restructuring the article significantly

---

## Ahrefs Product Reference

Use this to match new features to article topics.

### Core Products

| Product | URL | Best For |
|---------|-----|----------|
| **Site Explorer** | ahrefs.com/site-explorer | Competitor analysis, backlink research, traffic analysis |
| **Keywords Explorer** | ahrefs.com/keywords-explorer | Keyword research, SERP analysis, keyword metrics |
| **Site Audit** | ahrefs.com/site-audit | Technical SEO, crawling issues, on-page SEO |
| **Rank Tracker** | ahrefs.com/rank-tracker | Ranking monitoring, SERP tracking, competitor comparison |
| **Content Explorer** | ahrefs.com/content-explorer | Content research, link prospecting, trending topics |

### Newer Products (Check if post-article)

| Product | URL | Launched | Best For |
|---------|-----|----------|----------|
| **Brand Radar** | ahrefs.com/brand-radar | 2024 | AI visibility tracking, LLM mentions, share of voice in AI |
| **Web Analytics** | ahrefs.com/web-analytics | 2023 | Privacy-friendly analytics, GA alternative |
| **AI Content Helper** | ahrefs.com/ai-content-helper | 2024 | Content grading, topical gap analysis, AI writing |
| **GBP Monitor** | ahrefs.com/gbp-monitor | 2024 | Local SEO, Google Business Profile tracking |
| **Reports Builder** | ahrefs.com/reports-builder | 2024 | Custom SEO reports, white-label reporting |

### Free Tools & Extensions

| Product | URL | Best For |
|---------|-----|----------|
| **Ahrefs Webmaster Tools** | ahrefs.com/webmaster-tools | Free site audits, backlink data for own sites |
| **Ahrefs SEO Toolbar** | ahrefs.com/seo-toolbar | SERP overlay, quick SEO checks while browsing |
| **Detailed SEO Extension** | detailed.com/extension | One-click on-page SEO analysis |

### Recent Feature Additions (Examples)

Check the changelog, but common recent additions include:

- **AI visibility metrics in Site Explorer** - Track mentions in ChatGPT, Gemini, Perplexity
- **Content grading in AI Content Helper** - Score content vs top-ranking pages
- **Share of Voice in Rank Tracker** - % of SERP clicks going to your pages
- **Cannibalization reports** - Find pages competing for same keywords
- **Historical SERP snapshots** - See how SERPs changed over time

---

## Output

Save to `./update-pipeline/3-update-ahrefs-mentions/[slug].md`:

```markdown
# Ahrefs Mentions Audit: [Article Title]

**Source**: ./update-pipeline/1-extracted/[slug].md
**Original URL**: [source URL]
**Audit Date**: [today]
**Last Modified**: [date]
**Article Age**: [X months]

---

## Current Ahrefs Mentions

Products/features already mentioned in the article:

| Product | Section | Context |
|---------|---------|---------|
| [product] | [section name] | [how it's used] |

---

## New Features Since Publication

Features launched after [Last Modified Date] that could be relevant:

| Feature | Product | Launch Date | Relevance |
|---------|---------|-------------|-----------|
| [feature] | [product] | [date] | [why relevant to article] |

---

## Recommended Additions

### 1. [Feature Name]

**Product:** [Product name]
**Launched:** [Date]

**Relevant section:**
> [Quote the section where this would fit]

**Why add:** [How this feature helps with what the article discusses]

**Suggested insertion:**
> "[Draft sentence showing natural integration]"

**Insertion type:** Tip / Example / Alternative method / New capability

---

### 2. [Feature Name]

**Product:** [Product name]
**Launched:** [Date]

**Relevant section:**
> [Quote]

**Why add:** [Explanation]

**Suggested insertion:**
> "[Draft sentence]"

---

## Features Considered But Not Recommended

| Feature | Reason Not Included |
|---------|---------------------|
| [feature] | [Not relevant to topic / Would feel forced / etc.] |

---

## Summary

| Metric | Count |
|--------|-------|
| Existing Ahrefs mentions | [N] |
| New features identified | [N] |
| Recommended additions | [N] |
| Features skipped | [N] |

**Overall assessment:** [Brief note on whether article needs significant updates or just minor additions]
```

---

## Example Usage

```
/update-ahrefs-mentions ./update-pipeline/1-extracted/programmatic-seo.md
```

**Output**: `./update-pipeline/3-update-ahrefs-mentions/programmatic-seo.md`

---

## Quality Guidelines

### Good Mention Example

**Article section:** "To track how your programmatic pages are performing..."

**Suggested addition:**
> "You can monitor rankings for all your programmatic pages at once using Ahrefs' Rank Tracker. Set up a project, import your target keywords, and track position changes across thousands of pages—seeing which templates are gaining or losing visibility."

**Why it works:** Directly solves a problem the article discusses.

### Bad Mention Example

**Article section:** "Programmatic SEO creates pages from database content..."

**Forced addition:**
> "By the way, Ahrefs also has a Content Explorer tool!"

**Why it fails:** Not relevant to the specific topic, feels promotional.

---

## Changelog Sources

Primary sources for new feature information:

1. **Big Data page**: https://ahrefs.com/big-data (major metrics/features)
2. **Product Updates blog**: https://ahrefs.com/blog/category/product-updates/
3. **Changelog** (if available): Check for dedicated changelog page
4. **Twitter/X**: @aaborsh, @aaborsh for announcements

---

## Limitations

- New features must be generally available (not beta/limited)
- Don't suggest features that require different subscription tiers without noting it
- If unsure about launch date, verify before recommending
