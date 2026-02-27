---
name: blog-pipeline
description: Run the full blog creation pipeline from keyword to publish-ready article
argument-hint: [keyword or step]
allowed-tools: Read, Write, Edit, Skill
---

# Blog Pipeline Skill

Orchestrate the full blog creation pipeline, running each skill in sequence from keyword research to publish-ready article.

## Input

**Option A: Full pipeline from keyword**
```
/blog-pipeline "content marketing"
```
Runs all steps from research to publish.

**Option B: Resume from a specific step**
```
/blog-pipeline --from=draft "content marketing"
```
Resumes pipeline from the specified step (useful if earlier steps are complete).

**Option C: Run without arguments**
```
/blog-pipeline
```
Shows available keywords from `keyword-ideas.csv` (same as `/research` with no args).

---

## Pipeline Steps

| Step | Skill | Input | Output Folder |
|------|-------|-------|---------------|
| 1 | `/research` | keyword | `content-pipeline/1-research/` |
| 2 | `/ahrefs-reference` | keyword | `content-pipeline/2-reference/` |
| 3 | `/outline` | research file | `content-pipeline/3-outlines/` |
| 4 | `/ahrefs-mentions` | outline file | `content-pipeline/4-outlines-annotated/` |
| 5 | `/draft` | annotated outline | `content-pipeline/5-drafts/` |
| 6 | `/verify-claims` | draft file | `content-pipeline/6-drafts-cited/` |
| 7 | `/preview` | cited draft | `content-pipeline/7-preview/` |
| 8 | `/format-for-publish` | cited draft | `content-pipeline/8-publish/` |

---

## Step Details

### Step 1: Research
Gather keyword intelligence and analyze top-ranking content.

```
/research [keyword]
```

**Input:** Keyword (from argument or selected from CSV)
**Output:** `./content-pipeline/1-research/[keyword-slug].md`

**What it does:**
- Get keyword metrics (volume, difficulty, traffic potential)
- Find long-tail variations with same parent topic
- Pull questions report
- Analyze SERP and top 3 ranking pages
- Identify content gaps and opportunities

---

### Step 2: Ahrefs Reference
Pull existing Ahrefs blog articles as style and content reference.

```
/ahrefs-reference [keyword]
```

**Input:** Keyword (same as Step 1)
**Output:** `./content-pipeline/2-reference/[keyword-slug]-ahrefs.md`

**What it does:**
- Search ahrefs.com/blog for related articles
- Extract full content from up to 3 relevant articles
- Compile into a reference document for voice/style calibration
- Provides examples of Ahrefs' editorial approach

---

### Step 3: Outline
Create a structured article outline based on research.

```
/outline ./content-pipeline/1-research/[keyword-slug].md
```

**Input:** Research file from Step 1 (also reads reference from Step 2)
**Output:** `./content-pipeline/3-outlines/[keyword-slug].md`

**What it does:**
- Create H2/H3 structure based on competitor analysis
- Include target keywords for each section
- Add content briefs with key points to cover
- Incorporate questions to answer

---

### Step 4: Ahrefs Mentions
Annotate outline with natural Ahrefs product mentions.

```
/ahrefs-mentions ./content-pipeline/3-outlines/[keyword-slug].md
```

**Input:** Outline file from Step 3
**Output:** `./content-pipeline/4-outlines-annotated/[keyword-slug].md`

**What it does:**
- Identify sections where Ahrefs tools add value
- Add contextual product mentions (not forced)
- Include specific feature recommendations
- Preserve original outline structure

---

### Step 5: Draft
Expand the annotated outline into a full article.

```
/draft ./content-pipeline/4-outlines-annotated/[keyword-slug].md
```

**Input:** Annotated outline from Step 4 (also reads reference from Step 2)
**Output:** `./content-pipeline/5-drafts/[keyword-slug].md`

**What it does:**
- Write full prose for each section
- Follow Ahrefs blog voice and style
- Include examples and explanations
- Add transitional content between sections

---

### Step 6: Verify Claims
Find and add source links to factual claims.

```
/verify-claims ./content-pipeline/5-drafts/[keyword-slug].md
```

**Input:** Draft file from Step 5
**Output:** `./content-pipeline/6-drafts-cited/[keyword-slug].md`

**What it does:**
- Identify factual claims needing sources
- Search for authoritative sources
- Add hyperlinks to claims
- Flag claims that couldn't be verified

---

### Step 7: Preview
Generate an Ahrefs-styled HTML preview.

```
/preview ./content-pipeline/6-drafts-cited/[keyword-slug].md
```

**Input:** Cited draft from Step 6
**Output:** `./content-pipeline/7-preview/[keyword-slug].html`

**What it does:**
- Convert markdown to styled HTML
- Apply Ahrefs blog CSS styling
- Create visual preview for review

---

### Step 8: Format for Publish
Apply WordPress shortcodes and export to .docx.

```
/format-for-publish ./content-pipeline/6-drafts-cited/[keyword-slug].md
```

**Input:** Cited draft from Step 6
**Output:**
- `./content-pipeline/8-publish/[keyword-slug].md` (with shortcodes)
- `./content-pipeline/8-publish/[keyword-slug].docx` (Word document)

**What it does:**
- Convert callouts to WordPress shortcodes
- Format for CMS compatibility
- Export to .docx for upload

---

## Workflow Execution

When running the full pipeline:

1. **Parse keyword** from arguments (or prompt for selection from CSV)
2. **Convert to slug** (lowercase, hyphens: "content marketing" → "content-marketing")
3. **Run each step in sequence:**

```
Step 1: /research "[keyword]"
   → Verify: ./content-pipeline/1-research/[slug].md exists

Step 2: /ahrefs-reference "[keyword]"
   → Verify: ./content-pipeline/2-reference/[slug]-ahrefs.md exists

Step 3: /outline ./content-pipeline/1-research/[slug].md
   → Verify: ./content-pipeline/3-outlines/[slug].md exists

Step 4: /ahrefs-mentions ./content-pipeline/3-outlines/[slug].md
   → Verify: ./content-pipeline/4-outlines-annotated/[slug].md exists

Step 5: /draft ./content-pipeline/4-outlines-annotated/[slug].md
   → Verify: ./content-pipeline/5-drafts/[slug].md exists

Step 6: /verify-claims ./content-pipeline/5-drafts/[slug].md
   → Verify: ./content-pipeline/6-drafts-cited/[slug].md exists

Step 7: /preview ./content-pipeline/6-drafts-cited/[slug].md
   → Verify: ./content-pipeline/7-preview/[slug].html exists

Step 8: /format-for-publish ./content-pipeline/6-drafts-cited/[slug].md
   → Verify: ./content-pipeline/8-publish/[slug].md and .docx exist
```

4. **Report completion** with all file locations

---

## Resume from Step

To resume from a specific step (if earlier outputs exist):

```
/blog-pipeline --from=outline "content marketing"
```

Valid `--from` values:
- `research` (Step 1 - default, full pipeline)
- `ahrefs-reference` (Step 2)
- `outline` (Step 3)
- `ahrefs-mentions` (Step 4)
- `draft` (Step 5)
- `verify-claims` (Step 6)
- `preview` (Step 7)
- `format-for-publish` (Step 8)

Before resuming, verify the required input file exists from the previous step.

---

## Output Summary

After a complete pipeline run:

```
## Pipeline Complete: [keyword]

| Step | Output |
|------|--------|
| 1. Research | ./content-pipeline/1-research/[slug].md |
| 2. Reference | ./content-pipeline/2-reference/[slug]-ahrefs.md |
| 3. Outline | ./content-pipeline/3-outlines/[slug].md |
| 4. Annotated | ./content-pipeline/4-outlines-annotated/[slug].md |
| 5. Draft | ./content-pipeline/5-drafts/[slug].md |
| 6. Cited | ./content-pipeline/6-drafts-cited/[slug].md |
| 7. Preview | ./content-pipeline/7-preview/[slug].html |
| 8. Publish | ./content-pipeline/8-publish/[slug].md, .docx |

Ready for WordPress upload: ./content-pipeline/8-publish/[slug].docx
```

---

## Error Handling

- **Step fails:** Stop pipeline, report error, preserve completed outputs
- **Missing input:** Check if previous step's output exists before proceeding
- **Directory missing:** Create output directory if it doesn't exist

Each step is independent—if the pipeline fails mid-way, you can fix the issue and resume from that step.

---

## Example Usage

**Full pipeline:**
```
/blog-pipeline "keyword research"
```

**Pick from CSV:**
```
/blog-pipeline
```

**Resume from draft step:**
```
/blog-pipeline --from=draft "keyword research"
```

**Just research + outline (stop early):**
```
/blog-pipeline --to=outline "keyword research"
```
