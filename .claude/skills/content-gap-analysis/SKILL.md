---
name: content-gap-analysis
description: Find keyword opportunities by analyzing competitor content gaps
argument-hint: [your-domain]
allowed-tools: Read, Write, Bash, mcp__ahrefs__*
---

# Content Gap Analysis

> **Based on:** https://ahrefs.com/blog/content-gap-analysis/

Analyze **$ARGUMENTS** (your domain) to identify content gaps—keyword opportunities where competitors rank but you don't, revealing high-value topics to create content for.

**What you'll discover:**
- **Content gaps:** Topics competitors cover that you don't (new content needed)
- **Optimization opportunities:** Keywords competitors rank for on similar pages (improve existing content)
- **Traffic potential:** Estimated organic traffic you could capture by filling each gap

**Output:** High-priority keywords are saved to `keyword-ideas.csv` for the blog pipeline.

---

## Analysis Workflow

### 1. Identify Your Organic Competitors

Find competing websites that rank for similar keywords as your domain.

Call `mcp__ahrefs__site-explorer-organic-competitors` with:
- `target`: $ARGUMENTS (e.g., "example.com/")
- `mode`: "subdomains"
- `country`: User's target market (default "us" if not specified)
- `date`: Current date in YYYY-MM-DD format
- `select`: "domain,common_keywords,keywords_competitor,traffic,domain_rating"
- `order_by`: "common_keywords:desc"
- `limit`: 20

**Key insight:** `common_keywords` shows keyword overlap—higher numbers = more topically relevant competitors.

**Output:** Present a numbered list for user to select competitors:

**Your organic competitors (ranked by keyword overlap):**
1. [domain] ([common_keywords] common keywords, [traffic] traffic, DR [domain_rating])
2. [domain] ([common_keywords] common keywords, [traffic] traffic, DR [domain_rating])
3. [domain] ([common_keywords] common keywords, [traffic] traffic, DR [domain_rating])
...

**Selection criteria guidance:**
- ✅ **Good competitors:** High keyword overlap (500+), reasonable domain authority (DR 30-70), similar business model
- ⚠️ **Skip:** Mega-sites like Wikipedia, Reddit (unless directly competing), irrelevant industries

**Prompt user:** "Select 3-5 competitors to analyze (by number), or specify custom competitor domains."

**Wait for user's selection before proceeding.**

### 2. Pull Each Competitor's Top Pages

For each selected competitor (3-5 domains), identify their top-performing pages and the primary keywords driving traffic to each.

**For each competitor domain, call** `mcp__ahrefs__site-explorer-top-pages` with:
- `target`: Competitor domain (e.g., "competitor1.com/")
- `mode`: "subdomains"
- `country`: Same country as Step 1
- `date`: Current date in YYYY-MM-DD format
- `select`: "url,sum_traffic,keyword_top,keyword_top_volume,keyword_top_best_position,keywords"
- `order_by`: "sum_traffic:desc"
- `limit`: 50-100
- Optional `where` filter to exclude homepage/brand pages:
  ```json
  {
    "and": [
      {"field": "url", "is": ["ncontains", "/?"]},
      {"field": "keyword_top_volume", "is": ["gte", 50]}
    ]
  }
  ```

**Key fields:**
- `url` — Competitor's page URL
- `sum_traffic` — Estimated monthly organic traffic to that page
- `keyword_top` — The #1 keyword driving traffic to that page (**this is your gap candidate**)
- `keyword_top_volume` — Search volume of that keyword
- `keyword_top_best_position` — Competitor's ranking position
- `keywords` — Total keywords this page ranks for (indicates content depth)

**After collecting data from all competitors:**

Combine results into a single list and **deduplicate by `keyword_top`**:
- If multiple competitors have top pages targeting the same keyword → **stronger signal** (mark with count)
- If only one competitor targets it → still valid, but lower priority

**Expected output:** 150-500 candidate gap keywords from top competitor pages.

### 3. Check Which Keywords You Already Rank For

Determine whether your domain already ranks for the candidate gap keywords from Step 2.

Call `mcp__ahrefs__site-explorer-organic-keywords` with:
- `target`: $ARGUMENTS (your domain)
- `mode`: "subdomains"
- `country`: Same country as Steps 1-2
- `date`: Current date in YYYY-MM-DD format
- `select`: "keyword,best_position,best_position_url,volume,sum_traffic"
- `order_by`: "volume:desc"
- `limit`: 1000

**Cross-reference logic:**

For each candidate gap keyword from Step 2:
1. **You rank positions 1-10** → ❌ **ALREADY COMPETING** (exclude from report)
2. **You rank positions 11-50** → ⚠️ **OPTIMIZATION OPPORTUNITY** (medium priority)
3. **You don't rank at all (position > 100 or not found)** → ❓ **CANDIDATE GAP** (needs validation in Step 3.5)

**Important:** The API returns max 1,000 keywords, but large sites rank for 100K+. "Not found in API sample" ≠ "no content exists". Step 3.5 validates candidate gaps.

### 3.5 Validate Gap Keywords Against Existing Blog Content

Before enriching gap keywords, verify your domain doesn't already have dedicated articles for candidate gaps.

#### Load the Blog URL Index

Use the Screaming Frog export at `content-pipeline/2-reference/page_titles_all.csv` for fast local validation:

```bash
# Load the CSV (columns: Address, Title 1)
# Extract URL slugs and titles for matching
```

The CSV contains all blog URLs and their titles. Use this for instant lookups instead of slow site: searches.

#### Check for New Articles (Optional)

To catch articles published since the last crawl, fetch the sitemap:

```bash
curl -s https://ahrefs.com/blog/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' > /tmp/current_sitemap.txt
```

Compare against the CSV to identify new URLs not yet in the index.

#### Matching Logic

**For each candidate gap keyword**, check the local index:

1. **URL slug match:** Does any URL contain the keyword as a slug?
   - `keyword-clustering` → matches `/blog/keyword-clustering/`
   - `seo silo` → matches `/blog/seo-silo-structure/` (partial match OK)

2. **Title match:** Does any title contain the keyword phrase?
   - "types of seo" → matches "68 Types of SEO. Did We Miss Any?"

**Matching rules:**
- Convert keyword to lowercase, replace spaces with hyphens for URL matching
- Use case-insensitive substring match for titles
- Partial matches count (e.g., "keyword cluster" matches "keyword-clustering")

#### Classification

Based on match results + ranking data from Step 3:

| Match Found? | Ranking | Classification |
|--------------|---------|----------------|
| ✅ Yes | Top 10 | ❌ **EXISTING CONTENT** (exclude) |
| ✅ Yes | 11-100 | 🔄 **UPDATE OPPORTUNITY** |
| ❌ No | 11-50 | ⚠️ **OPTIMIZATION OPPORTUNITY** |
| ❌ No | Not ranking | ✅ **TRUE CONTENT GAP** |

**Example validation code:**

```bash
# Check if keyword exists in blog index
keyword="keyword clustering"
slug=$(echo "$keyword" | tr ' ' '-' | tr '[:upper:]' '[:lower:]')

# Search URL column
grep -i "$slug" content-pipeline/2-reference/page_titles_all.csv

# Search title column
grep -i "$keyword" content-pipeline/2-reference/page_titles_all.csv
```

This replaces dozens of slow site: searches with instant local lookups.

### 4. Enrich Gap Keywords with Traffic Potential

For the confirmed gap keywords (content gaps + optimization opportunities), pull detailed metrics.

**Batch the gap keywords** (up to 1,000 at a time) and call `mcp__ahrefs__keywords-explorer-overview` with:
- `keywords`: Comma-separated list of gap keywords
- `country`: Same country as previous steps
- `select`: "keyword,volume,traffic_potential,keyword_difficulty,cpc,is_informational,is_commercial,is_transactional"

**Key metrics for prioritization:**

| Metric | What It Means | Why It Matters |
|--------|---------------|----------------|
| `volume` | Monthly search volume | Direct demand indicator |
| `traffic_potential` | Est. total traffic top-ranking page gets | **REAL opportunity** |
| `keyword_difficulty` | Ranking difficulty score (0-100) | Feasibility indicator (lower = easier) |
| `cpc` | Cost per click (in USD cents, divide by 100) | Commercial value indicator |
| Intent flags | Informational, commercial, transactional | Content type guidance |

**Sort by:** `traffic_potential` descending (this is the primary opportunity metric)

### 5. Generate Prioritized Content Gap Report

Combine all data into a comprehensive, actionable content gap report.

**Prioritization logic:**

**🔴 HIGH PRIORITY (Create/optimize first)**
- Traffic potential: 500+ monthly visits
- Keyword difficulty: <40 (feasible)
- 2+ competitors ranking (validated opportunity)
- Gap type: Content gap OR optimization opportunity with position 21-50

**🟡 MEDIUM PRIORITY (Consider)**
- Traffic potential: 100-500 monthly visits
- Keyword difficulty: 40-60
- 1+ competitors ranking
- Gap type: Optimization opportunity with position 11-20 OR content gap with niche topic

**🟢 LOW PRIORITY (Monitor/defer)**
- Traffic potential: <100 monthly visits
- Keyword difficulty: >60 (very hard)
- 0-1 competitors ranking (weak signal)

**Optional scoring formula:**

```
Opportunity Score = (Traffic Potential × # Competitors Ranking) / (Keyword Difficulty + 1)
```

Higher score = higher priority.

---

## Saving Keywords to Pipeline

After completing the analysis, **save gap keywords with full metrics to the blog pipeline**.

### CSV Format

The `keyword-ideas.csv` file uses this structure:

```csv
keyword,volume,traffic_potential,difficulty,cpc,priority,source,business_potential,ahrefs_product,rank,selected
```

| Column | Description |
|--------|-------------|
| `keyword` | The gap keyword |
| `volume` | Monthly search volume |
| `traffic_potential` | Estimated traffic if ranking #1 |
| `difficulty` | Keyword difficulty (0-100) |
| `cpc` | Cost per click in cents (divide by 100 for USD) |
| `priority` | high / medium / low based on analysis |
| `source` | Where this keyword came from (content-gap-analysis, manual, etc.) |
| `business_potential` | 0-3 score (added by /keyword-prioritization) |
| `ahrefs_product` | Primary Ahrefs product fit (added by /keyword-prioritization) |
| `rank` | Priority rank (added by /keyword-prioritization) |
| `selected` | "yes" if keyword has been selected for research, empty otherwise |

### Append Gap Keywords

For each gap keyword identified, append a row with all metrics (leave business_potential, ahrefs_product, rank, and selected empty—these are populated by other skills):

```csv
reputation management companies,2200,47000,4,1200,high,content-gap-analysis,,,,
white label seo,5600,8100,39,1700,high,content-gap-analysis,,,,
mobile seo,4200,7500,21,50,high,content-gap-analysis,,,,
```

**Priority assignment:**
- **high**: Traffic potential 500+, KD <40, 2+ competitors ranking
- **medium**: Traffic potential 100-500, KD 40-60
- **low**: Traffic potential <100 or KD >60

### Summary Output

At the end of the analysis, show:

```
## Keywords Added to Pipeline

Added [N] keywords to keyword-ideas.csv:

| Keyword | Volume | TP | KD | Priority |
|---------|--------|-----|-----|----------|
| reputation management companies | 2,200 | 47,000 | 4 | high |
| white label seo | 5,600 | 8,100 | 39 | high |
| mobile seo | 4,200 | 7,500 | 21 | high |

To research and create content for these keywords:
/research "reputation management companies"
```

---

## Presentation Format

Present findings using this structure:

### Quick Summary
- Domain analyzed: [your domain]
- Competitors analyzed: [N] domains
- Total candidate keywords: [N]
- **Validated gaps:** [N] (after content check)
  - 🔴 High priority: [N]
  - 🟡 Medium priority: [N]
  - 🟢 Low priority: [N]
- True content gaps (new content needed): [N]
- Optimization opportunities (improve existing): [N]
- **Excluded:** [N] keywords (existing articles found)
- **Update opportunities:** [N] articles need refreshing

### High Priority Gaps

For each high-priority gap:

**[Number]. "[keyword]" ([traffic_potential] traffic potential)**

| Metric | Value |
|--------|-------|
| Gap Type | 🔴 Content gap / 🟡 Optimization opportunity |
| Traffic Potential | [traffic_potential] monthly visits |
| Search Volume | [volume] |
| Keyword Difficulty | [keyword_difficulty] (Easy/Medium/Hard) |
| CPC | $[cpc/100] |
| Intent | [intent type] |
| # Competitors | [N] competitors target this |

**Recommendation:** [CREATE NEW PAGE / OPTIMIZE EXISTING PAGE]

### Complete Gap Table

| Keyword | Gap Type | Traffic Potential | Volume | KD | # Comps | Priority |
|---------|----------|-------------------|--------|-----|---------|----------|
| [keyword] | Content gap | [N] | [N] | [N] | [N] | 🔴 High |
| ... | ... | ... | ... | ... | ... | ... |

---

### Excluded: Existing Content (Top 10)

Keywords where you already have articles ranking well—no action needed:

| Keyword | Blog URL | Position |
|---------|----------|----------|
| programmatic seo | /blog/programmatic-seo/ | 8 |
| ... | ... | ... |

*These were initially flagged as gaps due to API sampling limits, but validated against actual blog content.*

---

### Update Opportunities (Article Exists, Ranks Poorly)

Keywords where you have articles that need refreshing:

| Keyword | Blog URL | Current Position | Traffic Potential |
|---------|----------|------------------|-------------------|
| semantic seo | /blog/semantic-seo/ | 12 | 2,300 |
| ... | ... | ... | ... |

*Consider updating these articles to improve rankings. Feed into a content refresh workflow.*

---

## Common MCP Parameters

**Date format:**
- ✅ Correct: `"2026-02-17"` (YYYY-MM-DD)
- ❌ Wrong: `"today"`, `"latest"`, `"now"`

**Country codes:**
- ✅ Correct: `"us"`, `"gb"`, `"de"`, `"fr"`, `"ca"`, `"au"`
- ❌ Wrong: `"allGlobal"`, `"all"`, `"worldwide"`

**Target format:**
- ✅ Correct: `"example.com/"` (with trailing slash)

**Filter syntax (where parameter):**
```json
{"field":"column_name","is":["operator",value]}
{"and":[filter1,filter2]}
```

---

## Example Usage

```
/content-gap-analysis ahrefs.com
```

1. Finds organic competitors for ahrefs.com
2. User selects 3-5 competitors to analyze
3. Pulls top pages from each competitor
4. Identifies keywords you don't rank for
5. Enriches with traffic potential and difficulty
6. Generates prioritized report
7. **Saves high-priority keywords to keyword-ideas.csv**

---

## Troubleshooting

### Too Many Candidate Keywords (>1,000)

**Solution:**
1. Reduce number of competitors to 3-5 most relevant
2. Lower `limit` to 50 pages per competitor
3. Add `where` filter: `{"field": "keyword_top_volume", "is": ["gte", 100]}`

### No Competitors Found

**Solution:**
1. Check if domain has meaningful organic traffic
2. Try different country code
3. Manually specify competitor domains

### Keywords Explorer Timeout

**Solution:**
1. Batch keywords into groups of 500-1,000
2. Make multiple API calls for each batch

---

*This skill feeds into the blog pipeline. After running, use `/research` on the keywords added to keyword-ideas.csv.*
