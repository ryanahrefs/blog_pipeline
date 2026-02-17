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
| 1 | `/research` | keyword | `1-research/` |
| 2 | `/outline` | research file | `2-outlines/` |
| 3 | `/ahrefs-mentions` | outline file | `3-outlines-annotated/` |
| 4 | `/draft` | annotated outline | `4-drafts/` |
| 5 | `/verify-claims` | draft file | `5-drafts-cited/` |
| 6 | `/preview` | cited draft | `6-preview/` |
| 7 | `/format-for-publish` | cited draft | `7-publish/` |

---

## Step Details

### Step 1: Research
Gather keyword intelligence and analyze top-ranking content.

```
/research [keyword]
```

**Input:** Keyword (from argument or selected from CSV)
**Output:** `./1-research/[keyword-slug].md`

**What it does:**
- Get keyword metrics (volume, difficulty, traffic potential)
- Find long-tail variations with same parent topic
- Pull questions report
- Analyze SERP and top 3 ranking pages
- Identify content gaps and opportunities

---

### Step 2: Outline
Create a structured article outline based on research.

```
/outline ./1-research/[keyword-slug].md
```

**Input:** Research file from Step 1
**Output:** `./2-outlines/[keyword-slug].md`

**What it does:**
- Create H2/H3 structure based on competitor analysis
- Include target keywords for each section
- Add content briefs with key points to cover
- Incorporate questions to answer

---

### Step 3: Ahrefs Mentions
Annotate outline with natural Ahrefs product mentions.

```
/ahrefs-mentions ./2-outlines/[keyword-slug].md
```

**Input:** Outline file from Step 2
**Output:** `./3-outlines-annotated/[keyword-slug].md`

**What it does:**
- Identify sections where Ahrefs tools add value
- Add contextual product mentions (not forced)
- Include specific feature recommendations
- Preserve original outline structure

---

### Step 4: Draft
Expand the annotated outline into a full article.

```
/draft ./3-outlines-annotated/[keyword-slug].md
```

**Input:** Annotated outline from Step 3
**Output:** `./4-drafts/[keyword-slug].md`

**What it does:**
- Write full prose for each section
- Follow Ahrefs blog voice and style
- Include examples and explanations
- Add transitional content between sections

---

### Step 5: Verify Claims
Find and add source links to factual claims.

```
/verify-claims ./4-drafts/[keyword-slug].md
```

**Input:** Draft file from Step 4
**Output:** `./5-drafts-cited/[keyword-slug].md`

**What it does:**
- Identify factual claims needing sources
- Search for authoritative sources
- Add hyperlinks to claims
- Flag claims that couldn't be verified

---

### Step 6: Preview
Generate an Ahrefs-styled HTML preview.

```
/preview ./5-drafts-cited/[keyword-slug].md
```

**Input:** Cited draft from Step 5
**Output:** `./6-preview/[keyword-slug].html`

**What it does:**
- Convert markdown to styled HTML
- Apply Ahrefs blog CSS styling
- Create visual preview for review

---

### Step 7: Format for Publish
Apply WordPress shortcodes and export to .docx.

```
/format-for-publish ./5-drafts-cited/[keyword-slug].md
```

**Input:** Cited draft from Step 5
**Output:**
- `./7-publish/[keyword-slug].md` (with shortcodes)
- `./7-publish/[keyword-slug].docx` (Word document)

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
   → Verify: ./1-research/[slug].md exists

Step 2: /outline ./1-research/[slug].md
   → Verify: ./2-outlines/[slug].md exists

Step 3: /ahrefs-mentions ./2-outlines/[slug].md
   → Verify: ./3-outlines-annotated/[slug].md exists

Step 4: /draft ./3-outlines-annotated/[slug].md
   → Verify: ./4-drafts/[slug].md exists

Step 5: /verify-claims ./4-drafts/[slug].md
   → Verify: ./5-drafts-cited/[slug].md exists

Step 6: /preview ./5-drafts-cited/[slug].md
   → Verify: ./6-preview/[slug].html exists

Step 7: /format-for-publish ./5-drafts-cited/[slug].md
   → Verify: ./7-publish/[slug].md and .docx exist
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
- `outline` (Step 2)
- `ahrefs-mentions` (Step 3)
- `draft` (Step 4)
- `verify-claims` (Step 5)
- `preview` (Step 6)
- `format-for-publish` (Step 7)

Before resuming, verify the required input file exists from the previous step.

---

## Output Summary

After a complete pipeline run:

```
## Pipeline Complete: [keyword]

| Step | Output |
|------|--------|
| 1. Research | ./1-research/[slug].md |
| 2. Outline | ./2-outlines/[slug].md |
| 3. Annotated | ./3-outlines-annotated/[slug].md |
| 4. Draft | ./4-drafts/[slug].md |
| 5. Cited | ./5-drafts-cited/[slug].md |
| 6. Preview | ./6-preview/[slug].html |
| 7. Publish | ./7-publish/[slug].md, .docx |

Ready for WordPress upload: ./7-publish/[slug].docx
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
