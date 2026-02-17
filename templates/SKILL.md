---
name: [skill-name]
description: [Clear, specific description of what this skill does. Include when to use it and keywords users would say. Example: "Identifies content gaps using Ahrefs competitor analysis. Use when analyzing competitors, finding keyword opportunities, or planning content strategy."]
allowed-tools: "mcp__ahrefs__*"
---

# [Skill Title]

> **Based on:** [Link to Ahrefs blog post]

[1-2 sentence description of what this skill does, referencing $ARGUMENTS. Example: "Analyze **$ARGUMENTS** to identify content gaps—keyword opportunities where competitors rank but you don't, revealing high-value topics to target."]

---

## Analysis Workflow

### 1. [First Step Title - Data Collection]

Call `mcp__ahrefs__[tool-name]` with:
- `target`: $ARGUMENTS (with trailing slash, e.g., "example.com/")
- `mode`: "subdomains" (for domain analysis) or "exact" (for specific URLs)
- `select`: "[field1],[field2],[field3],..." (specific fields needed)
- `date`: Current date in YYYY-MM-DD format (e.g., "2026-02-10")
- `country`: 2-letter ISO country code (e.g., "us", "gb", "de")
- `where`: [Optional filter using JSON structure]:
  ```json
  {
    "and": [
      {"field":"[field_name]","is":["gte",[value]]},
      {"field":"[field_name]","is":["gt",[value]]}
    ]
  }
  ```
- `order_by`: "[field]:desc" (or ":asc")
- `limit`: [Number, typically 20-50]

**Key field:** `[field_name]` - [What this field shows and why it matters]

**Results:** [What data you'll receive from this API call]

**Output:** Before proceeding to analysis, present a simple numbered list of items found:
1. [item name/identifier] ([key metric])
2. [item name/identifier] ([key metric])
3. [item name/identifier] ([key metric])
...

This gives the user a quick overview of [what was discovered/scope of analysis].

### 2. [Second Step Title - Analysis/Prioritization]

[Instructions for analyzing and categorizing the data collected in Step 1]

Assign priority levels based on [criteria]:

**🔴 HIGH PRIORITY (Address first)**
- [Criterion 1 with specific threshold/condition]
- [Criterion 2 with specific threshold/condition]
- Example: [Concrete example of high priority item]

**🟡 MEDIUM PRIORITY (Investigate further)**
- [Criterion 1 with specific threshold/condition]
- [Criterion 2 with specific threshold/condition]
- Example: [Concrete example of medium priority item]

**🟢 LOW PRIORITY (Safe to ignore or monitor)**
- [Criterion 1 with specific threshold/condition]
- [Criterion 2 with specific threshold/condition]
- Example: [Concrete example of low priority item]

**Prioritization heuristics:**
- [Rule/pattern 1] → [Priority level]
- [Rule/pattern 2] → [Priority level]
- [Rule/pattern 3] → [Priority level]

### 3. [Third Step Title - Deep Dive on Priority Items]

For **high priority** and **medium priority** items, use `mcp__ahrefs__[tool-name]`:

**Call for each [priority item]:**
- `target`: [Description of what target should be, e.g., "Full URL of competing page"]
- `mode`: "[mode value]"
- `date`: Current date in YYYY-MM-DD format
- [Additional parameters as needed]

**Returns metrics:**
- `[metric1]`: [What it shows]
- `[metric2]`: [What it shows]
- `[metric3]`: [What it shows]

**Compare [specific metric]** to determine [what decision/insight this enables].

**Additional check:**
- [Any secondary validation or cross-check needed]
- Example: Check if [condition], which would indicate [insight]

### 4. Provide Recommendations

Tailor recommendations based on priority level and analysis findings:

**🔴 HIGH PRIORITY → [Primary Action]**
- **Action:** [Specific action to take]
- [Sub-action or implementation detail]
- [Sub-action or implementation detail]
- **Why:** [Reasoning based on data/strategy]

**🟡 MEDIUM PRIORITY → [Secondary Action]**
- **Option A:** [Approach 1] if [condition]
- **Option B:** [Approach 2] if [different condition]
- **Why:** [Reasoning based on data/strategy]

**🟢 LOW PRIORITY → [Minimal/No Action]**
- **Action:** [What to do, often "monitor" or "keep as-is"]
- [Any minimal action if needed]
- **Why:** [Reasoning why this doesn't need immediate attention]

**For [specific scenario] (common case):**
- [Detailed implementation guidance]
- [Expected outcome]
- [What to monitor post-implementation]

### 5. Create Action Plan

For each [issue/opportunity], provide:
- **[Component 1]:** [Specific value/approach] ([reasoning])
- **[Component 2]:** [Specific value/approach] ([reasoning])
- **Implementation steps:** [Numbered sequence]
- **Expected impact:** [Predicted outcome based on data]
- **Monitoring:** [What metrics to track]

### 6. Generate Complete Analysis Table

Create a comprehensive table of ALL [items] analyzed in this session.

**Table structure:**

| [Column 1] | [Column 2] | [Column 3] | [Column 4] | [Column 5] | [Action/Recommendation] |
|------------|------------|------------|------------|------------|-------------------------|
| [data] | [data] | [data] | [data] | [data] | [action] |

**Column definitions:**
- **[Column 1]:** [Description]
- **[Column 2]:** [Description]
- **[Column 3]:** [Description]
- **[Column 4]:** [Description]
- **[Column 5]:** [Description]
- **[Action/Recommendation]:** [Description]

**Format instructions:**
1. Present as markdown table for readability
2. Sort by [primary sort criterion], then by [secondary sort criterion]
3. Include ALL items analyzed, not just high priority
4. After the table, provide CSV download option

**Benefits of this table:**
- Complete reference document for implementation
- Easy to share with team members
- Can be imported into project management tools
- Provides audit trail of analysis decisions

---

## Common MCP Parameters

**Date format:**
- ✅ Correct: `"2026-02-10"` (YYYY-MM-DD)
- ❌ Wrong: `"today"`, `"latest"`, `"now"`
- Always use actual date in YYYY-MM-DD format

**Country codes:**
- ✅ Correct: `"us"`, `"gb"`, `"de"`, `"fr"`, `"ca"`, `"au"`
- ❌ Wrong: `"allGlobal"`, `"all"`, `"worldwide"`
- Must use 2-letter ISO 3166-1 alpha-2 country code
- No "all countries" option exists—choose primary market

**Target format:**
- ✅ Correct: `"example.com/"` (with trailing slash)
- ✅ Also correct: `"https://example.com/page/"` (full URL for exact mode)
- Include trailing slash for proper URL encoding

**Filter syntax (where parameter):**
- Use JSON format: `{"field":"column_name","is":["operator",value]}`
- Operators: `"eq"` (equals), `"neq"` (not equals), `"gt"` (greater than), `"gte"` (greater than or equal), `"lt"` (less than), `"lte"` (less than or equal)
- Combine filters: `{"and":[filter1,filter2]}` or `{"or":[filter1,filter2]}`
- Example: `{"and":[{"field":"volume","is":["gte",100]},{"field":"[field]","is":["gt",1]}]}`

**[Skill-specific parameter guidance]:**
- [Any additional parameter patterns specific to this skill's workflow]
- [Example with ✅ correct format]

**Tool naming:**
- Always use full MCP prefix: `mcp__ahrefs__site-explorer-[feature]`
- Not shortened: `site-explorer-[feature]`

---

## Presentation Format

Present findings using this structure:

### Quick Summary
- [Metric 1]: [number]
- [Metric 2]: [number]
- [Metric 3 (priority breakdown)]: [number]
- [Metric 4 (priority breakdown)]: [number]
- [Metric 5 (priority breakdown)]: [number]

### Detailed Analysis

For each high and medium priority item:

**[Number]. [Item Identifier]: "[Name/Details]" ([Key Metric])**

| [Column] | [Column] | [Column] | [Column] |
|----------|----------|----------|----------|
| [data] | [data] | [data] | [data] |

**Priority:** [🔴 HIGH / 🟡 MEDIUM / 🟢 LOW] - [Brief reasoning for priority assignment]

**[Analysis Label]:** [Detailed reasoning based on data—explain what the numbers show and what they mean for strategy]

**Recommendation:** [ACTION VERB IN CAPS]
- **[Component 1]:** [specific value] ([reason based on data])
- **[Component 2]:** [specific value] ([reason based on data])
- **Why:** [Strategic reasoning]
- **Expected impact:** [Predicted outcome]

### 🟢 Low Priority [Items] (Brief Summary)

List 2-3 examples of items that are low priority and why:
- **"[example 1]"** - [Brief reason why it's low priority]
- **"[example 2]"** - [Brief reason why it's low priority]

### Complete Analysis Table

Provide a comprehensive table of ALL [items] analyzed:

| [Column] | [Column] | [Column] | [Column] | [Column] | [Priority] | [Recommendation] |
|----------|----------|----------|----------|----------|-----------|------------------|
| [data] | [data] | [data] | [data] | [data] | 🔴/🟡/🟢 | [action] |

Followed by CSV format for download:
```csv
[Column1],[Column2],[Column3],[Column4],[Column5],[Priority],[Recommendation]
[data row 1]
[data row 2]
[data row 3]
```

**Summary:** [Key insight from overall analysis—what percentage of items need action, main patterns discovered]

### Action Plan

**Priority 1: [Issue/Opportunity Description]**
1. [Specific, actionable step]
2. [Specific, actionable step]
3. [Specific, actionable step]
4. Monitor: [What metrics to track and for how long]

**Priority 2: [Issue/Opportunity Description]**
1. [Specific, actionable step]
2. [Specific, actionable step]

### Next Steps

**To implement [recommendations]:**
- [Implementation guidance step 1]
- [Implementation guidance step 2]
- [Implementation guidance step 3]

**To monitor impact:**
- [Monitoring step 1 with timeframe]
- [Monitoring step 2 with metrics to watch]
- [Monitoring step 3 with success indicators]

**[Relevant Ahrefs tool for follow-up]:**
[URL to relevant Ahrefs app tool]

---

## Example

**User:** [Example natural language prompt that would trigger this skill]

**Claude:**

✅ **Step 1: [Action completed]. [N] [items] found.**

**[Title for initial list]:**
1. [item] ([metric])
2. [item] ([metric])
3. [item] ([metric])
4. [item] ([metric])
5. [item] ([metric])
... ([N more])

---

### Quick Summary
- [Metric 1]: [number]
- [Metric 2]: [number]
- 🔴 High priority issues: [number]
- 🟡 Medium priority issues: [number]
- 🟢 Low priority issues: [number]

---

### Detailed Analysis

#### 1. [Item Identifier]: "[Name]" ([Key Metric])

| [Column] | [Column] | [Column] | [Column] |
|----------|----------|----------|----------|
| [data] | [data] | [data] | [data] |

**Priority:** 🔴 **HIGH** - [Specific reasoning based on data showing why this is high priority]

**[Analysis Label]:** [Detailed explanation of what the data reveals about this item]

**Recommendation:** ⚠️ **[ACTION]**
- **[Component 1]:** [value] ([reasoning])
- **[Component 2]:** [value] ([reasoning])
- **Why:** [Strategic explanation]
- **Expected impact:** [Predicted outcome]

#### 2. [Item Identifier]: "[Name]" ([Key Metric])

| [Column] | [Column] | [Column] | [Column] |
|----------|----------|----------|----------|
| [data] | [data] | [data] | [data] |

**Priority:** 🟡 **MEDIUM** - [Reasoning]

**[Analysis Label]:** [Explanation]

**Recommendation:** [ACTION]
- [Details]

---

### 🟢 Low Priority Issues (Sample)

- **[example 1]** - [Why it's low priority]
- **[example 2]** - [Why it's low priority]
- **[example 3]** - [Why it's low priority]

---

### Complete Analysis Table

Here's the complete analysis of all [N] [items] (sorted by priority, then [metric]):

| [Column] | [Column] | [Column] | [Column] | [Column] | Priority | Recommendation |
|----------|----------|----------|----------|----------|----------|----------------|
| [data] | [data] | [data] | [data] | [data] | 🔴 High | [action] |
| [data] | [data] | [data] | [data] | [data] | 🟢 Low | [action] |
| [data] | [data] | [data] | [data] | [data] | 🟢 Low | [action] |
| ... | ... | ... | ... | ... | ... | ... |

**Download as CSV:**

```csv
[Column1],[Column2],[Column3],[Column4],[Column5],Priority,Recommendation
[data],[data],[data],[data],[data],High,[action]
[data],[data],[data],[data],[data],Low,[action]
[data],[data],[data],[data],[data],Low,[action]
```

**Summary:** [Key insight about results—e.g., "X high priority items found among Y analyzed (Z% requiring immediate action)"]

---

### Action Plan

**Priority 1: [Description]**
1. [Step]
2. [Step]
3. [Step]
4. Monitor: [What to track]

**Priority 2: [Description]**
1. [Step]
2. [Step]

---

### Next Steps

**To implement [recommendations]:**
- [Step 1]
- [Step 2]
- [Step 3]

**To monitor impact:**
- [Monitoring 1]
- [Monitoring 2]

**[Relevant tool]:**
[URL]

---

## Troubleshooting

### [Common Issue #1 Name]

**Error:** "[Error message or symptom]"

**Cause:** [What causes this issue]

**Solution:**
1. [Specific step to resolve]
2. [Specific step to resolve]
3. [Specific step to resolve]

---

### [Common Issue #2 Name]

**Error:** "[Error message or symptom]"

**Cause:** [What causes this issue]

**Solution:**
1. [Specific step to resolve]
2. [Specific step to resolve]

---

### MCP Connection Failed

**Error:** "Could not connect to Ahrefs MCP server" or "Authentication failed"

**Solution:**
1. Verify MCP server is connected: Settings > Extensions > Ahrefs
2. Check that your Ahrefs API key is valid and not expired
3. Confirm you have an active Ahrefs subscription with API access
4. Try disconnecting and reconnecting the MCP server
5. If issue persists, test MCP connection independently without the skill

---

### [Skill-Specific Issue #3]

**Symptom:** [Observable behavior]

**Cause:** [What causes this]

**Solution:**
1. [Resolution step]
2. [Resolution step]
3. [Alternative approach if needed]

---

### Parameter Format Issues

**Error:** "[Common parameter error]"

**Cause:** Incorrect parameter format

**Solution:**
1. Use YYYY-MM-DD date format (not "today" or "latest")
2. Use 2-letter ISO country codes ("us", "gb", "de")
3. Include trailing slash in domains ("example.com/")
4. Use JSON format for filters with proper operators

---

*This skill is part of the Ahrefs Marketing Skills collection.*
