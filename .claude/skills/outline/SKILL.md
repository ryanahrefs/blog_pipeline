---
name: outline
description: Create a structured article outline from a research file
argument-hint: [research-file]
allowed-tools: Read, Write
---

# Outline Skill

Transform a research file into a structured article outline ready for drafting.

## Input

**Research file path** - Path to the research file (from `/research` skill)

## Outline Structure Rules

### H2 Headers Must:
- Logically support the thesis
- Cover the topic completely
- Follow the article type structure
- Avoid passive "-ing" words (use active verbs instead)

### Under Each H2, Include:
1. **BLUF** (Bottom Line Up Front): One bullet with the section's biggest idea
2. **Sub-points**: Supporting details that expand on the BLUF
3. **Evidence**: Examples, data, expert opinions, potential objections to address

## Workflow

1. Read the research file to understand:
   - Target keyword and metrics
   - Related keywords to incorporate
   - Competitor analysis and gaps
   - Recommended angle

2. Draft the thesis statement based on the research angle

3. Create H2 headers that:
   - Support the thesis
   - Cover all key topics from research
   - Fill gaps identified in competitor content

4. For each H2, add:
   - BLUF bullet
   - 2-4 supporting sub-points
   - Evidence placeholders or specific data from research

5. Plan the introduction:
   - Hook idea (statistic, opinion, story, or quote)
   - Thesis statement
   - Preview of what the article covers

6. Plan the conclusion ("Final Thoughts"):
   - Summary of core argument
   - Extra insight or actionable next step (the "souvenir")

7. **Structural Edit Review** - Before finalizing, review and revise the outline against these editing principles:

### MECE Check (Mutually Exclusive, Collectively Exhaustive)
- **No overlap**: Each section covers a distinct idea—no redundancy between H2s
- **Complete coverage**: Together, the sections cover the entire topic promised by the title
- **Sufficient detail**: No major subtopics are missing that readers would expect
- If overlap exists → merge sections or clarify boundaries
- If gaps exist → add missing sections or expand existing ones

### Pyramid Principle Check
- **One idea per section**: Each H2 has a single, clear BLUF (not multiple competing ideas)
- **Evidence supports the idea**: Sub-points and evidence directly support the BLUF
- **Context elaborates**: Additional details add depth without introducing new main ideas
- If a section has multiple main ideas → split into separate H2s
- If evidence doesn't support BLUF → remove or reassign to correct section

### Section Weighting Check
- **Important ideas get more words**: Allocate word count proportional to importance
- **Core sections are substantial**: The main value sections (tips, how-to, analysis) should be 60-70% of total
- **Support sections are concise**: Intro, definitions, conclusions should be 30-40% combined
- Add suggested word counts to each section based on target total
- Flag sections that are over/under-weighted relative to importance

### Title Promise Check
- **Title sets expectation**: What does the title promise the reader will get?
- **Outline delivers**: Does every section contribute to fulfilling that promise?
- **No bait-and-switch**: Remove sections that don't serve the title's promise
- If outline doesn't deliver → revise structure or adjust title

### Header Clarity Check
- **Clear benefits**: Each header signals what the reader will gain from that section
- **Explicit advice**: Headers should be specific, not vague (e.g., "Optimize Your Pin Titles" not "Titles")
- **Scannable value**: A reader skimming headers alone should understand the article's value
- Revise vague headers to be benefit-driven and specific

---

## Output

Save the outline to `./2-outlines/[keyword-slug].md` with this structure:

```markdown
# [Article Title]

**Target Keyword**: [keyword]
**Target Word Count**: [X words]
**Thesis**: [one-sentence thesis]

---

## Structural Edit Review

| Check | Status | Notes |
|-------|--------|-------|
| MECE | ✓ | [No overlap; covers full topic] |
| Pyramid Principle | ✓ | [One idea per section with supporting evidence] |
| Section Weighting | ✓ | [Core sections: X%; Support: Y%] |
| Title Promise | ✓ | [Outline delivers on: "..."] |
| Header Clarity | ✓ | [All headers benefit-driven] |

---

## Introduction

**Hook**: [hook idea and type]

**Thesis**: [thesis statement]

**Preview**: [what reader will learn]

---

## [H2 Header 1]
**Target**: ~[X] words

- **BLUF**: [main point of this section]
- [Sub-point 1]
- [Sub-point 2]
- **Evidence**: [specific example, stat, or expert to cite]

## [H2 Header 2]
**Target**: ~[X] words

...

---

## Final Thoughts

- **Summary**: [restate core argument]
- **Souvenir**: [extra insight or next step for reader]
```

## Example Usage

```
/outline ./1-research/keyword-research.md
```
