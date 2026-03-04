---
name: generate-ahrefs-screenshot
description: Generate Ahrefs URLs for screenshot placeholders in drafts
argument-hint: [draft-file] [--target=domain.com]
allowed-tools: Read, Write, Bash
---

# Generate Ahrefs Screenshot Skill

Parses `[SCREENSHOT: ...]` placeholders from drafts and generates Ahrefs URLs for manual screenshot capture.

## Input

**Required:**
- **Draft file path** - Path to the draft containing `[SCREENSHOT: ...]` placeholders

**Optional:**
- **--target=domain.com** - Default domain for Site Explorer reports (default: `ahrefs.com`)

---

## Workflow

### Phase 1: Parse Draft

1. **Read the draft file**
2. **Extract all `[SCREENSHOT: ...]` placeholders** with line numbers
3. **Classify each placeholder** based on keywords:

| Pattern in placeholder | Report Type | URL Template |
|------------------------|-------------|--------------|
| `Matching terms` | keywords-explorer-matching | KE matching terms |
| `Keywords Explorer` (overview/metrics) | keywords-explorer-overview | KE overview |
| `SERP Overview` or `SERP` | keywords-explorer-serp | KE SERP overview |
| `Parent Topic` | keywords-explorer-overview | KE overview (scroll to Parent Topic) |
| `Competing Domains` or `Organic Competitors` | organic-competitors | SE report |
| `Organic Keywords` | organic-keywords | SE report |
| `Top Pages` | top-pages | SE report |
| `Backlinks` (not `Broken`) | backlinks | SE report |
| `Referring Domains` | refdomains | SE report |
| `Broken Backlinks` | broken-backlinks | SE report |
| `Content Gap` | content-gap | Content Gap tool |
| `Rank Tracker` | rank-tracker | Requires project (manual) |
| `Site Audit` | site-audit | Requires project (manual) |
| External tools (Pinterest, YouTube, etc.) | external | Manual |

### Phase 2: Generate URLs

Build URLs using these patterns:

**Keywords Explorer:**
```
https://app.ahrefs.com/keywords-explorer/google/us/overview?keyword={keyword}
https://app.ahrefs.com/keywords-explorer/google/us/matching-terms?keyword={keyword}
https://app.ahrefs.com/keywords-explorer/google/us/serp-overview?keyword={keyword}
```

**Site Explorer:**
```
https://app.ahrefs.com/v2-site-explorer/{report}/subdomains?country=us&target={target}
```

**Content Gap:**
```
https://app.ahrefs.com/content-gap?targets[]={competitor1}&targets[]={competitor2}&intersection_targets[]={target}
```

### Phase 3: Create Output Directory

```bash
mkdir -p content-pipeline/images/{slug}
```

### Phase 4: Generate Report

Output a markdown report with:

1. **URL table** - Each placeholder with its URL and filename
2. **Instructions** - How to capture screenshots
3. **Image markdown** - Ready to paste into draft after capturing

---

## Output Format

```markdown
## Screenshots: {slug}

### URLs to Capture

| # | Placeholder | URL | Filename |
|---|-------------|-----|----------|
| 1 | Keywords Explorer > Matching terms | [Open](url) | screenshot-1-matching-terms.png |
| 2 | ... | ... | ... |

### Manual Screenshots Needed

| # | Placeholder | Reason |
|---|-------------|--------|
| 6 | Rank Tracker | Requires project setup |

---

## Capture Instructions

1. Open each URL in your browser (logged into Ahrefs)
2. Wait for data to load
3. Take screenshot: `Cmd+Shift+4` (Mac) or `Win+Shift+S` (Windows)
4. Save to: `content-pipeline/images/{slug}/`

---

## Paste into Draft

After capturing, replace placeholders with:

![Description](../images/{slug}/screenshot-1-matching-terms.png)
```

---

## Example Usage

```bash
/generate-ahrefs-screenshot ./content-pipeline/6-drafts-cited/competitor-keyword-analysis.md --target=ahrefs.com
```

---

## Filename Convention

Screenshots use this naming pattern:
```
screenshot-{index}-{report-type}.png
```

Examples:
- `screenshot-1-matching-terms.png`
- `screenshot-2-keywords-overview.png`
- `screenshot-3-organic-competitors.png`
