# Blog Pipeline

An AI-powered content creation pipeline built with Claude Code. Takes a keyword from research to publish-ready article in 9 automated steps.

## What It Does

This pipeline transforms keyword ideas into fully-drafted, cited, and formatted blog articles. Each step is a standalone Claude Code skill that can run independently or chain together.

**The 9-step pipeline:**

```
Keyword → Research → Reference → Outline → Annotate → Draft → Cite → Screenshots → Preview → Publish
```

| Step | Skill | What It Does |
|------|-------|--------------|
| 1 | `/research` | Gathers keyword metrics, analyzes top 3 competitors, identifies content gaps |
| 2 | `/ahrefs-reference` | Pulls existing Ahrefs blog articles as style/content reference |
| 3 | `/outline` | Creates structured outline with BLUF, H2/H3 hierarchy, evidence placeholders |
| 4 | `/ahrefs-mentions` | Annotates outline with natural product mentions |
| 5 | `/draft` | Expands outline into full article (~2,000-3,500 words) |
| 6 | `/verify-claims` | Finds sources for statistics and adds hyperlinks |
| 7 | `/generate-ahrefs-screenshot` | Generates Ahrefs app URLs for screenshot placeholders |
| 8 | `/preview` | Generates styled HTML preview |
| 9 | `/format-for-publish` | Applies WordPress shortcodes, exports to .docx |

## Quick Start

### Run the Full Pipeline

```bash
# Start Claude Code in the project directory
claude

# Run the full pipeline for a keyword
/blog-pipeline "your keyword here"

# With drafting context/direction
/blog-pipeline "content marketing" --context="Focus on B2B examples, data-driven angle"

# Or pick from your keyword ideas CSV
/blog-pipeline
```

### Run Individual Steps

```bash
# Research a keyword
/research "content marketing"

# Pull reference articles
/ahrefs-reference "content marketing"

# Create outline from research
/outline ./content-pipeline/1-research/content-marketing.md

# Add product mentions
/ahrefs-mentions ./content-pipeline/3-outlines/content-marketing.md

# Write the draft
/draft ./content-pipeline/4-outlines-annotated/content-marketing.md

# Add source citations
/verify-claims ./content-pipeline/5-drafts/content-marketing.md

# Generate screenshot URLs
/generate-ahrefs-screenshot ./content-pipeline/6-drafts-cited/content-marketing.md

# Generate HTML preview
/preview ./content-pipeline/6-drafts-cited/content-marketing.md

# Format for WordPress
/format-for-publish ./content-pipeline/6-drafts-cited/content-marketing.md
```

### Discover Keywords First

```bash
# Find content gaps vs competitors
/content-gap-analysis yourdomain.com

# Prioritize keywords by blog fit + business relevance
/keyword-prioritization
```

## Project Structure

```
blog_pipeline/
├── .claude/
│   └── skills/              # Skill definitions (one folder per skill)
├── templates/               # HTML preview template
├── keyword-ideas.csv        # Keyword backlog with metrics
│
├── content-pipeline/        # Content creation workflow (contents gitignored)
│   ├── 0-context/           # Drafting context from --context flag
│   ├── 1-research/          # Keyword research outputs
│   ├── 2-reference/         # Ahrefs blog references + shared style files
│   ├── 3-outlines/          # Article outlines
│   ├── 4-outlines-annotated/# Outlines with product mentions
│   ├── 5-drafts/            # First drafts
│   ├── 6-drafts-cited/      # Drafts with source citations
│   ├── 7-preview/           # HTML previews
│   ├── 8-publish/           # WordPress-ready .md and .docx
│   └── images/              # Screenshot outputs (gitignored)
│
└── update-pipeline/         # Content refresh workflow (contents gitignored)
    ├── 0-guidance/          # Update priorities
    ├── 1-extracted/         # Extracted article content
    ├── 2-update-claims/     # Outdated stats audit
    ├── 3-update-ahrefs-mentions/  # New features audit
    ├── 4-update-topic-gaps/ # Missing topics audit
    └── 5-update-preview/    # Diff preview HTML
```

## Setup

### Prerequisites

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- [Ahrefs API access](https://ahrefs.com/api) (for keyword research)
- [pandoc](https://pandoc.org/) for .docx export

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ryanahrefs/blog_pipeline.git
   cd blog_pipeline
   ```

2. **Install pandoc** (for Word document export)
   ```bash
   # macOS
   brew install pandoc

   # Ubuntu/Debian
   sudo apt-get install pandoc

   # Windows
   choco install pandoc
   ```

3. **Configure Ahrefs MCP**

   Create `.mcp.json` in the project root:
   ```json
   {
     "mcpServers": {
       "ahrefs": {
         "command": "npx",
         "args": ["-y", "@anthropic/ahrefs-mcp"],
         "env": {
           "AHREFS_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```

4. **Add a style reference** (optional but recommended)

   Save an example article that matches your target voice to `content-pipeline/2-reference/style-reference.md`. The `/draft` skill uses this to calibrate tone and style.

5. **Start Claude Code**
   ```bash
   claude
   ```

## Customization

### Adding Your Own Keywords

Edit `keyword-ideas.csv` to add keywords manually:

```csv
keyword,volume,traffic_potential,difficulty,cpc,priority,source,business_potential,ahrefs_product,rank,selected
my keyword,1000,2500,30,150,high,manual,2,Site Explorer,1,
```

Or use `/content-gap-analysis` to populate it automatically from competitor gaps.

### Modifying Skills

Each skill is defined in `.claude/skills/[skill-name]/SKILL.md`. Edit these files to:
- Change output formats
- Adjust writing guidelines
- Add new shortcodes
- Modify the research workflow

### Using the Context Parameter

Pass drafting guidance to influence the article's approach:

```bash
# Focus on specific audience
/blog-pipeline "keyword research" --context="Target audience is agency SEOs"

# Request specific angle
/blog-pipeline "link building" --context="Take a contrarian angle, emphasize quality over quantity"

# Specify examples to include
/blog-pipeline "seo tools" --context="Include more Ahrefs case studies, mention Brand Radar"
```

### Style Reference

The `/draft` skill reads `content-pipeline/2-reference/style-reference.md` to extract voice patterns. Replace this file with an article that matches your brand's writing style.

## Content Update Pipeline

Separate workflow for refreshing existing articles:

```bash
# Full update pipeline
/update-pipeline https://example.com/blog/article-to-update/

# Or run steps individually
/extract-content https://example.com/blog/article/
/update-guidance article-slug
/update-claims ./update-pipeline/1-extracted/article-slug.md
/update-ahrefs-mentions ./update-pipeline/1-extracted/article-slug.md
/update-topic-gaps ./update-pipeline/1-extracted/article-slug.md
/update-preview article-slug
```

## Skills Reference

| Skill | Purpose | Input |
|-------|---------|-------|
| `/blog-pipeline` | Run full pipeline | keyword, `--from=step`, `--context=` |
| `/research` | Keyword intelligence | keyword |
| `/ahrefs-reference` | Pull reference articles | keyword |
| `/outline` | Create structure | research file |
| `/ahrefs-mentions` | Add product mentions | outline file |
| `/draft` | Write full article | annotated outline |
| `/verify-claims` | Add source citations | draft file |
| `/generate-ahrefs-screenshot` | Generate screenshot URLs | cited draft |
| `/ahrefs-urls` | Construct Ahrefs URLs | report type |
| `/preview` | HTML preview | cited draft |
| `/format-for-publish` | WordPress + .docx | cited draft |
| `/content-gap-analysis` | Find keyword gaps | domain |
| `/keyword-prioritization` | Rate keyword fit | (uses CSV) |
| `/update-pipeline` | Full update flow | URL |
| `/extract-content` | Extract page content | URL |
| `/update-guidance` | Set update priorities | slug |
| `/update-claims` | Find outdated stats | extracted file |
| `/update-ahrefs-mentions` | Find new features | extracted file |
| `/update-topic-gaps` | Find missing topics | extracted file |
| `/update-preview` | Generate diff preview | slug |

## Example Output

Running `/blog-pipeline "reddit keyword research"` produces:

- **Research**: Comprehensive analysis with SERP data, competitor headers, content gaps
- **Outline**: Structured outline with 7 H2 sections, word count targets
- **Draft**: ~2,500 word article in first-person voice with 4 methods
- **Cited**: Source hyperlinks added, stats verified
- **Publish**: WordPress shortcodes applied, .docx ready for upload

## Tips

- **Resume a failed pipeline**: Use `--from=step` to pick up where you left off
  ```bash
  /blog-pipeline --from=draft "seo chrome extensions"
  ```

- **Pass context for better drafts**: Use `--context` to guide tone, angle, or examples

- **Preview while writing**: Run `/preview` on any draft to see it styled

- **Track selected keywords**: The `selected` column in the CSV prevents re-recommending keywords you've already written about

- **Batch keyword discovery**: Run `/content-gap-analysis` against multiple competitor domains to build a robust keyword backlog

## Requirements

- Claude Code CLI
- Ahrefs API key (for MCP integration)
- pandoc (for .docx export)
- Node.js 18+ (for MCP server)

## License

MIT
