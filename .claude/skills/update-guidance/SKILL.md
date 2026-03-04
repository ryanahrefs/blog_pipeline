---
name: update-guidance
description: Set update priorities and goals before running audits
argument-hint: [slug]
allowed-tools: Read, Write, AskUserQuestion
---

# Update Guidance Skill

Gather user input on update priorities before running audits. This optional step lets users steer the update toward specific goals like "refresh stats only" or "focus on new Ahrefs features."

## Input

**Slug** - The article slug (e.g., `programmatic-seo`)

The extracted file should exist at `./update-pipeline/1-extracted/[slug].md`.

---

## Workflow

### Step 1: Verify Extracted File Exists

Check that `./update-pipeline/1-extracted/[slug].md` exists. If not, inform user to run `/extract-content` first.

### Step 2: Read Article Metadata

From the extracted file, note:
- Article title
- Last Modified date
- Calculate article age in months
- Approximate word count

### Step 3: Ask Structured Questions

Use `AskUserQuestion` to gather update priorities:

#### Question 1: Primary Goal

**Question:** What's your primary goal for this update?
**Header:** Goal
**Options:**
| Label | Description |
|-------|-------------|
| Refresh stats (Recommended) | Update outdated statistics and claims |
| Add Ahrefs features | Mention new product features launched since publication |
| Fill content gaps | Add missing topics that competitors now cover |
| Full refresh | All of the above - comprehensive update |

#### Question 2: Target Audience

**Question:** Who is the target audience for this article?
**Header:** Audience
**Options:**
| Label | Description |
|-------|-------------|
| Beginners (Recommended) | New to SEO/topic, needs fundamentals explained |
| Intermediate | Familiar with basics, wants tactical advice |
| Experts | Deep practitioners, wants advanced techniques |
| Mixed | All skill levels - keep current approach |

#### Question 3: Update Scope

**Question:** How extensive should this update be?
**Header:** Scope
**Options:**
| Label | Description |
|-------|-------------|
| Minimal | Less than 500 words added |
| Moderate (Recommended) | 500-1500 words added |
| Major | 1500+ words added |
| No limit | Whatever is needed to make it competitive |

#### Question 4: Structural Changes

**Question:** Are you open to changing the article structure?
**Header:** Structure
**Options:**
| Label | Description |
|-------|-------------|
| Keep current (Recommended) | Only update existing sections, no new H2s |
| Allow new sections | Can add new H2 sections as needed |
| Allow restructuring | Can reorganize the entire article if needed |

### Step 4: Generate Instructions for Audits

Based on the answers, determine how each audit skill should behave:

| Primary Goal | `/update-claims` | `/update-ahrefs-mentions` | `/update-topic-gaps` |
|--------------|------------------|---------------------------|----------------------|
| Refresh stats | **PRIORITY** | LOW | SKIP |
| Add Ahrefs features | LOW | **PRIORITY** | SKIP |
| Fill content gaps | LOW | LOW | **PRIORITY** |
| Full refresh | PRIORITY | PRIORITY | PRIORITY |

**Scope constraints:**
- Minimal: Be conservative, only critical updates
- Moderate: Balance thoroughness with brevity
- Major: Be thorough, identify all opportunities
- No limit: Full analysis, no constraints

**Structure constraints:**
- Keep current: No new H2 sections recommended
- Allow new sections: Can suggest new sections
- Allow restructuring: Can suggest major changes

---

## Output

Save to `./update-pipeline/0-guidance/[slug].md`:

```markdown
# Update Guidance: [slug]

**Generated:** [today's date]
**Article:** [article title]
**Last Modified:** [date] ([X months ago])

---

## User Selections

| Setting | Selection |
|---------|-----------|
| Primary goal | [selection] |
| Target audience | [selection] |
| Scope | [selection] |
| Structural changes | [selection] |

---

## Instructions for Audits

Based on the selections above, here's how each audit should behave:

### `/update-claims`

**Priority:** [PRIORITY / LOW / SKIP]

**Instructions:**
- [Specific instructions based on goal/scope]

### `/update-ahrefs-mentions`

**Priority:** [PRIORITY / LOW / SKIP]

**Instructions:**
- [Specific instructions based on goal/scope]

### `/update-topic-gaps`

**Priority:** [PRIORITY / LOW / SKIP]

**Instructions:**
- [Specific instructions based on goal/scope]

---

## Constraints

- **Scope:** [scope selection] - [interpretation]
- **Structure:** [structure selection] - [interpretation]
- **Audience:** [audience selection] - [implications for tone/depth]
```

---

## Example Usage

```
/update-guidance programmatic-seo
```

**Output**: `./update-pipeline/0-guidance/programmatic-seo.md`

---

## What Happens Next

After running `/update-guidance`, the downstream audit skills will:

1. Check if `./update-pipeline/0-guidance/[slug].md` exists
2. If yes, read the priority level for their audit type
3. Adjust behavior:
   - **PRIORITY**: Full analysis, all findings included
   - **LOW**: Conservative analysis, only obvious/critical findings
   - **SKIP**: Output minimal file noting skip per guidance
4. Include guidance summary in output header

---

## Skipping This Step

This skill is optional. If users run audits without running `/update-guidance` first:

- Audits run with default behavior (full analysis)
- No guidance file is referenced
- All audit types are treated as PRIORITY

---

## Example Scenarios

### Scenario: Quick Stats Refresh

**Answers:**
- Goal: Refresh stats
- Scope: Minimal

**Resulting guidance:**
- `/update-claims`: PRIORITY - Focus on outdated statistics
- `/update-ahrefs-mentions`: LOW - Only obvious natural fits
- `/update-topic-gaps`: SKIP - No new sections wanted

### Scenario: Comprehensive Update

**Answers:**
- Goal: Full refresh
- Scope: No limit
- Structure: Allow restructuring

**Resulting guidance:**
- All audits: PRIORITY
- No constraints on scope or structure
- Full competitive analysis enabled
