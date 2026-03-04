# Blog Pipeline

Content creation pipeline for blogging workflows. Each skill handles one step and can run independently or chained together.

## Skills

| Skill | Purpose |
|-------|---------|
| `/content-gap-analysis [domain]` | Find keyword opportunities from competitor gaps → saves to CSV |
| `/keyword-prioritization` | Filter by blog fit + score by Ahrefs product relevance (0-3) |
| `/research [keyword]` | Gather keyword intelligence using Ahrefs MCP (or pick from CSV) |
| `/ahrefs-reference [keyword]` | Pull Ahrefs blog articles as reference material |
| `/outline [research-file]` | Create structured article outline |
| `/ahrefs-mentions [outline-file]` | Annotate outline with natural Ahrefs product mentions |
| `/draft [outline-file]` | Expand outline into full article draft |
| `/verify-claims [draft-file]` | Find sources for claims and add hyperlinks |
| `/generate-ahrefs-screenshot [draft-file]` | Generate Ahrefs URLs for `[SCREENSHOT: ...]` placeholders (manual capture) |
| `/preview [draft-file]` | Generate Ahrefs-styled HTML preview |
| `/format-for-publish [draft-file]` | Apply WordPress shortcodes and export to .docx |
| `/blog-pipeline [keyword]` | Run full pipeline from keyword to publish-ready article |

## Project Structure

```
blog_pipeline/
├── .claude/skills/           # Skill definitions
├── keyword-ideas.csv         # Keyword ideas with metrics, business_potential (0-3), selected status
├── templates/                # HTML templates (ahrefs-preview.html)
│
├── content-pipeline/         # New content creation workflow
│   ├── 1-research/           # /research outputs
│   ├── 2-reference/          # /ahrefs-reference outputs
│   │   └── page_titles_all.csv  # Screaming Frog export for gap validation
│   ├── 3-outlines/           # /outline outputs
│   ├── 4-outlines-annotated/ # /ahrefs-mentions outputs
│   ├── 5-drafts/             # /draft outputs
│   ├── 6-drafts-cited/       # /verify-claims outputs
│   ├── 7-preview/            # /preview outputs
│   ├── 8-publish/            # /format-for-publish outputs
│   └── images/{slug}/        # /generate-ahrefs-screenshot outputs (gitignored)
│
└── update-pipeline/          # Content refresh workflow
    ├── 1-extracted/              # /extract-content outputs
    ├── 2-update-claims/          # /update-claims outputs
    ├── 3-update-ahrefs-mentions/ # /update-ahrefs-mentions outputs
    ├── 4-update-topic-gaps/      # /update-topic-gaps outputs
    ├── 5-update-preview/         # /update-preview outputs (diff HTML)
    ├── 6-update-plan/            # (planned)
    ├── 7-updated-draft/          # (planned)
    └── 8-updated-final/          # (planned)
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
/keyword-prioritization

# Full pipeline (research → publish)
/blog-pipeline "content marketing"

# Or step by step (specify keyword or pick from CSV)
/research                      # Pick from keyword-ideas.csv
/research "content marketing"  # Or specify directly
/ahrefs-reference "content marketing"
/outline ./content-pipeline/1-research/content-marketing.md
/ahrefs-mentions ./content-pipeline/3-outlines/content-marketing.md
/draft ./content-pipeline/4-outlines-annotated/content-marketing.md
/verify-claims ./content-pipeline/5-drafts/content-marketing.md
/generate-ahrefs-screenshot ./content-pipeline/6-drafts-cited/content-marketing.md --target=ahrefs.com
/preview ./content-pipeline/6-drafts-cited/content-marketing.md
/format-for-publish ./content-pipeline/6-drafts-cited/content-marketing.md
```

## Output File Naming

All outputs use kebab-case slugs derived from the keyword:
- "keyword research" → `keyword-research.md`
- "SEO best practices" → `seo-best-practices.md`

## Content Update Pipeline

Separate workflow for refreshing existing articles rather than creating new ones.

### Update Skills

| Skill | Purpose |
|-------|---------|
| `/extract-content [url]` | Extract page content and metadata from a URL |
| `/update-guidance [slug]` | Set update priorities before running audits (optional) |
| `/update-claims [extracted-file]` | Find outdated stats/claims and update with newer references |
| `/update-ahrefs-mentions [extracted-file]` | Add mentions of new Ahrefs features launched since publication |
| `/update-topic-gaps [extracted-file]` | Compare against current SERP to find missing topics |
| `/update-preview [slug]` | Generate side-by-side diff preview with changes highlighted |
| `/update-pipeline [url]` | Run full update pipeline from URL to diff preview |
| `/update-plan` | *(planned)* Consolidate audits into actionable update plan |
| `/update-draft` | *(planned)* Revise content based on update plan |

### Update Directory Structure

```
update-pipeline/
├── 0-guidance/               # /update-guidance outputs (optional)
├── 1-extracted/              # Raw content extracted from URLs
├── 2-update-claims/          # Outdated stats/claims audit
├── 3-update-ahrefs-mentions/ # New Ahrefs features audit
├── 4-update-topic-gaps/      # Missing topics vs competitors
├── 5-update-preview/         # Preview of changes with diff
├── 6-update-plan/            # Consolidated update plan
├── 7-updated-draft/          # Revised content
└── 8-updated-final/          # Final content ready for publish
```

### Update Workflow Example

```bash
# Step 1: Extract current content
/extract-content https://ahrefs.com/blog/keyword-research/

# Step 2 (optional): Set update priorities
/update-guidance keyword-research
# → Asks: Primary goal? Scope? Structural changes?
# → Saves to: ./update-pipeline/0-guidance/keyword-research.md

# Step 3: Run audits (can run in parallel)
# Audits will read guidance file if it exists and adjust behavior
/update-claims ./update-pipeline/1-extracted/keyword-research.md
/update-ahrefs-mentions ./update-pipeline/1-extracted/keyword-research.md
/update-topic-gaps ./update-pipeline/1-extracted/keyword-research.md

# Step 4: Preview all changes with diff view
/update-preview keyword-research

# Outputs:
#   ./update-pipeline/0-guidance/keyword-research.md (if /update-guidance was run)
#   ./update-pipeline/2-update-claims/keyword-research.md
#   ./update-pipeline/3-update-ahrefs-mentions/keyword-research.md
#   ./update-pipeline/4-update-topic-gaps/keyword-research.md
#   ./update-pipeline/5-update-preview/keyword-research.html  ← Opens in browser

# Future steps:
# /update-plan [slug]  # Consolidate audits → 6-update-plan/
# /update-draft [slug] # Apply changes → 7-updated-draft/
```

---

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

### Project Ideas

Ideas to consider for future sessions:

- **`/existing-content` skill (planned).** Search existing Ahrefs blog for relevant content before outlining new articles. Plan: (1) Search `2-reference/page_titles_all.csv` using keyword/title matching (no vectorization needed for MVP), (2) Fetch top 3 articles via WebFetch, (3) Output analysis to `0-existing-content/` with coverage matrix, stances taken, gaps identified, and internal linking opportunities, (4) Update `/outline` to consume this analysis. Full plan saved at `.claude/plans/playful-jumping-puffin.md`.

- **Content updating module (in progress).** Building dedicated workflow for refreshing existing articles. Complete: `/extract-content`, `/update-claims`, `/update-ahrefs-mentions`, `/update-topic-gaps`, `/update-preview`. Remaining: `/update-plan` (consolidate audits), `/update-draft` (apply changes), `/update-pipeline` (full flow).

- **Deep research report for drafting.** Add a research-style report based on the outline to inform the drafting step. Might be overkill, but could improve depth.

- **AI citation optimization.** Add discrete steps to make parts of the article more citable (re: Patrick's comment on making content that AI systems want to reference).

- **Dedicated title brainstorming step.** Add a step at the end to generate and evaluate multiple title options.

- **In-line editing on draft previews.** Experimented with a Google Docs-style split-pane interface, but might be simpler to just edit markdown directly in VS Code with `<!-- EDIT: ... -->` comment tags that Claude can process.

- **Keep blog URL index updated.** The Screaming Frog export at `2-reference/page_titles_all.csv` is used for fast gap validation. To catch new articles, the skill can optionally fetch the sitemap and diff against the CSV. Consider re-crawling periodically or automating sitemap checks.

---

## Session Log

### 2026-02-27: Content Update Pipeline Built

Built four new skills for the content update workflow:

1. **`/update-claims`** - Two-phase LLM pipeline to extract factual claims from articles and verify which are outdated. Uses WebSearch to find current data and suggests replacements with sources. Categorizes claims as `PRODUCT_FEATURES`, `FACTS_STATS`, `TIME_SENSITIVE` and outputs as `UPDATE_STAT`, `REFRESH_SOURCE`, `CURRENT`, `FLAG`, or `REMOVE`.

2. **`/update-ahrefs-mentions`** - Identifies opportunities to mention new Ahrefs features launched since article publication. Compares article Last-Modified date against Ahrefs changelog/product updates. Includes full Ahrefs product reference (Site Explorer, Keywords Explorer, Site Audit, etc.).

3. **`/update-topic-gaps`** - Compares article against current SERP to find missing topics. Uses `mcp__ahrefs__serp-overview` and scrapes top 3 competitors via WebFetch. Builds topic coverage matrix and classifies gaps as `CRITICAL`, `SIGNIFICANT`, or `OPTIONAL`.

4. **`/update-preview`** - Generates side-by-side HTML diff preview showing original article alongside proposed changes with highlighting. Green for insertions, red strikethrough for deletions, yellow for modifications. Includes synchronized scrolling and change summary panel with Accept/Reject buttons.

**Tested on:** `programmatic-seo` article
- Found 5 changes: 4 stat updates (Nomadlist lost visibility, Zapier 4x growth, Webflow 14x growth, Wise 37x page expansion) + 1 URL refresh (twitter.com → x.com)
- Generated diff preview at `update-pipeline/5-update-preview/programmatic-seo.html`

**Folder restructuring:**
- Moved content creation folders into `content-pipeline/`
- Renamed `2-audit` → `2-update-claims` for clearer stage inspection
- Added `5-update-preview/` for diff HTML outputs
