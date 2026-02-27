---
name: preview
description: Generate Ahrefs-styled HTML preview of a draft
argument-hint: [draft-file]
allowed-tools: Read, Write, Bash
---

# Preview Skill

Generate an Ahrefs blog-styled HTML preview from a markdown draft.

## Input

- `$ARGUMENTS`: Path to a markdown draft file (e.g., `./content-pipeline/6-drafts-cited/pinterest-seo.md`)

## Workflow

1. **Read the draft** from the provided path
2. **Extract the title** from the first H1 heading (`# Title`)
3. **Convert markdown to HTML**:
   - Headings: `# ` → `<h1>`, `## ` → `<h2>`, etc.
   - Paragraphs: Blank line separated text → `<p>` tags
   - Lists: `- ` items → `<ul><li>`, `1. ` items → `<ol><li>`
   - Bold: `**text**` → `<strong>`
   - Italic: `*text*` → `<em>`
   - Links: `[text](url)` → `<a href="url">text</a>`
   - Inline code: `` `code` `` → `<code>`
   - Code blocks: ``` → `<pre><code>`
   - Blockquotes: `> ` → `<blockquote>`
   - Images: `![alt](src)` → `<img src="src" alt="alt">`
4. **Read the template** from `templates/ahrefs-preview.html`
5. **Insert content** by replacing `{{TITLE}}` and `{{CONTENT}}` placeholders
6. **Derive output filename** from input (e.g., `pinterest-seo.md` → `pinterest-seo.html`)
7. **Write HTML** to `content-pipeline/7-preview/[slug].html`
8. **Open in browser**: Run `open content-pipeline/7-preview/[slug].html`

## Output

- HTML file at `content-pipeline/7-preview/[slug].html`
- Opens automatically in the default browser

## Example

```
/preview ./content-pipeline/6-drafts-cited/pinterest-seo.md
```

Creates `content-pipeline/7-preview/pinterest-seo.html` and opens it in the browser.
