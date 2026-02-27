# Blog Pipeline

An AI-powered content creation pipeline built with Claude Code. Takes a keyword from research to publish-ready article in 7 automated steps.

## What It Does

This pipeline transforms keyword ideas into fully-drafted, cited, and formatted blog articles. Each step is a standalone Claude Code skill that can run independently or chain together.

**The 7-step pipeline:**

```
Keyword → Research → Outline → Annotate → Draft → Cite → Preview → Publish
```

| Step | Skill | What It Does |
|------|-------|--------------|
| 1 | `/research` | Gathers keyword metrics, analyzes top 3 competitors, identifies content gaps |
| 2 | `/outline` | Creates structured outline with BLUF, H2/H3 hierarchy, evidence placeholders |
| 3 | `/ahrefs-mentions` | Annotates outline with natural product mentions |
| 4 | `/draft` | Expands outline into full article (~2,000-3,500 words) |
| 5 | `/verify-claims` | Finds sources for statistics and adds hyperlinks |
| 6 | `/preview` | Generates styled HTML preview |
| 7 | `/format-for-publish` | Applies WordPress shortcodes, exports to .docx |

## Quick Start

### Run the Full Pipeline

```bash
# Start Claude Code in the project directory
claude

# Run the full pipeline for a keyword
/blog-pipeline "your keyword here"

# Or pick from your keyword ideas CSV
/blog-pipeline
```

### Run Individual Steps

```bash
# Research a keyword
/research "content marketing"

# Create outline from research
/outline ./1-research/content-marketing.md

# Add product mentions
/ahrefs-mentions ./2-outlines/content-marketing.md

# Write the draft
/draft ./3-outlines-annotated/content-marketing.md

# Add source citations
/verify-claims ./4-drafts/content-marketing.md

# Generate HTML preview
/preview ./5-drafts-cited/content-marketing.md

# Format for WordPress
/format-for-publish ./5-drafts-cited/content-marketing.md
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
├── reference/               # Style reference articles
├── keyword-ideas.csv        # Keyword backlog with metrics
│
├── 1-research/              # Keyword research outputs
├── 2-outlines/              # Article outlines
├── 3-outlines-annotated/    # Outlines with product mentions
├── 4-drafts/                # First drafts
├── 5-drafts-cited/          # Drafts with source citations
├── 6-preview/               # HTML previews
└── 7-publish/               # WordPress-ready .md and .docx
```

## Setup

### Prerequisites

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- [Ahrefs API access](https://ahrefs.com/api) (for keyword research)
- [pandoc](https://pandoc.org/) for .docx export

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/blog_pipeline.git
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

   Save an example article that matches your target voice to `reference/style-reference.md`. The `/draft` skill uses this to calibrate tone and style.

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

### Style Reference

The `/draft` skill reads `reference/style-reference.md` to extract voice patterns. Replace this file with an article that matches your brand's writing style.

## Skills Reference

| Skill | Purpose | Input |
|-------|---------|-------|
| `/blog-pipeline` | Run full pipeline | keyword or `--from=step` |
| `/research` | Keyword intelligence | keyword |
| `/outline` | Create structure | research file |
| `/ahrefs-mentions` | Add product mentions | outline file |
| `/draft` | Write full article | annotated outline |
| `/verify-claims` | Add source citations | draft file |
| `/preview` | HTML preview | cited draft |
| `/format-for-publish` | WordPress + .docx | cited draft |
| `/content-gap-analysis` | Find keyword gaps | domain |
| `/keyword-prioritization` | Rate keyword fit | (uses CSV) |

## Example Output

Running `/blog-pipeline "seo chrome extensions"` produces:

- **Research**: 295-line analysis with SERP data, competitor headers, content gaps
- **Outline**: Structured outline with 7 H2 sections, word count targets
- **Draft**: ~3,100 word article in first-person voice
- **Cited**: 6 source hyperlinks added, stats verified
- **Publish**: WordPress shortcodes applied, .docx ready for upload

## Tips

- **Resume a failed pipeline**: Use `--from=step` to pick up where you left off
  ```bash
  /blog-pipeline --from=draft "seo chrome extensions"
  ```

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
