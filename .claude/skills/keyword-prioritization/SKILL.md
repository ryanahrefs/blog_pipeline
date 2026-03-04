---
name: keyword-prioritization
description: Prioritize keywords by blog fit and Ahrefs product relevance
argument-hint: [keyword-ideas.csv or keyword]
allowed-tools: Read, Write, Edit
---

# Keyword Prioritization

Evaluate keywords for blog suitability and assign a Business Potential score (0-3) based on how essential Ahrefs products are to solving the problem.

## Input

- **No argument**: Score all unscored keywords in `keyword-ideas.csv`
- **CSV file path**: Score keywords in the specified CSV
- **Single keyword**: Score just that keyword and explain reasoning

---

## Blog Fit Filter

Before scoring Business Potential, first assess whether the keyword is appropriate for a **blog post** (vs. other page types).

| Blog Fit | Criteria | Examples |
|----------|----------|----------|
| **Yes** | Educational, informational, or how-to content. Searchers want to learn, understand, or solve a problem. | "what is keyword difficulty", "link building strategies", "how to do an seo audit" |
| **No** | Searchers want a tool, product, pricing, or direct action. Better served by a landing page, feature page, or interactive tool. | "free backlink checker", "seo tool", "ahrefs pricing", "keyword generator" |

### Keywords to Skip (Not Blog Fit)

- **Tool/generator queries**: "keyword generator", "backlink checker tool", "seo analyzer"
- **Product/brand queries**: "[brand] pricing", "[brand] vs [brand]", "[brand] alternative"
- **Feature queries**: "rank tracking software", "site audit tool"
- **Free tool queries**: "free keyword research tool", "free backlink checker"
- **Login/account queries**: "[brand] login", "create account"

These keywords should be marked `blog_fit: no` and typically skipped for blog content planning.

---

## Business Potential Rubric

| Score | Criteria | Example |
|-------|----------|---------|
| **3** | Ahrefs is an **irreplaceable solution** to the problem. The article fundamentally requires our tools to execute the advice. | "competitor backlink analysis", "keyword difficulty", "content gap analysis" |
| **2** | Ahrefs **helps quite a bit** but isn't essential. Other tools could work, but Ahrefs is a natural fit. | "link building strategies", "seo audit checklist", "keyword research" |
| **1** | Ahrefs can only be **mentioned fleetingly**. The topic is tangentially related to SEO/marketing. | "content marketing strategy", "social media tips", "email subject lines" |
| **0** | **No clear way** to mention Ahrefs. Topic is unrelated to our product capabilities. | "office productivity", "team management", "graphic design" |

---

## Ahrefs Product Capabilities Reference

Use this comprehensive list to evaluate how well Ahrefs can address each topic:

### Core SEO Analysis
- **Backlink analysis**: Checking backlinks, referring domains, anchor text, link velocity, lost/new links
- **Competitor research**: Analyzing competitor keywords, traffic, top pages, content gaps
- **Keyword research**: Finding keywords, search volume, difficulty, traffic potential, SERP analysis
- **Rank tracking**: Monitoring keyword positions, SERP features, share of voice
- **Site audits**: Technical SEO issues, crawl errors, on-page problems, Core Web Vitals
- **Content analysis**: Finding top-performing content, content gaps, topic research

### Specific Features by Product

**Site Explorer** (Score 3 for):
- Backlink checking, referring domains, anchor text analysis
- Competitor traffic analysis, top pages
- Organic keyword research for any domain
- Content gap analysis
- Paid search/PPC research

**Keywords Explorer** (Score 3 for):
- Keyword research, keyword ideas, search volume
- Keyword difficulty assessment
- SERP analysis, search intent
- Questions and topic clusters
- Click metrics, traffic potential

**Site Audit** (Score 3 for):
- Technical SEO audits
- Crawl error detection
- On-page SEO issues
- Internal linking analysis
- Site health monitoring

**Rank Tracker** (Score 3 for):
- Keyword position monitoring
- SERP feature tracking
- Competitor rank comparison
- Share of voice metrics
- Local rank tracking

**Content Explorer** (Score 3 for):
- Finding popular content by topic
- Content research and ideation
- Link prospecting
- Trending topics
- Author research

**Web Analytics** (Score 2-3 for):
- Website traffic analysis
- Referral source tracking
- User behavior metrics
- Conversion funnels

**Brand Radar** (Score 3 for):
- AI visibility tracking (ChatGPT, Gemini, Perplexity)
- Brand mention monitoring in LLMs
- Share of voice in AI responses
- GEO (Generative Engine Optimization)

**Social Media Manager** (Score 2-3 for):
- Social media scheduling and publishing
- Multi-platform posting (X/Twitter, Facebook, Instagram, LinkedIn, Bluesky)
- Social media analytics and performance tracking
- Content calendar management
- Social media strategy and planning

**Ahrefs SEO Toolbar** (Score 2 for):
- Quick SERP analysis
- On-page SEO checks
- Browser-based SEO metrics

**Detailed SEO Extension** (Score 2 for):
- On-page SEO audits
- Meta tag analysis
- Schema markup checking

**Free Tools / AWT** (Score 2 for):
- Basic backlink checking
- Simple keyword research
- Website health checks

---

## Scoring Guidelines

### Score 3 — Irreplaceable
The article topic **directly maps to a core Ahrefs feature**:
- "how to check competitor backlinks" → Site Explorer does exactly this
- "keyword difficulty explained" → Keywords Explorer is the go-to tool
- "content gap analysis" → Site Explorer's Content Gap feature
- "track keyword rankings" → Rank Tracker's core function
- "find broken backlinks" → Site Explorer broken backlinks report
- "AI brand visibility" → Brand Radar tracks this
- "best time to post on social media" → Social Media Manager provides this data

### Score 2 — Helps Quite a Bit
Ahrefs is **one of the best tools** for this, but the topic is broader:
- "seo audit checklist" → Site Audit helps, but article covers more than tool
- "link building strategies" → Site Explorer finds opportunities, but execution is manual
- "keyword research for beginners" → Keywords Explorer is great, but topic is educational
- "competitive analysis" → Multiple Ahrefs tools help, but isn't just about our tool
- "technical seo guide" → Site Audit relevant, but topic is comprehensive
- "social media scheduling tools" → Social Media Manager is a great fit, but topic is comparative

### Score 1 — Fleeting Mention
Topic is **tangentially related** to SEO/marketing:
- "content marketing trends" → Could mention Content Explorer briefly
- "instagram marketing tips" → Social Media Manager relevant but not core to topic
- "email marketing tips" → Limited SEO connection
- "conversion rate optimization" → Web Analytics somewhat relevant
- "marketing analytics" → Peripheral tool relevance

### Score 0 — No Mention
Topic has **no connection** to Ahrefs capabilities:
- "team productivity tools"
- "project management"
- "graphic design software"
- "accounting for small business"
- "HR best practices"

---

## Workflow

### For CSV Scoring

1. **Read keyword-ideas.csv**
2. **For each keyword without scores:**
   - **First, assess Blog Fit** — Is this a blog post topic or better as a tool/landing page?
   - If `blog_fit: no`, mark it and skip Business Potential scoring
   - If `blog_fit: yes`, proceed to score Business Potential (0-3)
   - Match against Ahrefs product capabilities
   - Note which Ahrefs product(s) are most relevant
3. **Update the CSV** with `blog_fit` and `business_potential` columns
4. **Rank all keywords** (see Ranking Step below) — only rank `blog_fit: yes` keywords
5. **Output summary** showing blog fit filter results and score distribution

### Ranking Step

After scoring all keywords, assign an overall `rank` (1 = highest priority) based on:

1. **Primary sort: Business Potential (descending)** — BP 3 keywords always rank above BP 2, etc.
2. **Secondary sort: Search Volume (descending)** — Within the same BP tier, higher volume = higher priority

**Ranking logic:**
```
Sort by: business_potential DESC, volume DESC
Assign rank: 1, 2, 3, ... in sorted order
```

**Example ranking:**

| Rank | Keyword | BP | Volume |
|------|---------|-----|--------|
| 1 | keyword gap | 3 | 1,300 |
| 2 | focus keywords | 3 | 1,000 |
| 3 | mobile seo | 2 | 4,200 |
| 4 | semantic seo | 2 | 3,300 |
| 5 | pinterest seo | 1 | 1,200 |

Keywords with missing volume data should be ranked last within their BP tier.

### For Single Keyword

1. **Assess Blog Fit first** — Is the searcher looking for educational content or a tool/product?
2. If **not blog-fit**: Explain why and suggest alternative page types
3. If **blog-fit**: Analyze the keyword and user intent
4. **Identify relevant Ahrefs products** (if any)
5. **Assign Business Potential score** with detailed reasoning
6. **Suggest how** Ahrefs could be mentioned (for scores 1-3)

---

## CSV Format

The skill expects and updates `keyword-ideas.csv` with this structure:

```csv
keyword,volume,traffic_potential,difficulty,cpc,priority,source,blog_fit,business_potential,ahrefs_product,rank
```

| Column | Description |
|--------|-------------|
| `blog_fit` | `yes` or `no` — Is this keyword appropriate for a blog post? |
| `business_potential` | Score 0-3 based on this rubric (only scored if blog_fit=yes) |
| `ahrefs_product` | Primary Ahrefs product relevant to this topic |
| `rank` | Overall priority ranking (1 = highest priority, sorted by BP then volume). Only blog_fit=yes keywords are ranked. |

---

## Output Format

### CSV Summary

```
## Keyword Scoring Complete

Evaluated [N] keywords in keyword-ideas.csv:

### Blog Fit Filter
- **Blog-appropriate:** [N] keywords
- **Not blog-appropriate:** [N] keywords (tool pages, landing pages, etc.)

Skipped for blog (examples): "free backlink checker", "seo tool pricing", ...

---

### Business Potential Scores (Blog-Fit Keywords Only)

| Score | Count | Keywords |
|-------|-------|----------|
| 3 | [N] | keyword gap, backlink analysis, ... |
| 2 | [N] | seo audit, link building, ... |
| 1 | [N] | content marketing, ... |
| 0 | [N] | ... |

**Average Business Potential:** [X.X]

---

## Priority Ranking (All Keywords)

Keywords ranked from highest to lowest priority (BP × Volume):

| Rank | Keyword | BP | Volume | Product |
|------|---------|-----|--------|---------|
| 1 | keyword gap | 3 | 1,300 | Site Explorer |
| 2 | focus keywords | 3 | 1,000 | Keywords Explorer |
| 3 | mobile seo | 2 | 4,200 | Site Audit |
| ... | ... | ... | ... | ... |

### Top 10 Recommendations
These keywords have the best combination of Business Potential and search demand:
1. **keyword gap** (BP 3, 1,300 vol) — Site Explorer
2. **focus keywords** (BP 3, 1,000 vol) — Keywords Explorer
...

### High-Value Keywords (Score 3)
These are ideal for Ahrefs blog content:
- keyword gap (Keywords Explorer)
- competitor backlinks (Site Explorer)
...
```

### Single Keyword

```
## Keyword Assessment: "keyword gap"

**Blog Fit:** Yes — Educational/how-to topic, searchers want to learn the concept

**Business Potential: 3** — Irreplaceable solution

**Reasoning:**
"Keyword gap" directly describes a core Ahrefs feature. Site Explorer's Content Gap
tool is specifically designed to find keywords competitors rank for that you don't.
This is exactly what searchers want when they search this term.

**Relevant Ahrefs Products:**
- Site Explorer → Content Gap report (primary)
- Keywords Explorer → Competitor keyword analysis

**Suggested Mention:**
"To find your keyword gaps, use Ahrefs' Content Gap tool in Site Explorer—paste
your domain and up to 10 competitors, and it shows keywords they rank for that
you're missing."
```

### Single Keyword (Not Blog Fit)

```
## Keyword Assessment: "free backlink checker"

**Blog Fit:** No — Tool/product query, searchers want to use a tool directly

**Recommendation:** Skip for blog content. This keyword is better served by:
- A dedicated tool landing page
- The free backlink checker tool page itself

**Note:** Could potentially write "How to Check Backlinks (Free & Paid Methods)"
to capture adjacent informational intent with blog content.
```

---

## Example Usage

```bash
# Prioritize all keywords in the default CSV
/keyword-prioritization

# Prioritize keywords in a specific file
/keyword-prioritization ./research/keyword-list.csv

# Evaluate a single keyword with explanation
/keyword-prioritization "technical seo audit"
```

---

## Priority Integration

Business Potential can inform content prioritization:

| Priority Formula |
|------------------|
| `Content Priority = Traffic Potential × Business Potential Score` |

Or factor into existing priority:
- **High priority + Score 3**: Publish ASAP (high traffic, perfect product fit)
- **High priority + Score 1-2**: Good traffic, may need creative product integration
- **Medium priority + Score 3**: Lower volume but great for brand/product content
- **Low priority + Score 0-1**: Deprioritize or skip

---

*This skill helps prioritize content that naturally showcases Ahrefs products while delivering value to readers.*
