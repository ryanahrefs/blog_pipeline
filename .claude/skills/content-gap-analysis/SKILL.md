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

### 3. Check Against Existing Blog Content (Primary)

Use the Screaming Frog export to instantly check which candidate keywords already have dedicated articles. This is faster and more complete than API sampling.

#### Recommended CSV Columns

Export from Screaming Frog with these columns for best matching:

| Column | Purpose |
|--------|---------|
| `Address` | URL for slug matching |
| `Title 1` | Page title for keyword matching |
| `H1-1` | H1 heading (often more keyword-focused than title) |
| `Meta Description 1` | Additional keyword context |
| `Indexability` | Filter to indexable pages only |

**Current CSV location:** `content-pipeline/2-reference/page_titles_all.csv`

#### Smart Keyword Extraction from Titles

Titles are often clickbait-y. Extract the core topic by:

1. **Remove common patterns:**
   - Numbers: "67 Types of SEO" → "types of seo"
   - How-to prefixes: "How to Do Keyword Research" → "keyword research"
   - Suffixes: "... A Complete Guide", "... in 2024", "... (+ Examples)"
   - Questions: "What is SEO?" → "seo"

2. **Extraction examples:**

| Title | Extracted Topic |
|-------|-----------------|
| "How to Optimize Google My Business in 30 Minutes" | `google my business` |
| "67 Types of SEO: A Complete Guide" | `types of seo` |
| "What is Keyword Cannibalization? (And How to Fix It)" | `keyword cannibalization` |
| "Link Building for SEO: The Beginner's Guide" | `link building`, `link building for seo` |
| "SEO Competitor Analysis: How to Find & Spy on Your Rivals" | `seo competitor analysis` |

3. **Implementation:**

```python
import re

def extract_topic(title):
    """Extract core topic from blog title."""
    t = title.lower()

    # Remove trailing year/guide phrases
    t = re.sub(r'\s*[\(\[]?\s*(in )?\d{4}\s*[\)\]]?\s*$', '', t)
    t = re.sub(r'\s*[:\-–]\s*(a )?(complete |beginner.s |ultimate )?guide.*$', '', t, flags=re.I)
    t = re.sub(r'\s*[\(\[].*?[\)\]]\s*$', '', t)  # Remove trailing parentheticals

    # Remove leading patterns
    t = re.sub(r'^(how to |what is |what are |why |when )', '', t, flags=re.I)
    t = re.sub(r'^\d+\+?\s+', '', t)  # Leading numbers

    # Remove filler words
    t = re.sub(r'\s+(for seo|for beginners|you need to know|explained)$', '', t, flags=re.I)

    return t.strip()
```

#### Matching Logic

**For each candidate gap keyword**, check the local index:

1. **URL slug match** (strongest signal):
   ```
   keyword: "keyword clustering"
   slug: "keyword-clustering"
   matches: /blog/keyword-clustering/ ✅
   ```

2. **Extracted topic match** (checks H1 if available, then Title):
   ```
   keyword: "types of seo"
   title: "67 Types of SEO: A Complete Guide"
   extracted: "types of seo" ✅
   ```

3. **Partial/fuzzy match** (lower confidence):
   ```
   keyword: "seo audit"
   title: "How to Do an SEO Audit in 2024"
   partial match ✅ (flag for manual review)
   ```

**Matching rules:**
- Exact slug match → **HIGH confidence**
- Extracted topic match → **HIGH confidence**
- Keyword substring in title/H1 → **MEDIUM confidence**
- Partial word overlap (2+ words) → **LOW confidence** (flag for review)

#### Check for New Articles (Optional)

To catch articles published since the last SF crawl:

```bash
curl -s https://ahrefs.com/blog/sitemap.xml | grep -oP '(?<=<loc>)[^<]+' > /tmp/current_sitemap.txt
# Diff against CSV addresses to find new URLs
```

#### Initial Classification

| Match Result | Classification |
|--------------|----------------|
| ✅ High confidence match | ❓ **LIKELY COVERED** (verify ranking in Step 3.5) |
| ⚠️ Low confidence match | 🔍 **NEEDS REVIEW** (manual check) |
| ❌ No match found | ✅ **CANDIDATE GAP** (proceed to Step 3.5) |

### 3.5 Get Ranking Positions for Gaps (API)

For keywords NOT matched in the CSV (true gap candidates), check if you rank at all using the API.

Call `mcp__ahrefs__site-explorer-organic-keywords` with:
- `target`: $ARGUMENTS (your domain)
- `mode`: "subdomains"
- `country`: Same country as Steps 1-2
- `date`: Current date in YYYY-MM-DD format
- `select`: "keyword,best_position,best_position_url,volume,sum_traffic"
- `where`: Filter to only the candidate gap keywords if possible
- `order_by`: "volume:desc"
- `limit`: 1000

**Cross-reference the gap candidates:**

1. **You rank positions 1-10** → ❌ **ALREADY COMPETING** (CSV may be outdated, exclude)
2. **You rank positions 11-50** → ⚠️ **OPTIMIZATION OPPORTUNITY** (improve existing page)
3. **You don't rank (position > 100 or not found)** → ✅ **TRUE CONTENT GAP**

**For "LIKELY COVERED" keywords from Step 3:**

Also check their ranking positions to classify:

| CSV Match | API Ranking | Final Classification |
|-----------|-------------|----------------------|
| ✅ Match | Top 10 | ❌ **EXISTING CONTENT** (exclude) |
| ✅ Match | 11-100 | 🔄 **UPDATE OPPORTUNITY** |
| ✅ Match | Not ranking | 🔄 **UPDATE OPPORTUNITY** (content exists but not ranking) |
| ❌ No match | 11-50 | ⚠️ **OPTIMIZATION OPPORTUNITY** |
| ❌ No match | Not ranking | ✅ **TRUE CONTENT GAP** |

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
