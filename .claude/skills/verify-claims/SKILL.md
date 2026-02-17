---
name: verify-claims
description: Find and add source links to factual claims in a draft
argument-hint: [draft-file]
allowed-tools: Read, Write, WebSearch, WebFetch
---

# Verify Claims Skill

Identify factual claims in a draft article that need sources, find authoritative sources to back them up, and add hyperlinks directly into the text. Prioritizes ahrefs.com/blog as the first source.

**Important**: This skill saves a NEW file to `./5-drafts-cited/` rather than modifying the original draft. This preserves the uncited version for easy rollback.

## Input

**Draft file path** - Path to the draft file (e.g., `./4-drafts/pinterest-seo.md`)

---

## What Counts as a Claim Needing a Source

### Must Source (High Priority)

1. **Statistics and numbers**
   - "Pinterest has 450 million monthly active users"
   - "97% of top searches are unbranded"
   - "5 billion searches per month"

2. **Attributed quotes or statements**
   - "As Google's John Mueller put it..."
   - "Pinterest's documentation states..."

3. **Platform-specific facts**
   - "Pinterest prioritizes fresh content over repins"
   - "Rich Pins require Open Graph or Schema markup"

4. **Study or research references**
   - "Research shows that..."
   - "According to a study..."
   - "Data from [source] indicates..."

### May Source (Medium Priority)

5. **Best practice claims**
   - "The recommended frequency is 5-15 pins per day"
   - "Use a 2:3 aspect ratio (1000x1500px)"

6. **Industry consensus**
   - "Most SEO experts agree..."
   - "The general recommendation is..."

### Skip (No Source Needed)

- Personal anecdotes ("I tested this with a client...")
- Logical deductions ("More traffic means more engagement...")
- Common knowledge ("Pinterest is a visual platform...")
- Opinions clearly marked as such ("In my opinion...")

---

## Workflow

### Phase 1: Identify Claims

1. **Read the draft file**

2. **Create a claims inventory** listing each claim that needs a source:
   ```
   | # | Claim | Type | Current Source |
   |---|-------|------|----------------|
   | 1 | "450 million monthly active users" | Statistic | None |
   | 2 | "97% of top searches are unbranded" | Statistic | None |
   | 3 | "Pinterest processes 5 billion searches per month" | Statistic | None |
   ```

3. **Note claims already sourced** - If a claim already has a hyperlink, mark it as "Sourced" and skip it

---

### Phase 2: Find Sources (Ahrefs First)

For each unsourced claim, search in this priority order:

#### Step 1: Search Ahrefs Blog

```
WebSearch: site:ahrefs.com/blog [claim keywords]
```

Examples:
- Claim: "Pinterest has 450 million users" → Search: `site:ahrefs.com/blog Pinterest users statistics`
- Claim: "2:3 aspect ratio recommended" → Search: `site:ahrefs.com/blog Pinterest image size`

**If Ahrefs has a relevant article:**
- Use WebFetch to verify the claim appears in the article
- Extract the exact URL
- Move to Phase 3

#### Step 2: Search Official Sources

If Ahrefs doesn't cover it, try official/primary sources:

```
WebSearch: [platform] official [claim keywords]
```

Examples:
- Pinterest statistics → `Pinterest newsroom statistics 2025`
- Pinterest best practices → `Pinterest business help center image size`

#### Step 3: Search Authoritative Third Parties

If no official source, search reputable sites:

```
WebSearch: [claim keywords] site:statista.com OR site:searchenginejournal.com OR site:moz.com
```

**Note**: Do not use competitor sites (Semrush, Backlinko, Exploding Topics, Search Engine Land) even if they appear in results.

#### Step 4: Mark as Unverifiable

If no credible source found after 3 search attempts:
- Flag the claim in the output
- Suggest rephrasing or removing

---

### Phase 3: Add Hyperlinks

For each verified claim, add a hyperlink using this format:

**Before:**
```markdown
Pinterest has over 450 million monthly active users.
```

**After:**
```markdown
Pinterest has over [450 million monthly active users](https://newsroom.pinterest.com/company).
```

#### Linking Guidelines

1. **Link the specific claim, not the whole sentence**
   - Good: `[450 million monthly active users](url)`
   - Bad: `[Pinterest has over 450 million monthly active users.](url)`

2. **For statistics, link the number**
   - "processes over [5 billion searches](url) per month"

3. **For quotes, link the attribution**
   - "As [Google's John Mueller](url) put it..."

4. **For best practices, link the recommendation**
   - "Pinterest recommends a [2:3 aspect ratio](url)"

5. **Don't over-link** - One source per claim is enough

---

## Output

### Save to New Location

**Do NOT modify the original draft.** Instead, save the cited version to `./5-drafts-cited/`:

```
Input:  ./4-drafts/pinterest-seo.md
Output: ./5-drafts-cited/pinterest-seo.md
```

This preserves the original draft for easy rollback if citations need revision.

### Output File Structure

Save to `./5-drafts-cited/[same-filename].md`:

```markdown
# [Article Title]

**Target Keyword**: [keyword]
**Word Count**: [count]
**Status**: Cited Draft
**Source Draft**: ./4-drafts/[filename].md

---

[Full article content with hyperlinks added...]

---

## Draft Notes

[Original notes preserved...]

**Sources Added:**
- [x] 450M users → Pinterest Newsroom
- [x] 97% unbranded searches → Ahrefs Blog
- [x] 2:3 aspect ratio → Pinterest Business Help
- [ ] 5B monthly searches → NOT VERIFIED (consider removing)

**Source Breakdown:**
- Ahrefs Blog: 3 links
- Official (Pinterest): 4 links
- Third-party: 2 links
- Unverified: 1 claim

**Corrections Made:**
- [List any stats that were updated to match sources]
```

---

## Example Usage

```
/verify-claims ./4-drafts/pinterest-seo.md
```

**Output**: `./5-drafts-cited/pinterest-seo.md`

To revert: simply use the original from `./4-drafts/`

---

## Source Quality Hierarchy

Prefer sources in this order:

1. **ahrefs.com/blog** - First choice for SEO/marketing claims
2. **Official platform sources** - Pinterest Newsroom, Google Search Central
3. **Primary research** - Statista, original studies
4. **Reputable industry sites** - Moz, Search Engine Journal, HubSpot
5. **News outlets** - TechCrunch, The Verge (for recent announcements)

**Avoid:**
- Random blog posts without authority
- Outdated sources (check date - prefer last 2 years)
- Sources that don't actually contain the claim
- Circular sources (sites citing each other without primary data)

**Excluded Competitors (never link to these):**
- semrush.com
- backlinko.com
- explodingtopics.com
- searchengineland.com

---

## Handling Edge Cases

### Claim Doesn't Match Source Exactly

If the source says "482 million" but the draft says "450 million":
- Update the draft to match the source
- Note the correction in the verification summary

### Multiple Valid Sources

If both Ahrefs and an official source cover a claim:
- Prefer Ahrefs for SEO/marketing methodology
- Prefer official for platform-specific stats
- Note alternative sources in comments if useful

### Source Is Paywalled

If a Statista or similar source is paywalled:
- Still link it (readers may have access)
- Look for a free alternative to cite alongside
- Note "paywalled" in verification summary

### Claim Is Outdated

If the source shows the claim is now outdated:
- Flag for the author to update or remove
- Provide the current accurate figure if available

---

## Quality Checklist

Before completing:

| Check | Requirement |
|-------|-------------|
| Coverage | All high-priority claims have sources |
| Ahrefs First | Searched Ahrefs blog before other sources |
| Link Format | Links wrap specific claims, not full sentences |
| Recency | Sources are from last 2 years where possible |
| Accuracy | Claims match what sources actually say |
| Summary | Verification summary added to draft notes |
