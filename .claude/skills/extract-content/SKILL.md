---
name: extract-content
description: Extract HTML page content and metadata from a URL for content updating
argument-hint: [url]
allowed-tools: Read, Write, Bash
---

# Extract Content Skill

Fetch a URL and extract its content and metadata into a structured markdown file for content updating workflows.

## Input

- `$ARGUMENTS`: URL of the page to extract (e.g., `https://ahrefs.com/blog/keyword-research/`)

---

## Extraction Method

**For Ahrefs blog pages**: Use `curl` + Python parsing (WebFetch fails due to JS rendering)

```bash
# Fetch and extract using the extractor script
curl -s -L "$URL" > /tmp/page.html
python3 .claude/skills/extract-content/extractor.py "$URL" ./update-pipeline/1-extracted/
```

**For other sites**: WebFetch may work, but fall back to curl + Python if content is incomplete.

---

## What Gets Extracted

### Metadata

| Field | Source | Example |
|-------|--------|---------|
| Title | `<title>` tag | "Keyword Research: The Beginner's Guide" |
| Meta Description | `<meta name="description">` | "Learn how to find keywords..." |
| Canonical URL | `<link rel="canonical">` | `https://ahrefs.com/blog/keyword-research/` |
| Published Date | JSON-LD `datePublished` | 2024-03-15 |
| Modified Date | JSON-LD `dateModified` | 2025-01-10 |
| Author | Author link slug (Ahrefs) or schema | "Joshua Hardwick" |
| Word Count | Calculated from body content | 3,450 |

### Content Structure

| Element | Conversion |
|---------|------------|
| Headings | `<h2>` → `## `, `<h3>` → `### ` |
| Paragraphs | `<p>` → plain text with blank lines |
| Lists | `<ul>/<li>` → `- `, `<ol>/<li>` → `1. ` |
| Links | `<a href="url">text</a>` → `[text](url)` |
| Images | `<img>` → `![alt](src)` (lazy-load `data-src` supported) |
| Bold | `<strong>/<b>` → `**text**` |
| Italic | `<em>/<i>` → `*text*` |
| Blockquotes | `<blockquote>` → `> ` |

### Excluded Elements

- Navigation/header/footer
- Author bio blocks
- Table of contents
- Performance data widgets
- Sidebars and related posts
- Comments sections

---

## Workflow

### Step 1: Fetch the Page

```bash
curl -s -L "https://ahrefs.com/blog/programmatic-seo/" > /tmp/ahrefs-page.html
```

### Step 2: Run the Extractor

```bash
python3 .claude/skills/extract-content/extractor.py \
    "https://ahrefs.com/blog/programmatic-seo/" \
    ./update-pipeline/1-extracted/
```

The extractor script handles:
1. Metadata extraction (title, description, dates, author)
2. Content area identification (`entry-content` or `post-content` class)
3. HTML to markdown conversion
4. Structure outline generation
5. Statistics counting (words, links, images)

### Step 3: Verify Output

Check the generated file at `./update-pipeline/1-extracted/[slug].md`

---

## Output Format

Save to `./update-pipeline/1-extracted/[slug].md`:

```markdown
# [Title]

**Source URL**: [canonical URL]
**Extracted**: [today's date]
**Published**: [published date]
**Last Modified**: [modified date]
**Author**: [author name]
**Word Count**: [word count]
**Meta Description**: [description]

---

## Content

[Converted markdown content...]

---

## Extraction Notes

- **Images found**: [count] images (URLs preserved, not downloaded)
- **Internal links**: [count] links to ahrefs.com
- **External links**: [count] links to other domains
- **H2 sections**: [count]
- **H3 sections**: [count]

---

## Original Structure

- [H2: First Section]
  - [H3: Subsection]
  - [H3: Subsection]
- [H2: Second Section]
...
```

---

## Example Usage

```
/extract-content https://ahrefs.com/blog/programmatic-seo/
```

**Output**: `./update-pipeline/1-extracted/programmatic-seo.md`

---

## Slug Derivation

Slug is derived from the URL path:
- `https://ahrefs.com/blog/keyword-research/` → `keyword-research`
- `https://ahrefs.com/blog/seo-basics/` → `seo-basics`

---

## Error Handling

| Error | Action |
|-------|--------|
| 404 Not Found | Report error, do not create output |
| Empty content | Report "No article content detected" |
| Curl failure | Report network error |
| Incomplete extraction | Note in extraction notes |

---

## Files

- `SKILL.md` - This skill definition
- `extractor.py` - Python extraction script

---

## Limitations

- **Ahrefs blog only**: The extractor is tuned for Ahrefs blog HTML structure. Other sites may need adjustments.
- **No image download**: Image URLs are preserved but not downloaded.
- **Static content only**: Dynamic/JS-rendered content beyond initial page load is not captured.
