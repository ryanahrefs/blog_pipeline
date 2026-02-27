---
name: ahrefs-mentions
description: Identify natural opportunities to mention Ahrefs products in an outline
argument-hint: [outline-file]
allowed-tools: Read, Write
---

# Ahrefs Mentions Skill

Analyze an article outline and identify opportunities to naturally mention Ahrefs products where they genuinely add value.

## Input

- `$ARGUMENTS`: Path to an outline file (e.g., `./content-pipeline/3-outlines/keyword-research.md`)

## Philosophy

As much as we aim to educate generally, we also showcase Ahrefs tools as part of the solution when it makes sense. **"Naturally" is key** – references to our products should feel helpful, not promotional.

When analyzing the outline, think about how Ahrefs (or a specific tool) can solve the problem or illustrate the concept being discussed. Then suggest mentioning it in-context, as a tip or an option.

### Good Examples

**In an article about analyzing website traffic:**
> "You can analyze your own AI traffic with Ahrefs Web Analytics – just connect your site and you'll be able to see referral traffic from AI chatbots in your dashboard."

**In an article about keyword research:**
> "Using Ahrefs' Keywords Explorer, you can quickly check the search volume and difficulty of these terms to prioritize your list."

### Guidelines

1. **Frame from the user's benefit perspective**: Not "Ahrefs is great at X," but "By using Ahrefs, _you_ can do X more effectively."

2. **Avoid over-plugging**: If an article mentions our tool every other sentence, it loses credibility. Aim for 1-3 natural mentions max depending on article length.

3. **Mention when it would be odd not to**: An Ahrefs guide to backlink analysis should mention Site Explorer. A keyword research guide should mention Keywords Explorer.

4. **Make it actionable**: Each mention should help readers accomplish something specific.

## Ahrefs Product Reference

Use this detailed reference to match products to outline topics. Understanding each product's full capabilities helps you make natural, specific mentions.

---

### Site Explorer

**URL**: https://ahrefs.com/site-explorer

**What it does**: The #1 competitor analysis tool. Analyze any website's backlink profile, organic search traffic, and paid advertising strategy.

**Key capabilities**:
- **Backlink analysis**: 493.9B backlinks indexed across 500.4M root domains. View referring domains, anchor text distribution, new/lost links over time
- **Organic traffic research**: See which keywords any site ranks for, estimated traffic per page, and traffic value
- **Top pages report**: Find competitor's best-performing content by traffic, backlinks, or social shares
- **Content gap analysis**: Discover keywords competitors rank for that you don't
- **Paid search analysis**: 37M ads tracked across 16.1M URLs—see competitor PPC keywords and ad copy
- **AI visibility metrics**: Track visibility in ChatGPT, Copilot, Gemini, and Perplexity responses

**Best for articles about**: Competitor analysis, backlink building, link prospecting, traffic analysis, content gap analysis, PPC research

**Example mention**: "To see who's linking to your competitors, paste their URL into Ahrefs' Site Explorer and check the Backlinks report—you can filter by dofollow links and sort by Domain Rating to find the most valuable opportunities."

---

### Keywords Explorer

**URL**: https://ahrefs.com/keywords-explorer

**What it does**: Find winning keyword ideas at scale with comprehensive keyword research and SERP analysis.

**Key capabilities**:
- **Massive keyword database**: 41.8B keywords indexed, 28.7B filtered; 10M new keywords discovered daily
- **190+ countries**: Localized search volume data for US (2.5B keywords), UK, Germany, France, Brazil, India, and more
- **Keyword metrics**: Search volume, keyword difficulty (KD), clicks, CPC, traffic potential, parent topic
- **SERP analysis**: See who ranks for any keyword, SERP features present, and historical ranking changes
- **Keyword ideas**: Matching terms, related terms, questions, also rank for, search suggestions
- **Click metrics**: Understand if keywords drive clicks or get answered in SERP features

**Best for articles about**: Keyword research, SEO strategy, content planning, search intent analysis, PPC keyword research

**Example mention**: "Using Ahrefs' Keywords Explorer, you can check the search volume, keyword difficulty, and traffic potential for thousands of keywords at once—then filter by KD under 30 to find low-competition opportunities."

---

### Site Audit

**URL**: https://ahrefs.com/site-audit

**What it does**: Crawl your website to find and fix technical SEO issues that hurt your rankings.

**Key capabilities**:
- **170+ SEO checks**: Detects technical and on-page issues across your entire site
- **Issue prioritization**: Categorizes problems as Errors (critical), Warnings (important), and Notices (minor)
- **Crawl analysis**: Find redirect chains/loops, broken links, orphan pages, duplicate content, thin content
- **On-page SEO**: Check title tags, meta descriptions, H1s, image alt text, structured data
- **Performance**: Page speed issues, large images, render-blocking resources
- **Always-on monitoring**: Continuous crawling to catch issues in real-time as they appear
- **JavaScript rendering**: Crawls JS-rendered content like Googlebot

**Best for articles about**: Technical SEO, site audits, fixing SEO issues, site migrations, Core Web Vitals, crawlability

**Example mention**: "Run your site through Ahrefs' Site Audit to scan for 170+ technical SEO issues—it'll prioritize what to fix first and show you exactly how to resolve each problem."

---

### Rank Tracker

**URL**: https://ahrefs.com/rank-tracker

**What it does**: Track keyword rankings across desktop and mobile in 190+ locations, and compare against competitors.

**Key capabilities**:
- **Global tracking**: Monitor rankings in 190+ countries, down to city/zip code level for local SEO
- **Desktop & mobile**: Separate tracking for each device type
- **Competitor comparison**: Track up to 10 competitors side-by-side for any keyword set
- **Share of Voice**: See what percentage of total search traffic goes to your pages vs. competitors
- **SERP features**: Tracks 12 different SERP feature types (featured snippets, PAA, local packs, etc.)
- **Visibility metrics**: Overall visibility score, average position, position distribution charts
- **Historical data**: Track ranking changes over time with visual graphs

**Best for articles about**: Rank tracking, SEO reporting, competitor monitoring, local SEO, SERP features

**Example mention**: "Set up Ahrefs' Rank Tracker to monitor your target keywords daily—you'll see ranking changes, track your share of voice against competitors, and get alerts when you win or lose SERP features."

---

### Content Explorer

**URL**: https://ahrefs.com/content-explorer

**What it does**: Search a database of over 1 billion web pages to find high-performing content on any topic.

**Key capabilities**:
- **Content discovery**: Search by keyword, topic, or domain to find popular content
- **Performance filters**: Filter by organic traffic, referring domains, social shares, word count, publish date
- **Link prospecting**: Find content with lots of backlinks in your niche for outreach targets
- **Trending content**: Filter to last 24 hours to find fresh, trending topics
- **Author research**: Find influential authors and their most shared content
- **Broken link building**: Find pages that used to get links but are now 404

**Best for articles about**: Content ideation, content research, link building, outreach, trending topics, content strategy

**Example mention**: "Use Ahrefs' Content Explorer to find content in your niche that's earned hundreds of backlinks—these are proven topics that attract links, and you can create something even better."

---

### Ahrefs Webmaster Tools (AWT)

**URL**: https://ahrefs.com/webmaster-tools

**What it does**: Free SEO tools for website owners—includes Site Audit, Site Explorer data, and Web Analytics for verified sites.

**Key capabilities**:
- **Free Site Audit**: Scan up to 5,000 pages per verified project for 170+ SEO issues
- **Backlink data**: See up to 1,000 backlinks with full filtering and sorting (no limits on total reported)
- **Organic keywords**: Unlimited organic keyword data for your verified sites
- **Web Analytics**: Free traffic analytics as a Google Analytics alternative
- **Unlimited projects**: Verify as many sites as you own at no cost

**Best for articles about**: Free SEO tools, beginner SEO, small business SEO, DIY website optimization

**Example mention**: "If you're just getting started with SEO, sign up for Ahrefs Webmaster Tools—it's completely free and gives you access to site audits, backlink data, and traffic analytics for your own sites."

---

### Alerts

**URL**: https://ahrefs.com/alerts

**What it does**: Get email notifications for new/lost backlinks, brand mentions, and new keyword rankings.

**Key capabilities**:
- **Backlink alerts**: Notified when any domain gains or loses backlinks—great for monitoring competitors
- **Mention alerts**: Track when your brand, product, or any keyword appears in new content online
- **New keyword alerts**: Get notified when a site starts ranking for new keywords
- **Customizable frequency**: Daily or weekly email digests
- **Competitor monitoring**: Set up alerts for competitor domains to track their link building activity

**Best for articles about**: Brand monitoring, competitor analysis, link building outreach, PR monitoring, reputation management

**Example mention**: "Set up an Ahrefs Alert for your brand name to get notified whenever someone mentions you online—these are perfect opportunities for link building outreach."

---

### AI Content Helper

**URL**: https://ahrefs.com/ai-content-helper

**What it does**: AI-powered writing assistant that grades your content against top-ranking pages and helps you fill topical gaps.

**Key capabilities**:
- **Content grading**: Scores your content against what's ranking in the top 10 for your target keyword
- **Topical gap analysis**: Shows topics covered by competitors that you're missing
- **Search intent detection**: Identifies multiple search intents for your keyword
- **In-line AI assistance**: Rephrase, summarize, or expand text with "Ask AI" feature
- **Built-in chat**: AI chat with access to your document and competitor articles for feedback
- **Outline generation**: Turn rough ideas into structured outlines
- **Free tier**: Available free with Ahrefs Webmaster Tools account

**Best for articles about**: Content writing, content optimization, SEO writing, content briefs, AI writing tools

**Example mention**: "Before publishing, run your draft through Ahrefs' AI Content Helper—it'll show you which topics the top-ranking pages cover that you might have missed."

---

### Web Analytics

**URL**: https://ahrefs.com/web-analytics

**What it does**: Simple, privacy-friendly Google Analytics alternative. Free, fast, and cookie-free.

**Key capabilities**:
- **Privacy-first**: No cookies required, no personal data collected, no consent banners needed
- **Core metrics**: Pageviews, visitors, traffic sources, top pages, locations, devices, browsers
- **Conversion funnels**: Track how visitors move through your site and where they drop off
- **Event tracking**: Monitor button clicks, form submissions, downloads
- **Real-time data**: See traffic as it happens
- **Free tier**: Up to 1 million events per project per month at no cost

**Best for articles about**: Website analytics, privacy-friendly analytics, traffic analysis, conversion tracking, Google Analytics alternatives

**Example mention**: "For a simpler alternative to Google Analytics, try Ahrefs Web Analytics—it's free, doesn't require cookie consent banners, and shows you exactly where your traffic comes from."

---

### Brand Radar

**URL**: https://ahrefs.com/brand-radar

**What it does**: Monitor your brand's visibility across AI platforms and track how often you appear in AI-generated answers.

**Platforms tracked**:
- **ChatGPT** (OpenAI)
- **Google AI Mode** (Search)
- **Google AI Overviews** (SGE)
- **Microsoft Copilot**
- **Gemini** (Google)
- **Perplexity**

**Key capabilities**:
- **AI mention tracking**: See how often your brand appears in AI-generated responses
- **Share of voice**: Compare your AI visibility against competitors
- **253M+ monthly prompts tracked**: Massive dataset of real questions asked to AI platforms
- **Custom query tracking**: Monitor specific prompts relevant to your brand ($0.02/query)
- **Citation tracking**: See which pages AI platforms cite when mentioning your brand
- **Topic analysis**: Understand what topics trigger mentions of your brand

**Best for articles about**: AI visibility, LLM optimization, brand monitoring, AI search, future of search, GEO (Generative Engine Optimization)

**Example mention**: "Use Ahrefs' Brand Radar to track how often your brand appears in ChatGPT, Gemini, Perplexity, and Google's AI Overviews—it tracks 250M+ real prompts monthly so you can see your actual AI visibility."

---

### Ahrefs SEO Toolbar

**URL**: https://ahrefs.com/seo-toolbar

**What it does**: Free Chrome/Firefox extension that shows Ahrefs SEO metrics directly in your browser and on Google search results.

**Key capabilities**:
- **SERP overlay**: See Domain Rating, URL Rating, backlinks, and traffic estimates for every result on Google
- **On-page SEO report**: Analyze any page's title, meta description, headings, word count, and more
- **Redirect tracer**: Track redirect chains and identify redirect issues
- **Outgoing links report**: See all links on a page, check for broken links, highlight nofollow/sponsored/UGC
- **HTTP headers**: View response headers for any page
- **Country changer**: Check Google results from different countries without VPN
- **Free to use**: No Ahrefs subscription required for basic features; premium data requires login

**Best for articles about**: Browser extensions, quick SEO checks, on-page analysis, SERP analysis, redirect tracking, competitive research while browsing

**Example mention**: "Install the free Ahrefs SEO Toolbar to see Domain Rating and backlink counts right in Google search results—it helps you quickly assess the competition for any keyword without leaving the SERP."

---

### Detailed SEO Extension

**URL**: https://detailed.com/extension/

**What it does**: Free Chrome/Firefox extension (by Ahrefs) for quick on-page SEO analysis of any webpage.

**Key capabilities**:
- **One-click SEO overview**: Instantly see title, meta description, canonical URL, robots directives, and structured data
- **Heading structure**: View the complete H1-H6 hierarchy to check content organization
- **Link analysis**: Count internal/external links, identify nofollow links
- **Image analysis**: Check for missing alt text across all images
- **Technical details**: View hreflang tags, Open Graph data, Twitter cards
- **Schema markup viewer**: See all structured data on a page in a readable format
- **Export functionality**: Copy all data for documentation or audits
- **100% free**: No account or subscription required

**Best for articles about**: On-page SEO audits, technical SEO checks, content audits, schema markup, meta tags, heading structure, SEO browser tools

**Example mention**: "For a quick on-page SEO check, use the free Detailed SEO Extension—click the icon on any page to instantly see its title tag, meta description, heading structure, and schema markup without opening any other tools."

---

### Additional Products

| Product | Description | Best for |
|---------|-------------|----------|
| **Reports Builder** | Create custom, white-labeled SEO reports for clients with drag-and-drop modules | Agency workflows, client reporting, SEO dashboards |
| **GBP Monitor** | Track Google Business Profile rankings, reviews, and local pack positions | Local SEO, multi-location businesses, review management |
| **Ahrefs API / MCP** | Programmatic access to Ahrefs data; MCP server for AI assistant integrations | Developers, AI workflows, custom tooling, automation |
| **Free SEO Tools** | Suite of free tools: backlink checker, keyword generator, SERP checker, website checker | Quick lookups, beginners, one-off research |

## Workflow

1. **Read the outline** from the provided path
2. **Analyze each section** for natural product mention opportunities:
   - What problem is this section solving?
   - Could an Ahrefs tool help readers accomplish this?
   - Would it feel natural or forced to mention it here?
3. **Annotate the outline** with `<!-- AHREFS: ... -->` comments suggesting:
   - Which product to mention
   - Where in the section (intro, example, tip)
   - A draft sentence showing natural integration
4. **Add a summary** at the top listing all suggested mentions
5. **Write the annotated outline** to `content-pipeline/4-outlines-annotated/[slug].md` (preserves original)

## Output Format

Add annotations like this:

```markdown
### How to find competitor backlinks

<!-- AHREFS: Site Explorer
Location: After explaining why competitor backlinks matter
Draft: "To see who's linking to your competitors, paste their URL into Ahrefs' Site Explorer and check the Backlinks report—you can filter by dofollow links and sort by Domain Rating to find the most valuable opportunities."
-->

Analyzing competitor backlinks reveals...
```

At the top of the file, add a summary:

```markdown
## Ahrefs Mention Opportunities

| Section | Product | Type |
|---------|---------|------|
| Finding competitor backlinks | Site Explorer | How-to tip |
| Checking keyword difficulty | Keywords Explorer | In-context example |

---
```

## Output

- Annotated outline saved to `content-pipeline/4-outlines-annotated/[slug].md`
- Original outline in `outlines/` remains unchanged

## Example

```
/ahrefs-mentions ./content-pipeline/3-outlines/link-building.md
```

Reads the outline, identifies 2-3 natural spots to mention relevant Ahrefs tools, and saves the annotated version to `content-pipeline/4-outlines-annotated/link-building.md`.
