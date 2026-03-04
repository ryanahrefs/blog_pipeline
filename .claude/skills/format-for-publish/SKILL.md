---
name: format-for-publish
description: Format a draft with WordPress shortcodes and export to .docx
argument-hint: [draft-file]
allowed-tools: Read, Write, Bash
---

# Format for Publish Skill

Transform a finished draft into a WordPress-ready document with Ahrefs shortcodes, then export to .docx format.

## Input

**Draft file path** - Path to a cited draft file (e.g., `./content-pipeline/6-drafts-cited/pinterest-seo.md`)

## Dependencies

**pandoc** is required for .docx export. Install via Homebrew:
```bash
brew install pandoc
```

If pandoc is not installed, the skill will save the formatted .md file and note that manual conversion is needed.

---

## WordPress Shortcodes Reference

### Content Structure

| Shortcode | Purpose | When to Use |
|-----------|---------|-------------|
| `[intro_text][/intro_text]` | Wraps the intro paragraph | First paragraph after the title |
| `[intro_toc]` | Auto-generates table of contents | After intro, before first H2 |
| `[post_nav_link]` | Section navigation anchor | Wraps each H2 heading |

### Callouts & Highlights

| Shortcode | Purpose | When to Use |
|-----------|---------|-------------|
| `[recommendation title="Tip"][/recommendation]` | Highlighted tip box | Actionable advice, tool recommendations |
| `[sidenote][/sidenote]` | Side note callout | Tangential but useful info |
| `[editor_note][/editor_note]` | Editor attribution | Editorial comments or updates |

### Quotes & Attribution

| Shortcode | Purpose | When to Use |
|-----------|---------|-------------|
| `[blockquote]` | Styled quote with author | Expert quotes, testimonials |

### Media & Widgets

| Shortcode | Purpose | When to Use |
|-----------|---------|-------------|
| `[caption][/caption]` | Image with caption | All images that need context |
| `[toolWidget]` | Ahrefs tool embed | When referencing Ahrefs free tools |

### End Matter

| Shortcode | Purpose | When to Use |
|-----------|---------|-------------|
| `[further_reading][/further_reading]` | Related articles list | End of article, 2-4 related posts |

---

## Shortcode Syntax

**Important:** Always use straight quotes (`"`) in shortcode attributes, never curly/smart quotes (`"` `"`).

### intro_text
```
[intro_text]First paragraph of the article that hooks the reader.[/intro_text]
```

### post_nav_link
```
[post_nav_link link_text="Section Title" section="section-slug"]

## Section Title

[/post_nav_link]
```

**Section slug rules:**
- Lowercase
- Hyphens instead of spaces
- No special characters
- Example: "What is YouTube SEO?" → `section="what-is-youtube-seo"`

### recommendation
```
[recommendation title="Tip"]

Your tip content here. Can include paragraphs, lists, and images.

![](https://example.com/image.jpg)

[/recommendation]
```

**Common titles:** "Tip", "Pro tip", "Don't sleep on...", "Important", "Note"

### sidenote
```
[sidenote]

Additional context that's useful but not essential to the main point.

[/sidenote]
```

### editor_note
```
[editor_note editor="Joshua Hardwick" editor_photo="https://ahrefs.com/blog/wp-content/uploads/2017/09/me.jpg" editor_job="Head of Content"]

Editor's commentary or update notice.

[/editor_note]
```

### blockquote
```
[blockquote size="small" author="John Mueller" author_photo="https://ahrefs.com/blog/wp-content/uploads/2022/02/john-mueller-google.png" author_job="Search Advocate," link_text="Google" link_url="https://www.google.com"]

_The quoted text goes here, typically in italics._

[/blockquote]
```

**Author photo URLs for common sources:**
- John Mueller: `https://ahrefs.com/blog/wp-content/uploads/2022/02/john-mueller-google.png`
- Ryan Law: `https://ahrefs.com/blog/wp-content/themes/Ahrefs-4/images/authors/main/RyanLaw.jpg`

### caption
```
[caption id="attachment_XXXXX" align="alignnone" width="1365"]![Alt text](https://ahrefs.com/blog/wp-content/uploads/YYYY/MM/image.png) Caption text describing the image.[/caption]
```

**Note:** Use placeholder ID `attachment_000000` - CMS will assign real ID on upload.

### toolWidget
```
[toolWidget tool="Keyword Generator" heading="Find thousands of keyword ideas in seconds"]
```

**Available tools:**
- `Website Traffic Checker` - "See search traffic estimates for any website or webpage"
- `Website Authority Checker` - "Check the authority of your domain"
- `Backlink Checker` - "Get a glimpse into the power of our premium tool"
- `Keyword Generator` - "Find thousands of keyword ideas in seconds"
- `Keyword Difficulty Checker` - "See how hard it will be to get into top 10 search results"

### further_reading
```
[further_reading]

- [Article Title 1](https://ahrefs.com/blog/slug-1/)
- [Article Title 2](https://ahrefs.com/blog/slug-2/)
- [Article Title 3](https://ahrefs.com/blog/slug-3/)

[/further_reading]
```

---

## Workflow

### Phase 1: Read and Analyze Draft

1. **Read the draft file** from the provided path
2. **Identify elements** that need shortcodes:
   - Intro paragraph (first paragraph after title)
   - All H2 headings (need post_nav_link)
   - Tips or recommendations (convert to [recommendation])
   - Expert quotes (convert to [blockquote])
   - Image placeholders (convert to [caption])
   - Ahrefs tool mentions (consider [toolWidget])

### Phase 2: Apply Shortcodes

Transform the content following these rules:

#### 1. Intro Section
```markdown
# Title

First paragraph...
```
Becomes:
```
# Title

[intro_text]First paragraph...[/intro_text]

Rest of intro...

[intro_toc]
```

#### 2. H2 Sections
```markdown
## What is YouTube SEO?

Content...
```
Becomes:
```
[post_nav_link link_text="What is YouTube SEO?" section="what-is-youtube-seo"]

## What is YouTube SEO?

[/post_nav_link]

Content...
```

#### 3. Tips and Recommendations
Look for patterns like:
- "Pro tip:" or "Tip:" prefixes
- Paragraphs starting with "You can use Ahrefs..."
- Callout-worthy advice

Convert to:
```
[recommendation title="Tip"]

The tip content...

[/recommendation]
```

#### 4. Expert Quotes
Look for blockquotes with attribution. Convert:
```markdown
> Quote text
> — John Mueller, Google
```
To:
```
[blockquote size="small" author="John Mueller" author_photo="URL" author_job="Search Advocate," link_text="Google" link_url="https://google.com"]

_Quote text_

[/blockquote]
```

#### 5. Images
Convert `[SCREENSHOT: description]` placeholders to:
```
[caption id="attachment_000000" align="alignnone" width="1365"]![Description](IMAGE_URL_PLACEHOLDER) Description of what the image shows.[/caption]
```

#### 6. Further Reading
Add at the end before the Twitter CTA:
```
[further_reading]

- [Related Article 1](https://ahrefs.com/blog/related-1/)
- [Related Article 2](https://ahrefs.com/blog/related-2/)
- [Related Article 3](https://ahrefs.com/blog/related-3/)

[/further_reading]
```

### Phase 3: Clean Up

1. **Remove metadata header** (Target Keyword, Word Count, Status, Style Card)
2. **Remove Draft Notes section** at the end
3. **Remove HTML comments** (`<!-- ... -->`)
4. **Ensure proper spacing** around shortcodes (blank lines before/after)
5. **Normalize quotes** - Replace curly/smart quotes with straight quotes:
   - `"` (U+201C) and `"` (U+201D) → `"` (straight double quote)
   - `'` (U+2018) and `'` (U+2019) → `'` (straight single quote)

   This is critical for WordPress shortcode attributes like `link_text="..."` and `title="..."`.

### Phase 4: Export to .docx

Use pandoc to convert the formatted markdown to .docx:

```bash
pandoc input.md -o output.docx --from markdown-smart --to docx
```

If pandoc is not installed, save as .md with a note that manual conversion is needed.

---

## Output

1. **Formatted markdown** saved to `content-pipeline/8-publish/[slug].md`
2. **Word document** saved to `content-pipeline/8-publish/[slug].docx`

---

## Example Transformation

### Before (draft excerpt):
```markdown
# YouTube SEO: How to Rank Your Videos in 2026

**Target Keyword**: youtube seo
**Status**: Sources Added

---

YouTube processes over 3 billion searches per month. That makes it the second-largest search engine in the world.

But here's the problem: over 500 hours of video get uploaded every minute.

## What is YouTube SEO?

YouTube SEO is the practice of optimizing your videos...

For a broader view of keyword opportunities, you can use Ahrefs' Keywords Explorer to check search volumes.

[SCREENSHOT: YouTube autocomplete suggestions]

---

## Draft Notes
...
```

### After (publish-ready):
```
# YouTube SEO: How to Rank Your Videos in 2026

[intro_text]YouTube processes over 3 billion searches per month. That makes it the second-largest search engine in the world.[/intro_text]

But here's the problem: over 500 hours of video get uploaded every minute.

[intro_toc]

[post_nav_link link_text="What is YouTube SEO?" section="what-is-youtube-seo"]

## What is YouTube SEO?

[/post_nav_link]

YouTube SEO is the practice of optimizing your videos...

[recommendation title="Tip"]

For a broader view of keyword opportunities, you can use Ahrefs' Keywords Explorer to check search volumes and see related video keywords.

[/recommendation]

[caption id="attachment_000000" align="alignnone" width="1365"]![YouTube autocomplete suggestions](IMAGE_URL_PLACEHOLDER) YouTube's search autocomplete showing keyword suggestions.[/caption]
```

---

## Further Reading Suggestions

When adding `[further_reading]`, select 2-4 related articles from the Ahrefs blog. Common related topics:

| Article Topic | Related Articles |
|---------------|------------------|
| YouTube SEO | Video SEO, Keyword Research, Content Marketing |
| Pinterest SEO | Social Media Marketing, Image SEO, Traffic Sources |
| Keyword Research | SEO Basics, Content Strategy, SERP Analysis |
| Link Building | Backlinks, Outreach, Content Promotion |

---

## Example Usage

```
/format-for-publish ./content-pipeline/6-drafts-cited/youtube-seo.md
```

Creates:
- `content-pipeline/8-publish/youtube-seo.md` (formatted with shortcodes)
- `content-pipeline/8-publish/youtube-seo.docx` (Word document)
