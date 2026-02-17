---
name: ahrefs-reference
description: Search Ahrefs blog for reference articles on a keyword
argument-hint: [keyword]
allowed-tools: WebSearch, WebFetch, Write, Bash
---

# Ahrefs Reference Skill

Search the Ahrefs blog (ahrefs.com/blog) for articles relevant to a target keyword and compile their full content into a single reference document.

## Input

**Target keyword** - The topic to search for on Ahrefs blog (e.g., "keyword research", "link building")

---

## Workflow

### Step 1: Search Ahrefs Blog

Use WebSearch to find relevant articles on ahrefs.com/blog for the target keyword.

Search query: `site:ahrefs.com/blog [target keyword]`

**From the results, select up to 3 articles that are:**
- Directly relevant to the target keyword
- Educational/guide content (not news or updates)
- Comprehensive (prefer guides over short posts)

**Skip articles that are:**
- Product announcements or changelog posts
- Tangentially related topics
- Duplicate/overlapping content with another selected article

---

### Step 2: Extract Full Content

For each selected article (up to 3), use WebFetch to extract the complete content.

**Use this prompt for WebFetch:**
```
Extract the full article content in markdown format. Include:
1. The article title as H1
2. All H2 and H3 headers preserved
3. All body text paragraphs
4. Any numbered or bulleted lists
5. Key statistics or data points
6. Skip: navigation, ads, author bios, related posts, comments

Format the output as clean markdown that could be read as a standalone document.
```

**For each article, record:**
- Title
- URL
- Full content in markdown

---

### Step 3: Compile Reference Document

Combine all extracted articles into a single reference document.

**Document structure:**
- Header with keyword and date
- Table of contents linking to each article
- Each article separated by horizontal rules
- Source URLs preserved for attribution

---

## Output

Save to `./reference/[keyword-slug]-ahrefs.md`:

```markdown
# Ahrefs Reference: [Keyword]

**Generated**: [YYYY-MM-DD]
**Source**: ahrefs.com/blog
**Articles**: [N] articles compiled

---

## Table of Contents

1. [Article 1 Title](#article-1-title)
2. [Article 2 Title](#article-2-title)
3. [Article 3 Title](#article-3-title)

---

# Article 1 Title

**Source**: [URL]

[Full article content in markdown...]

---

# Article 2 Title

**Source**: [URL]

[Full article content in markdown...]

---

# Article 3 Title

**Source**: [URL]

[Full article content in markdown...]
```

---

## Example Usage

```
/ahrefs-reference "link building"
/ahrefs-reference "keyword research"
/ahrefs-reference "technical seo"
```

---

## Use Cases

- **Before writing**: Get Ahrefs' perspective on a topic as authoritative reference
- **During research**: Supplement keyword data with strategic content from Ahrefs experts
- **For outlines**: Use Ahrefs article structures as inspiration for your own content

---

## Troubleshooting

### No Results Found
- Try broader keyword (e.g., "SEO" instead of "programmatic SEO for SaaS")
- Check if Ahrefs has written about this topic
- Try related terms

### WebFetch Blocked
- Some pages may block scraping
- Note which articles couldn't be fetched
- Try alternative articles from search results

### Content Too Long
- If an article is extremely long, WebFetch may truncate
- Note truncation in the output
- Focus on extracting the most relevant sections
