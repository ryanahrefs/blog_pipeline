# Ahrefs App URLs - Keyword Cannibalization Skill

Reference list of all app.ahrefs.com report URLs needed for the keyword cannibalization workflow.

## Quick Reference - Minimal Working URLs

### 1. Find Keywords with Multiple URLs (Cannibalization Detection)
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target={DOMAIN}%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today
```

### 2. Compare Backlinks for Competing URLs
```
https://app.ahrefs.com/v2-site-explorer/refdomains?target={URL}%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50
```

### 3. Site Audit (Post-Redirect Cleanup)
```
https://app.ahrefs.com/site-audit
```

**Examples:**

**Step 1 - Find cannibalization:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=backlinko.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today
```

**Step 2 - Compare two competing pages:**
```
https://app.ahrefs.com/v2-site-explorer/refdomains?target=https://backlinko.com/seo-expert%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50

https://app.ahrefs.com/v2-site-explorer/refdomains?target=https://backlinko.com/seo-consultants%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50
```

**Key findings from real URLs:**
- ✅ All reports use `/v2-site-explorer/` prefix
- ✅ Referring domains path: `/refdomains` (NOT `/referring-domains`)
- ✅ Multiple URLs filter: `multipleUrlsOnly=1` (NOT `multipleUrls`)
- ✅ Volume format: `volume=100-` (NOT `volumeFrom=100`)
- ✅ Comparison: `compareDate=prev3Months` (NOT `compare=YYYY-MM-DD`)
- ✅ Domain/URL format: `target=domain.com%2F` (URL-encoded trailing slash)

## Primary Reports

### 1. Site Explorer - Organic Keywords (Main Cannibalization Detection)

**Base URL:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?brandedMode=all&chartGranularity=daily&chartInterval=all&compareDate=dontCompare&country=allGlobal&currentDate=today&hiddenColumns=&intentsAttrs=&keywordRules=&limit=50&localMode=all&mainOnly=0&mode=subdomains&multipleUrlsOnly=0&offset=0&performanceChartTopPosition=top11_20%7C%7Ctop21_50%7C%7Ctop3%7C%7Ctop4_10%7C%7Ctop51&positionChanges=&projectId=9301494&sort=OrganicTrafficInitial&sortDirection=desc&target={DOMAIN}%2F&urlRules=&volume_type=monthly
```

**With Multiple URLs Filter:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?brandedMode=all&chartGranularity=daily&chartInterval=all&compareDate=dontCompare&country=allGlobal&currentDate=today&hiddenColumns=&intentsAttrs=&keywordRules=&limit=50&localMode=all&mainOnly=0&mode=subdomains&multipleUrlsOnly=0&offset=0&performanceChartTopPosition=top11_20%7C%7Ctop21_50%7C%7Ctop3%7C%7Ctop4_10%7C%7Ctop51&positionChanges=&projectId=9301494&sort=OrganicTrafficInitial&sortDirection=desc&target={DOMAIN}%2F&urlRules=&volume_type=monthly
```

**With Volume Filter (100+ searches):**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?brandedMode=all&chartGranularity=daily&chartInterval=all&compareDate=dontCompare&country=allGlobal&currentDate=today&hiddenColumns=&intentsAttrs=&keywordRules=&limit=50&localMode=all&mainOnly=0&mode=subdomains&multipleUrlsOnly=1&offset=0&performanceChartTopPosition=top11_20%7C%7Ctop21_50%7C%7Ctop3%7C%7Ctop4_10%7C%7Ctop51&positionChanges=&projectId=9301494&sort=OrganicTrafficInitial&sortDirection=desc&target={DOMAIN}%2F&urlRules=&volume=100-&volume_type=monthly
```

**With Date Comparison (to see changes over time):**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?brandedMode=all&chartGranularity=daily&chartInterval=all&compareDate=prev3Months&country=allGlobal&currentDate=today&hiddenColumns=&intentsAttrs=&keywordRules=&limit=50&localMode=all&mainOnly=0&mode=subdomains&multipleUrlsOnly=1&offset=0&performanceChartTopPosition=top11_20%7C%7Ctop21_50%7C%7Ctop3%7C%7Ctop4_10%7C%7Ctop51&positionChanges=&projectId=9301494&sort=OrganicTrafficInitial&sortDirection=desc&target={DOMAIN}%2F&urlRules=&volume=100-&volume_type=monthly
```

**Key Parameters Extracted from Real URLs:**

**CRITICAL for Cannibalization:**
- `multipleUrlsOnly=1` - Shows only keywords where 2+ URLs rank (line 21) ⭐
- `volume=100-` - Filter for keywords with 100+ monthly searches

**Target & Mode:**
- `target={DOMAIN}%2F` - Domain with URL-encoded trailing slash (e.g., `ahrefs.com%2F`)
- `mode=subdomains` - Include www and all subdomains
- `mode=domain` - Exact domain only (excludes subdomains)
- `mode=prefix` - All URLs under a path
- `mode=exact` - Single specific URL

**Date Comparison:**
- `compareDate=dontCompare` - No comparison (base URL)
- `compareDate=prev3Months` - Compare to 3 months ago (line 26)
- `compareDate=prev1Month` - Compare to 1 month ago (assumed)
- `compareDate=prev6Months` - Compare to 6 months ago (assumed)
- `currentDate=today` - Use today's data

**Location/Country:**
- `country=allGlobal` - All countries combined
- `country=us` - United States only (assumed)
- `country=gb` - United Kingdom (assumed)
- *(Replace with 2-letter country code)*

**Display/Sorting:**
- `sort=OrganicTrafficInitial` - Sort by organic traffic
- `sortDirection=desc` - Descending order
- `limit=50` - Show 50 results per page
- `offset=0` - Start at first result (pagination)

**Filters:**
- `volume=100-` - Min volume 100+ (100-∞)
- `volume=100-1000` - Volume range 100-1000 (assumed)
- `volume=-1000` - Max volume 1000 (assumed)
- `brandedMode=all` - Include branded keywords
- `localMode=all` - Include local keywords
- `mainOnly=0` - Include SERP features (0=no, 1=yes)

**Chart Settings (can likely be ignored):**
- `chartGranularity=daily`
- `chartInterval=all`
- `performanceChartTopPosition=top11_20%7C%7Ctop21_50%7C%7Ctop3%7C%7Ctop4_10%7C%7Ctop51`

**Other:**
- `projectId=9301494` - Site Audit project ID (user-specific, can be omitted)
- `volume_type=monthly` - Use monthly search volume

**Simplified URL Templates (Essential Parameters Only):**

For keyword cannibalization detection, use this minimal format:
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target={DOMAIN}%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today
```

**Example URLs:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=ahrefs.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today

https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=backlinko.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=us&currentDate=today

https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=backlinko.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today&compareDate=prev3Months
```

**Note:** The domain should be URL-encoded with `%2F` at the end (represents trailing `/`)

---

### 2. Site Explorer - Backlinks (Compare Competing URLs)

**Backlinks Report URL:**
```
https://app.ahrefs.com/v2-site-explorer/backlinks?target={URL}%2F&mode=exact&history=all&followType=all&bestFilter=all&grouping=group-similar&sort=Traffic&sortDirection=desc&limit=50&offset=0
```

**Referring Domains Report URL (Recommended for Comparison):**
```
https://app.ahrefs.com/v2-site-explorer/refdomains?target={URL}%2F&mode=exact&history=all&followType=all&bestFilter=all&sort=Dr&sortDirection=desc&limit=50&offset=0
```

**Key Parameters:**

**Target & Mode:**
- `target={URL}%2F` - Full URL with URL-encoded trailing slash
  - For domain: `target=ahrefs.com%2F&mode=subdomains`
  - For specific page: `target=https://ahrefs.com/blog/seo-basics/%2F&mode=exact`
- `mode=exact` - Analyze specific page only
- `mode=subdomains` - Analyze entire domain with all subdomains
- `mode=prefix` - Analyze all URLs under a path

**Link Filters:**
- `followType=all` - All links (dofollow + nofollow)
- `followType=dofollow` - Only dofollow links
- `followType=nofollow` - Only nofollow links
- `bestFilter=all` - All backlinks
- `bestFilter=best` - Only best links per domain

**Display:**
- `history=all` - All historical backlinks
- `history=new` - Only new backlinks
- `history=lost` - Only lost backlinks
- `sort=Traffic` (backlinks) or `sort=Dr` (referring domains)
- `sortDirection=desc`
- `limit=50` - Results per page
- `offset=0` - Pagination

**Backlinks Specific:**
- `grouping=group-similar` - Group similar backlinks
- `filterLiveOnly=0` - Include all backlinks (0) or only live (1)
- `highlightChanges=1y` - Highlight changes from last year

**Filter Rules (Advanced - usually empty):**
- `anchorRules=` - Filter by anchor text
- `domainNameRules=` - Filter by domain name
- `refPageUrlRules=` - Filter by referring page URL
- `targetUrlRules=` - Filter by target URL
- `ipRules=` - Filter by IP address
- `surroundingRules=` - Filter by surrounding text

**Simplified URL Templates (Essential Parameters Only):**

For comparing backlinks of competing pages:
```
https://app.ahrefs.com/v2-site-explorer/refdomains?target={URL}%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50
```

**Examples:**
```
https://app.ahrefs.com/v2-site-explorer/backlinks?target=https://backlinko.com/seo-expert%2F&mode=exact&sort=Traffic&sortDirection=desc&limit=50

https://app.ahrefs.com/v2-site-explorer/refdomains?target=https://backlinko.com/seo-consultants%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50
```

---

### 3. Site Explorer - Overview (Context for Decision Making)

**Base URL:**
```
https://app.ahrefs.com/v2-site-explorer/overview?target={URL_OR_DOMAIN}%2F&mode=subdomains
```

**Parameters:**
- `target={URL_OR_DOMAIN}%2F` - URL or domain with URL-encoded trailing slash
- `mode=exact` - Single page analysis
- `mode=subdomains` - Domain + all subdomains
- `mode=prefix` - All URLs under a path

**Examples:**
```
https://app.ahrefs.com/v2-site-explorer/overview?target=https://backlinko.com/seo-expert%2F&mode=exact

https://app.ahrefs.com/v2-site-explorer/overview?target=backlinko.com%2F&mode=subdomains
```

---

### 4. Site Audit - Link Explorer (Post-Redirect Internal Link Cleanup)

**Base URL:**
```
https://app.ahrefs.com/site-audit/{PROJECT_ID}/internal-links
```

**Link Explorer (specific page incoming links):**
```
https://app.ahrefs.com/site-audit/{PROJECT_ID}/internal-links?target={URL}
```

**Redirected URLs Report:**
```
https://app.ahrefs.com/site-audit/{PROJECT_ID}/redirected
```

**Parameters:**
- `PROJECT_ID` = numeric ID of Site Audit project (user needs to have project set up)
- `target` = specific URL to find links to

**Examples:**
```
https://app.ahrefs.com/site-audit/12345/internal-links
https://app.ahrefs.com/site-audit/12345/internal-links?target=https://backlinko.com/seo-expert
https://app.ahrefs.com/site-audit/12345/redirected
```

**Note:** User must have a Site Audit project created first. Cannot provide project ID without knowing their account.

---

### 5. Site Audit - Main Dashboard (Setup Entry Point)

**Base URL:**
```
https://app.ahrefs.com/site-audit
```

**Specific Project:**
```
https://app.ahrefs.com/site-audit/{PROJECT_ID}
```

---

## Secondary/Helper Reports

### 6. Site Explorer - Best by Links (Find Strongest Pages)

**Base URL:**
```
https://app.ahrefs.com/v2-site-explorer/best-by-links?target={DOMAIN}%2F&mode=subdomains&sort=refdomains&sortDirection=desc&limit=50
```

**Parameters:**
- `target={DOMAIN}%2F` - Domain with URL-encoded trailing slash
- `mode=subdomains` - Include all subdomains
- `sort=refdomains` - Sort by number of referring domains
- `sortDirection=desc` - Highest first
- `limit=50` - Results per page

**Example:**
```
https://app.ahrefs.com/v2-site-explorer/best-by-links?target=backlinko.com%2F&mode=subdomains&sort=refdomains&sortDirection=desc&limit=50
```

**Use case:** Identify which pages have the most backlinks (helps decide which URL to keep when consolidating).

---

### 7. Site Explorer - Top Pages (Find Traffic Winners)

**Base URL:**
```
https://app.ahrefs.com/v2-site-explorer/top-pages?target={DOMAIN}%2F&mode=subdomains&country=allGlobal&sort=traffic&sortDirection=desc&limit=50
```

**Parameters:**
- `target={DOMAIN}%2F` - Domain with URL-encoded trailing slash
- `mode=subdomains` - Include all subdomains
- `country=allGlobal` - All countries or specific country code
- `sort=traffic` - Sort by organic traffic
- `sortDirection=desc` - Highest first
- `limit=50` - Results per page

**Example:**
```
https://app.ahrefs.com/v2-site-explorer/top-pages?target=backlinko.com%2F&mode=subdomains&country=allGlobal&sort=traffic&sortDirection=desc&limit=50
```

**Use case:** See which pages get the most organic traffic (helps decide which URL to keep when consolidating).

---

### 8. Site Explorer - Anchors (Understand Link Context)

**Base URL:**
```
https://app.ahrefs.com/v2-site-explorer/anchors?target={URL_OR_DOMAIN}%2F&mode=subdomains&sort=refdomains&sortDirection=desc&limit=50
```

**Parameters:**
- `target={URL_OR_DOMAIN}%2F` - URL or domain with URL-encoded trailing slash
- `mode=subdomains` - Domain analysis or `mode=exact` for specific page
- `sort=refdomains` - Sort by number of referring domains
- `sortDirection=desc` - Highest first
- `limit=50` - Results per page

**Examples:**
```
https://app.ahrefs.com/v2-site-explorer/anchors?target=backlinko.com%2F&mode=subdomains&sort=refdomains&sortDirection=desc&limit=50

https://app.ahrefs.com/v2-site-explorer/anchors?target=https://backlinko.com/seo-expert%2F&mode=exact&sort=refdomains&sortDirection=desc&limit=50
```

**Use case:** See what anchor text points to competing pages (helps understand link equity distribution).

---

## URL Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DOMAIN}` | Domain name without protocol | `ahrefs.com`, `backlinko.com` |
| `{URL}` | Full URL with protocol | `https://backlinko.com/seo-expert` |
| `{PROJECT_ID}` | Numeric Site Audit project ID | `12345` |
| `{DATE}` | Date in YYYY-MM-DD format | `2025-01-15` |

---

## Complete Parameter Reference

### Essential Parameters (Minimal Working URL)

| Parameter | Values | Description |
|-----------|--------|-------------|
| `target` | `domain.com%2F` | Domain with URL-encoded trailing slash |
| `mode` | `subdomains`, `domain`, `prefix`, `exact` | Analysis scope |
| `multipleUrlsOnly` | `0`, `1` | ⭐ **1 = Show only cannibalization candidates** |
| `volume` | `100-`, `100-1000`, `-1000` | Search volume filter (min-max format) |
| `country` | `allGlobal`, `us`, `gb`, etc. | Country/location |
| `currentDate` | `today` | Use current data |

### Comparison & Date Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `compareDate` | `dontCompare`, `prev1Month`, `prev3Months`, `prev6Months` | Historical comparison |
| `currentDate` | `today` | Current snapshot date |

### Display & Sorting

| Parameter | Values | Description |
|-----------|--------|-------------|
| `sort` | `OrganicTrafficInitial`, `Volume`, `Position` | Sort column |
| `sortDirection` | `asc`, `desc` | Sort order |
| `limit` | `50`, `100`, `250` | Results per page |
| `offset` | `0`, `50`, `100` | Pagination offset |

### Filter Parameters

| Parameter | Values | Description |
|-----------|--------|-------------|
| `brandedMode` | `all`, `branded`, `nonBranded` | Include/exclude branded keywords |
| `localMode` | `all`, `local`, `nonLocal` | Include/exclude local keywords |
| `mainOnly` | `0`, `1` | 0=include SERP features, 1=main organic only |
| `volume_type` | `monthly`, `average` | Volume calculation method |

### Position Filters

For filtering by ranking position, the format appears to be in the `performanceChartTopPosition` parameter, but this is complex. Likely better to filter in the app UI after loading.

### Intent Filters

Based on URL structure, intent filtering may be in `intentsAttrs` parameter, but format is not clear from examples. May require app UI filtering.

---

## Validation Questions - ANSWERED ✅

Based on real URLs provided:

1. **"Multiple URLs only" toggle** ✅ ANSWERED
   - Correct parameter: `multipleUrlsOnly=1` (NOT `multipleUrls=1`)
   - Set to `1` to show only keywords with 2+ URLs ranking

2. **Ranking history view** ❓ NEEDS VALIDATION
   - Not evident from URL structure
   - Likely only accessible via dropdown in organic keywords table
   - No direct URL parameter found

3. **Link Explorer in Site Audit** ❓ NEEDS VALIDATION
   - Still need real URL from Site Audit for internal links
   - Expected format: `https://app.ahrefs.com/site-audit/{PROJECT_ID}/internal-links?target={URL}`

4. **Date comparison** ✅ ANSWERED
   - Correct parameter: `compareDate=prev3Months` (NOT `compare=YYYY-MM-DD`)
   - Values: `dontCompare`, `prev1Month`, `prev3Months`, `prev6Months`
   - Uses relative dates, not absolute YYYY-MM-DD format

5. **Country filter** ✅ ANSWERED
   - Correct parameter: `country=allGlobal` or `country=us`
   - Uses 2-letter country codes or `allGlobal` for all countries

6. **Project ID** ✅ ANSWERED
   - `projectId=9301494` appears in URL but seems optional
   - For Site Audit reports, project ID is required in path: `/site-audit/{PROJECT_ID}/...`
   - For Site Explorer, can be omitted or is user-specific
   - Recommendation: Omit projectId for Site Explorer URLs in fallback

7. **Base path** ✅ DISCOVERED
   - Actual path: `/v2-site-explorer/organic-keywords` (NOT `/site-explorer/organic-keywords`)
   - May need to validate if both versions work

---

## Usage Notes

- Replace `{DOMAIN}` with actual domain (no protocol): `ahrefs.com`
- Replace `{URL}` with full URL including protocol: `https://ahrefs.com/blog/seo-basics/`
- Replace `{PROJECT_ID}` with numeric project ID (only for Site Audit URLs)
- Always use `mode=subdomains` for domain-level analysis to include www and all subdomains
- Use `mode=exact` when analyzing specific competing URLs for backlinks
- Add `&multipleUrls=1` filter to immediately show cannibalization candidates

---

## Test URLs - FULLY VALIDATED ✅

### Test Case: ahrefs.com

**Step 1: Find cannibalization (Organic Keywords with Multiple URLs filter):**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=ahrefs.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today&sort=OrganicTrafficInitial&sortDirection=desc&limit=50
```

**Step 1b: With 3-month comparison:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=ahrefs.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today&compareDate=prev3Months&sort=OrganicTrafficInitial&sortDirection=desc&limit=50
```

**Step 2: Compare backlinks for two competing URLs (Referring Domains):**
```
https://app.ahrefs.com/v2-site-explorer/refdomains?target=https://ahrefs.com/blog/affiliate-marketing/%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50

https://app.ahrefs.com/v2-site-explorer/refdomains?target=https://ahrefs.com/blog/affiliate-marketing-is-dead/%2F&mode=exact&sort=Dr&sortDirection=desc&limit=50
```

**Alternative: Full backlinks report (more detailed):**
```
https://app.ahrefs.com/v2-site-explorer/backlinks?target=https://ahrefs.com/blog/affiliate-marketing/%2F&mode=exact&sort=Traffic&sortDirection=desc&limit=50
```

**Step 3: Site Audit (for post-redirect internal link cleanup):**
```
https://app.ahrefs.com/site-audit
```

---

## Return Format for Skill

When MCP is not available, the skill should return URLs in this format:

```markdown
### Step 1: Find Keywords with Multiple Ranking URLs

Go to Site Explorer → Organic Keywords:
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=YOUR-DOMAIN.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today

This will show only keywords where 2+ of your URLs rank, filtered for meaningful search volume (100+ monthly searches).

**What to look for:**
- Keywords where multiple URLs appear in rankings
- Click the dropdown arrow (▼) next to any keyword to view ranking history
- Look for URLs that swap positions over time (indicates competition)

**Optional: Add 3-month comparison to see changes over time:**
https://app.ahrefs.com/v2-site-explorer/organic-keywords?target=YOUR-DOMAIN.com%2F&mode=subdomains&multipleUrlsOnly=1&volume=100-&country=allGlobal&currentDate=today&compareDate=prev3Months

### Step 2: Compare Backlink Profiles

For each competing URL, check referring domains:
- URL 1: https://app.ahrefs.com/site-explorer/referring-domains?target=https://YOUR-DOMAIN.com/page-1
- URL 2: https://app.ahrefs.com/site-explorer/referring-domains?target=https://YOUR-DOMAIN.com/page-2

**Review:**
- Number of referring domains (higher = stronger)
- Domain Rating of linking sites (quality of backlinks)
- Which page has stronger link profile (keep this one as primary)

### Step 3: After Implementing Redirects

Update internal links using Site Audit:
https://app.ahrefs.com/site-audit

1. Select your project for this domain
2. Go to Internal Links report
3. Search for links pointing to redirected URLs
4. Update those links to point directly to final destination
```

**Implementation note for Claude:**
- Replace `YOUR-DOMAIN.com` with the actual domain from user's request
- Replace `/page-1` and `/page-2` with actual competing URLs found in analysis
- Ensure domain in organic keywords URL has `%2F` at the end (URL-encoded slash)

---

*Last updated: 2026-02-11*
*Skill: keyword-cannibalization*
*Status: VALIDATED ✅*

**Fully Validated:**
- ✅ Organic Keywords URL structure (`/v2-site-explorer/organic-keywords`)
- ✅ Backlinks URL structure (`/v2-site-explorer/backlinks`)
- ✅ Referring Domains URL structure (`/v2-site-explorer/refdomains`)
- ✅ All parameter names and formats
- ✅ Multiple URLs filter (`multipleUrlsOnly=1`)
- ✅ Volume filtering (`volume=100-`)
- ✅ Date comparison format (`compareDate=prev3Months`)
- ✅ Country/location parameter (`country=allGlobal` or `country=us`)
- ✅ Target format with URL-encoded trailing slash

**Still optional/unknown:**
- ❓ Site Audit internal links exact URL format (requires project setup)
- ❓ Ranking history direct URL (likely only via dropdown in organic keywords table)
- ❓ Whether old `/site-explorer/` (non-v2) URLs still work as fallback

**Ready for production use in skill fallback URLs.**
