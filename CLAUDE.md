# Blog Pipeline

Content creation pipeline for blogging workflows. Each skill handles one step and can run independently or chained together.

## Skills

| Skill | Purpose |
|-------|---------|
| `/content-gap-analysis [domain]` | Find keyword opportunities from competitor gaps → saves to CSV |
| `/score-business-potential` | Score keywords by Ahrefs product relevance (0-3) |
| `/research [keyword]` | Gather keyword intelligence using Ahrefs MCP (or pick from CSV) |
| `/ahrefs-reference [keyword]` | Pull Ahrefs blog articles as reference material |
| `/outline [research-file]` | Create structured article outline |
| `/ahrefs-mentions [outline-file]` | Annotate outline with natural Ahrefs product mentions |
| `/draft [outline-file]` | Expand outline into full article draft |
| `/verify-claims [draft-file]` | Find sources for claims and add hyperlinks |
| `/preview [draft-file]` | Generate Ahrefs-styled HTML preview |
| `/format-for-publish [draft-file]` | Apply WordPress shortcodes and export to .docx |
| `/blog-pipeline [keyword]` | Run full pipeline from keyword to publish-ready article |

## Project Structure

```
blog_pipeline/
├── .claude/skills/        # Skill definitions
├── keyword-ideas.csv      # Keyword ideas with metrics, business_potential (0-3), selected status
├── 1-research/            # Step 1: Research outputs from /research
├── 2-outlines/            # Step 2: Outline outputs from /outline
├── 3-outlines-annotated/  # Step 3: Annotated outlines from /ahrefs-mentions
├── 4-drafts/              # Step 4: Draft outputs from /draft
├── 5-drafts-cited/        # Step 5: Cited drafts from /verify-claims
├── 6-preview/             # Step 6: HTML previews from /preview
├── 7-publish/             # Step 7: Publish-ready files from /format-for-publish
├── reference/             # Ahrefs blog reference articles from /ahrefs-reference
└── templates/             # HTML templates (ahrefs-preview.html)
```

## Ahrefs MCP Integration

The `/research` skill uses Ahrefs MCP for:
- Keyword metrics (volume, difficulty, CPC)
- Related/matching keywords
- SERP analysis
- Competitor content analysis

## Workflow Example

```bash
# Step 0: Find keyword ideas (populates keyword-ideas.csv)
/content-gap-analysis ahrefs.com

# Step 0.5: Score keywords by Ahrefs product fit (0-3)
/score-business-potential

# Full pipeline (research → publish)
/blog-pipeline "content marketing"

# Or step by step (specify keyword or pick from CSV)
/research                      # Pick from keyword-ideas.csv
/research "content marketing"  # Or specify directly
/outline ./1-research/content-marketing.md
/ahrefs-mentions ./2-outlines/content-marketing.md
/draft ./3-outlines-annotated/content-marketing.md
/verify-claims ./4-drafts/content-marketing.md
/preview ./5-drafts-cited/content-marketing.md
/format-for-publish ./5-drafts-cited/content-marketing.md
```

## Output File Naming

All outputs use kebab-case slugs derived from the keyword:
- "keyword research" → `keyword-research.md`
- "SEO best practices" → `seo-best-practices.md`

## Next Steps

### WordPress MCP Integration

Look into adding a WordPress MCP server to publish drafts automatically:

- [AutoWP MCP](https://github.com/Njengah/autowpmcp) - Publish posts from Claude to WordPress
- [wordpress-mcp](https://github.com/aaronsb/wordpress-mcp) - Role-based content management
- [AI Engine + MCP](https://meowapps.com/claude-wordpress-mcp/) - WordPress plugin with MCP endpoints

This would enable a `/publish` skill to:
- Create draft posts directly in WordPress
- Upload images and set featured images
- Apply categories and tags
- Schedule or publish posts
