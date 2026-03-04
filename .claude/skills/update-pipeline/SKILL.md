---
name: update-pipeline
description: Run the full content update pipeline from URL to diff preview
argument-hint: [url or --from=step slug]
allowed-tools: Read, Write, Edit, Skill, Bash, WebFetch, WebSearch, AskUserQuestion, mcp__ahrefs__*
---

# Update Pipeline Skill

Orchestrate the full content update pipeline, running each skill in sequence from URL extraction to diff preview.

## Input

**Option A: Full pipeline from URL**
```
/update-pipeline https://ahrefs.com/blog/seo-chrome-extensions/
```
Runs all steps from extraction to preview.

**Option B: Resume from a specific step**
```
/update-pipeline --from=claims seo-chrome-extensions
```
Resumes pipeline from the specified step (useful if earlier steps are complete).

**Option C: Skip guidance step**
```
/update-pipeline --skip-guidance https://ahrefs.com/blog/seo-chrome-extensions/
```
Runs full pipeline but skips the interactive guidance questions (uses default behavior for all audits).

---

## Pipeline Steps

| Step | Skill | Input | Output Folder |
|------|-------|-------|---------------|
| 1 | `/extract-content` | URL | `update-pipeline/1-extracted/` |
| 2 | `/update-guidance` | slug | `update-pipeline/0-guidance/` |
| 3 | `/update-claims` | extracted file | `update-pipeline/2-update-claims/` |
| 4 | `/update-ahrefs-mentions` | extracted file | `update-pipeline/3-update-ahrefs-mentions/` |
| 5 | `/update-topic-gaps` | extracted file | `update-pipeline/4-update-topic-gaps/` |
| 6 | `/update-preview` | slug | `update-pipeline/5-update-preview/` |

---

## Step Details

### Step 1: Extract Content

Extract article content and metadata from the URL.

```
/extract-content [url]
```

**Input:** Ahrefs blog URL
**Output:** `./update-pipeline/1-extracted/[slug].md`

**What it does:**
- Fetch the page via WebFetch
- Extract article title, content, metadata
- Parse Last-Modified date
- Save as markdown for auditing

**Slug extraction:**
- URL: `https://ahrefs.com/blog/seo-chrome-extensions/`
- Slug: `seo-chrome-extensions`

---

### Step 2: Update Guidance (Interactive)

Gather user preferences for the update.

```
/update-guidance [slug]
```

**Input:** Slug from URL
**Output:** `./update-pipeline/0-guidance/[slug].md`

**What it does:**
- Ask 4 questions via AskUserQuestion:
  - Primary goal (Refresh stats / Add features / Fill gaps / Full refresh)
  - Target audience (Beginners / Intermediate / Experts)
  - Scope (Minimal / Moderate / Major / No limit)
  - Structural changes (Keep current / Allow new sections / Allow restructuring)
- Generate priority levels for each audit skill
- Save guidance for downstream skills to consume

**Can be skipped with:** `--skip-guidance` flag

---

### Step 3: Update Claims

Find outdated statistics and claims.

```
/update-claims ./update-pipeline/1-extracted/[slug].md
```

**Input:** Extracted file from Step 1
**Output:** `./update-pipeline/2-update-claims/[slug].md`

**What it does:**
- Extract all factual claims from article
- Search for current data
- Identify outdated stats with replacements
- Reads guidance file if present (adjusts thoroughness)

---

### Step 4: Update Ahrefs Mentions

Find opportunities to mention new Ahrefs features.

```
/update-ahrefs-mentions ./update-pipeline/1-extracted/[slug].md
```

**Input:** Extracted file from Step 1
**Output:** `./update-pipeline/3-update-ahrefs-mentions/[slug].md`

**What it does:**
- Check Ahrefs changelog for features since article publication
- Identify natural insertion points
- Draft contextual feature mentions
- Reads guidance file if present (adjusts thoroughness)

---

### Step 5: Update Topic Gaps

Compare against current SERP to find missing topics.

```
/update-topic-gaps ./update-pipeline/1-extracted/[slug].md
```

**Input:** Extracted file from Step 1
**Output:** `./update-pipeline/4-update-topic-gaps/[slug].md`

**What it does:**
- Pull current SERP for primary keyword
- Scrape top 3 competitor structures
- Build topic coverage matrix
- Identify critical, significant, and optional gaps
- Reads guidance file if present (adjusts recommendations)

---

### Step 6: Update Preview

Generate side-by-side diff preview.

```
/update-preview [slug]
```

**Input:** Slug (reads all audit outputs)
**Output:** `./update-pipeline/5-update-preview/[slug].html`

**What it does:**
- Consolidate findings from all audits
- Generate HTML diff preview
- Highlight changes (green=add, red=remove, yellow=modify)
- Open in browser for review

---

## Workflow Execution

When running the full pipeline:

1. **Parse URL** from arguments
2. **Extract slug** from URL path (e.g., `seo-chrome-extensions`)
3. **Run each step in sequence:**

```
Step 1: /extract-content "[url]"
   → Verify: ./update-pipeline/1-extracted/[slug].md exists

Step 2: /update-guidance [slug]
   → (Interactive: asks user 4 questions)
   → Verify: ./update-pipeline/0-guidance/[slug].md exists
   → (Skip if --skip-guidance flag)

Step 3: /update-claims ./update-pipeline/1-extracted/[slug].md
   → Verify: ./update-pipeline/2-update-claims/[slug].md exists

Step 4: /update-ahrefs-mentions ./update-pipeline/1-extracted/[slug].md
   → Verify: ./update-pipeline/3-update-ahrefs-mentions/[slug].md exists

Step 5: /update-topic-gaps ./update-pipeline/1-extracted/[slug].md
   → Verify: ./update-pipeline/4-update-topic-gaps/[slug].md exists

Step 6: /update-preview [slug]
   → Verify: ./update-pipeline/5-update-preview/[slug].html exists
   → Opens in browser
```

4. **Report completion** with all file locations

---

## Resume from Step

To resume from a specific step (if earlier outputs exist):

```
/update-pipeline --from=claims seo-chrome-extensions
```

Valid `--from` values:
- `extract` (Step 1 - default, full pipeline)
- `guidance` (Step 2)
- `claims` (Step 3)
- `ahrefs-mentions` (Step 4)
- `topic-gaps` (Step 5)
- `preview` (Step 6)

Before resuming, verify the required input file exists from the previous step.

---

## Output Summary

After a complete pipeline run:

```markdown
## Update Pipeline Complete: [slug]

**Source URL:** [url]
**Article:** [title]
**Last Modified:** [date] ([X months ago])

### Guidance Summary

| Setting | Selection |
|---------|-----------|
| Primary goal | [goal] |
| Scope | [scope] |

### Audit Results

| Audit | Findings |
|-------|----------|
| Claims | [N] updates, [N] current |
| Ahrefs Mentions | [N] recommended additions |
| Topic Gaps | [N] critical, [N] significant |

### Output Files

| Step | Output |
|------|--------|
| 1. Extracted | ./update-pipeline/1-extracted/[slug].md |
| 2. Guidance | ./update-pipeline/0-guidance/[slug].md |
| 3. Claims | ./update-pipeline/2-update-claims/[slug].md |
| 4. Ahrefs | ./update-pipeline/3-update-ahrefs-mentions/[slug].md |
| 5. Gaps | ./update-pipeline/4-update-topic-gaps/[slug].md |
| 6. Preview | ./update-pipeline/5-update-preview/[slug].html |

Preview opened in browser: ./update-pipeline/5-update-preview/[slug].html
```

---

## Error Handling

- **URL invalid:** Must be an ahrefs.com/blog URL (or other supported domain)
- **Step fails:** Stop pipeline, report error, preserve completed outputs
- **Missing input:** Check if previous step's output exists before proceeding
- **Guidance skipped:** Note in output that default audit behavior was used

Each step is independent—if the pipeline fails mid-way, you can fix the issue and resume from that step using `--from`.

---

## Example Usage

**Full pipeline from URL:**
```
/update-pipeline https://ahrefs.com/blog/seo-chrome-extensions/
```

**Skip interactive guidance:**
```
/update-pipeline --skip-guidance https://ahrefs.com/blog/keyword-research/
```

**Resume from claims step:**
```
/update-pipeline --from=claims seo-chrome-extensions
```

**Resume from preview only:**
```
/update-pipeline --from=preview programmatic-seo
```

---

## URL Patterns Supported

| Domain | Example URL | Slug Extraction |
|--------|-------------|-----------------|
| Ahrefs Blog | `https://ahrefs.com/blog/seo-chrome-extensions/` | `seo-chrome-extensions` |

The slug is extracted from the URL path, removing the domain and `/blog/` prefix.

---

## Pipeline Timing

Approximate time per step:
- Extract: ~10 seconds
- Guidance: ~30 seconds (interactive)
- Claims: ~2-5 minutes (searches for current data)
- Ahrefs Mentions: ~1-2 minutes (checks changelog)
- Topic Gaps: ~2-4 minutes (scrapes competitors)
- Preview: ~30 seconds

**Total:** ~7-12 minutes for full pipeline
