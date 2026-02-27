---
name: research
description: Research a keyword using Ahrefs - find related keywords and analyze top-ranking content
argument-hint: [keyword]
allowed-tools: Read, Write, Edit, Bash, WebFetch, mcp__ahrefs__*
---

# Research Skill

Gather keyword intelligence and analyze top-ranking content for a target keyword using Ahrefs MCP.

## Input

**Option A: User provides keyword directly**
If `$ARGUMENTS` contains a keyword, use that keyword and skip to the Workflow section.

**Option B: Select from keyword-ideas.csv**
If `$ARGUMENTS` is empty or user wants to pick from the pipeline:

1. **Read `keyword-ideas.csv`** and filter to show available keywords:
   - Exclude rows where `selected` column = "yes"
   - Sort by `business_potential` (desc), then `priority` (high > medium > low), then `traffic_potential` (desc)

2. **Present top 10 available keywords:**

   ```
   ## Available Keywords (from keyword-ideas.csv)

   | # | Keyword | Volume | TP | KD | Priority | BP | Product |
   |---|---------|--------|-----|-----|----------|-----|---------|
   | 1 | [keyword] | [vol] | [tp] | [kd] | [priority] | [bp] | [product] |
   | 2 | [keyword] | [vol] | [tp] | [kd] | [priority] | [bp] | [product] |
   ...

   Select a keyword by number, or type a custom keyword to research.
   ```

   **Column key:** TP = Traffic Potential, KD = Keyword Difficulty, BP = Business Potential (0-3)

3. **Wait for user selection.**

4. **When user selects a keyword from the list:**
   - Use that keyword for research
   - **Mark it as selected** by updating the `selected` column to "yes" in `keyword-ideas.csv`

   Use the Edit tool to update the CSV:
   ```
   old_string: [keyword],[volume],[tp],[difficulty],...
   new_string: [keyword],[volume],[tp],[difficulty],...,yes
   ```

   If the CSV doesn't have a `selected` column yet, add it as the last column header first.

---

## Workflow

### Step 1: Get Primary Keyword Metrics & Parent Topic

First, get the metrics for the target keyword to understand its parent topic.

Call `mcp__ahrefs__keywords-explorer-overview` with:
- `keywords`: Target keyword
- `country`: "us" (or user's target market)
- `select`: "keyword,volume,difficulty,traffic_potential,cpc,parent_topic"

**Extract:**
- Primary keyword volume and difficulty
- **Parent topic** - This is critical for identifying which keywords can be targeted together

---

### Step 2: Find Long-Tail Variations (Same Parent Topic)

Find long-tail keywords that share the same parent topic as the target keyword. Keywords with the same parent topic can typically be targeted on one page.

Call `mcp__ahrefs__keywords-explorer-matching-terms` with:
- `keywords`: Target keyword
- `country`: "us"
- `select`: "keyword,volume,difficulty,traffic_potential,parent_topic"
- `order_by`: "volume:desc"
- `limit`: 50
- `where`:
```json
{"and": [
  {"field": "volume", "is": ["gte", 50]},
  {"field": "word_count", "is": ["gte", 3]}
]}
```

**Filter results to keep only keywords where:**
- `parent_topic` matches the target keyword's parent topic, OR
- `parent_topic` equals the target keyword itself

**Discard keywords where:**
- Parent topic differs (these need separate articles)
- The keyword represents a different intent (e.g., "youtube seo services" vs "youtube seo tips")

**Organize into:**
- **Primary keyword** - The main target
- **Secondary keywords** - Long-tail variations with same parent topic (can rank with one page)
- **Separate article candidates** - Keywords with different parent topics (note for future content)

---

### Step 3: Pull Questions Report

Use Keywords Explorer to find questions people search for about this topic. These inform FAQ sections, H2 headers, and content gaps.

Call `mcp__ahrefs__keywords-explorer-matching-terms` with:
- `keywords`: Target keyword
- `country`: "us"
- `select`: "keyword,volume,difficulty,parent_topic"
- `order_by`: "volume:desc"
- `limit`: 30
- `terms`: "questions"

**Organize questions into:**

1. **High-priority questions (volume 100+)** - These should be directly addressed in the article, either as H2 headers or dedicated sections

2. **Supporting questions (volume 50-99)** - Good for FAQ sections or brief coverage within related sections

3. **Question themes** - Group similar questions to identify broader topics people want answered:
   - "What is..." questions → Definition/explanation needed
   - "How to..." questions → Tutorial/steps needed
   - "Why..." questions → Reasoning/benefits needed
   - "Best..." questions → Recommendations/comparisons needed

**Note:** Questions don't need to match the exact parent topic - they reveal what users want to know about the subject.

---

### Step 4: Get SERP Overview

Pull the top 10 organic results to identify who ranks and understand the competitive landscape.

Call `mcp__ahrefs__serp-overview` with:
- `keyword`: Target keyword
- `country`: "us"
- `select`: "position,url,title,domain_rating,traffic,refdomains,type"
- `top_positions`: 10

**Extract for each result:**
- URL and title
- Domain rating (authority indicator)
- Estimated traffic to that page
- Type (organic, snippet, etc.)

---

### Step 5: Analyze Search Intent & Content Format

Based on the top 10 SERP results, determine the dominant search intent and content format.

**Analyze the SERP to identify:**

1. **Primary Intent** - What does the searcher want?
   - **Informational** - Wants to learn/understand (guides, explanations, how-tos)
   - **Commercial Investigation** - Researching before a purchase (comparisons, reviews, "best X")
   - **Transactional** - Ready to buy/sign up (product pages, pricing, tools)
   - **Navigational** - Looking for a specific site/page

2. **Dominant Content Format** - What format ranks?
   - **Comprehensive Guide** - Long-form educational content (2000+ words)
   - **Listicle** - Numbered lists ("10 ways to...", "Best X for Y")
   - **How-To/Tutorial** - Step-by-step instructions
   - **Tool/Calculator** - Interactive tools or apps
   - **Comparison** - X vs Y, feature comparisons
   - **Definition/Explainer** - "What is X" focused content
   - **Video** - YouTube videos ranking in SERPs

3. **Content Depth Signals:**
   - Average word count of top 3 results
   - Presence of tools ranking (indicates transactional sub-intent)
   - Reddit/forum results (indicates discussion/opinion seeking)
   - Video results (indicates visual learning preference)

**Summarize as:**
- Primary intent (1-2 words)
- Secondary intent if mixed (optional)
- Recommended content format to match SERP

---

### Step 6: Analyze Top 3 Ranking Pages

For the top 3 organic results from Step 4, extract and analyze their content.

**For each URL, use WebFetch with this prompt:**
```
Extract the exact H2 and H3 headers from this article in order. Format as:
## [H2 text]
### [H3 text]
### [H3 text]
## [H2 text]
...
Also note: approximate word count, and any lists/tables/special elements used.
```

**Record for each article:**
1. **Full header structure** - Every H2 and H3 in order (this is critical for outline creation)
2. **Word count** - Approximate length
3. **Special elements** - Lists, tables, images, downloadable resources

**After analyzing all 3, identify patterns:**
- Headers/topics covered by all 3 (must include)
- Headers/topics covered by 2/3 (should include)
- Unique headers (potential differentiators or gaps)

---

### Step 7: Identify Content Gaps and Opportunities

Compare the 3 analyzed articles against each other and against user questions to find gaps.

**A. Header/Topic Gap Analysis**

Create a comparison matrix of what each competitor covers:

| Topic/Header | Article 1 | Article 2 | Article 3 | Gap? |
|--------------|-----------|-----------|-----------|------|
| [topic from headers] | ✓ | ✓ | ✓ | No - must cover |
| [topic from headers] | ✓ | ✓ | ✗ | No - should cover |
| [topic from headers] | ✓ | ✗ | ✗ | Maybe - differentiator |
| [topic NOT in any] | ✗ | ✗ | ✗ | Yes - opportunity |

**B. Questions Gap Analysis**

Cross-reference the questions from Step 3 against competitor content:
- Which high-volume questions do competitors answer well?
- Which questions are NOT addressed by any competitor? (opportunities)
- Which questions are only partially answered? (depth opportunity)

**C. Identify Opportunities**

Based on the gap analysis, identify:

1. **Missing topics** - Headers/subjects no competitor covers that users search for
2. **Underserved questions** - Questions with search volume that competitors don't answer
3. **Depth gaps** - Topics competitors mention briefly that deserve fuller treatment
4. **Freshness gaps** - Outdated information or missing current-year updates
5. **Format gaps** - Missing elements (tables, checklists, examples) that would add value

**D. Determine Angle**

Based on gaps, decide how to differentiate:
- More comprehensive coverage of underserved topics
- Better answers to unaddressed questions
- Fresher, more current information
- More actionable/practical focus
- Better structure or scannability

---

## Output

Save to `./content-pipeline/1-research/[keyword-slug].md`:

```markdown
# Research: [Keyword]

**Date**: [YYYY-MM-DD]
**Target Market**: [country]

---

## Keyword Targeting

### Primary Keyword
| Keyword | Volume | KD | Traffic Potential | Parent Topic |
|---------|--------|-----|-------------------|--------------|
| [target keyword] | [vol] | [kd] | [tp] | [parent] |

### Secondary Keywords (Same Parent Topic - Target on Same Page)
These long-tail variations share the same parent topic and can be targeted in one article.

| Keyword | Volume | KD | Parent Topic |
|---------|--------|-----|--------------|
| [keyword] | [vol] | [kd] | [parent] |

---

## Questions Report

### High-Priority Questions (Volume 100+)
Address these directly in the article.

| Question | Volume | Addressed by Competitors? |
|----------|--------|---------------------------|
| [question] | [vol] | [Yes - all / Partial / No] |

### Supporting Questions (Volume 50-99)
Good for FAQ or brief coverage.

- [question] ([volume])
- [question] ([volume])

### Question Themes
- **"What is..." questions:** [list]
- **"How to..." questions:** [list]
- **"Why/Best..." questions:** [list]

---

## Keyword Targeting (Continued)

### Separate Article Opportunities
Keywords with different parent topics - these need their own dedicated articles.

| Keyword | Volume | Parent Topic | Why Separate |
|---------|--------|--------------|--------------|
| [keyword] | [vol] | [different parent] | [different intent/topic] |

---

## SERP Analysis

### Top 10 Results
| Pos | Title | Domain | DR | Traffic |
|-----|-------|--------|-----|---------|
| 1 | [title] | [domain] | [dr] | [traffic] |
| 2 | [title] | [domain] | [dr] | [traffic] |
...

### Search Intent Analysis

**Primary Intent:** [Informational / Commercial Investigation / Transactional / Navigational]

**Intent Signals:**
- [What in the SERP indicates this intent - e.g., "All top results are educational guides"]
- [E.g., "No product pages or tools in top 10"]
- [E.g., "People Also Ask boxes focus on 'how to' and 'what is' questions"]

**Dominant Content Format:** [Comprehensive Guide / Listicle / How-To / Tool / Comparison / Definition]

**Format Signals:**
- [What formats rank - e.g., "7/10 results are long-form guides"]
- [E.g., "Top result is 6,000+ words"]
- [E.g., "One tool (TubeRanker) ranks at position 5"]

**Recommended Approach:** [1-2 sentence summary of what content format to create to match the SERP]

---

### Top 3 Content Analysis

#### 1. [Title] - [Domain]
**URL**: [url]
**Estimated Traffic**: [traffic]
**Word Count**: ~[X] words

**Header Structure:**
```
## [H2 header 1]
### [H3 sub-header]
### [H3 sub-header]
## [H2 header 2]
### [H3 sub-header]
## [H2 header 3]
...
```

**Special Elements:** [lists, tables, images, downloads, etc.]

---

#### 2. [Title] - [Domain]
**URL**: [url]
**Estimated Traffic**: [traffic]
**Word Count**: ~[X] words

**Header Structure:**
```
## [H2 header 1]
### [H3 sub-header]
## [H2 header 2]
...
```

**Special Elements:** [lists, tables, images, downloads, etc.]

---

#### 3. [Title] - [Domain]
**URL**: [url]
**Estimated Traffic**: [traffic]
**Word Count**: ~[X] words

**Header Structure:**
```
## [H2 header 1]
### [H3 sub-header]
## [H2 header 2]
...
```

**Special Elements:** [lists, tables, images, downloads, etc.]

---

## Common Patterns

**Headers/Topics All 3 Cover (Must Include):**
- [header theme or topic]
- [header theme or topic]

**Headers/Topics 2/3 Cover (Should Include):**
- [header theme or topic]
- [header theme or topic]

**Unique to One Competitor (Potential Differentiator):**
- [unique header/topic] - from [competitor]

**Structural Patterns:**
- Average H2 sections: [N]
- Average H3 sub-sections: [N]
- Common elements: [lists, tables, images, etc.]
- Word count range: [X-Y words]

---

## Content Gaps & Opportunities

### Topic Coverage Matrix
| Topic | Art. 1 | Art. 2 | Art. 3 | Opportunity |
|-------|--------|--------|--------|-------------|
| [topic] | ✓ | ✓ | ✓ | Must cover |
| [topic] | ✓ | ✓ | ✗ | Should cover |
| [topic] | ✓ | ✗ | ✗ | Differentiator |
| [topic] | ✗ | ✗ | ✗ | Gap - opportunity |

### Unanswered Questions
Questions from Step 3 that competitors don't address well:
- [question] ([volume]) - Not covered by any competitor
- [question] ([volume]) - Only partially addressed

### Gap Summary

**Missing Topics:**
- [topic no competitor covers]

**Depth Opportunities:**
- [topic covered briefly that deserves more]

**Freshness Gaps:**
- [outdated info or missing current-year content]

**Format Gaps:**
- [missing tables, checklists, examples, etc.]

---

## Recommended Approach

**Angle**: [unique angle to differentiate]

**Content Type**: [guide / listicle / tutorial / comparison]

**Target Word Count**: [X words] (based on competitor average)

**Key Differentiators:**
- [What will make this stand out]
- [Gaps to fill]
- [Unique value to add]

**Suggested H2 Structure:**
1. [H2 idea based on research]
2. [H2 idea]
3. [H2 idea]
...
```

---

## Example Usage

**Option A: Specify a keyword directly**
```
/research "content marketing strategy"
```

**Option B: Pick from pipeline (no argument)**
```
/research
```
This shows available keywords from `keyword-ideas.csv` for selection. Selected keywords are marked so they won't appear again.

---

## Common MCP Parameters

**Date format:**
- ✅ Correct: `"2026-02-17"` (YYYY-MM-DD)
- ❌ Wrong: `"today"`, `"latest"`

**Country codes:**
- ✅ Correct: `"us"`, `"gb"`, `"de"`, `"au"`, `"ca"`
- ❌ Wrong: `"allGlobal"`, `"all"`

**Filter syntax:**
```json
{"field": "volume", "is": ["gte", 100]}
{"and": [filter1, filter2]}
{"or": [filter1, filter2]}
```

---

## Troubleshooting

### No Related Keywords Found
- Try broader keyword (e.g., "SEO" instead of "technical SEO audit checklist")
- Check spelling
- Try different country code

### SERP Overview Empty
- Keyword may be too niche
- Try variations of the keyword

### WebFetch Fails for Competitor URLs
- Some sites block scraping
- Note which URLs couldn't be analyzed
- Use available data from other competitors

### MCP Connection Issues
- Verify Ahrefs MCP is connected in settings
- Check API key is valid
- Confirm Ahrefs subscription includes API access
