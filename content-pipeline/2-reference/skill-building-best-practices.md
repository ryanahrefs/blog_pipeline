# Claude Skills: Best Practices for Building and Testing

*Extracted from: The Complete Guide to Building Skills for Claude (Anthropic, 2026)*

---

## Core Principles

### Progressive Disclosure (Three-Level System)
1. **Level 1: YAML frontmatter** - Always loaded in system prompt. Must be minimal but sufficient for Claude to know when to load the skill.
2. **Level 2: SKILL.md body** - Loaded when skill is triggered. Contains full instructions.
3. **Level 3: Linked files** - Additional resources loaded only as needed (references/, assets/, scripts/).

### Composability
- Skills must work alongside other skills
- Don't assume your skill is the only one loaded
- Avoid conflicting with built-in capabilities

### Portability
- Skills work identically across Claude.ai, Claude Code, and API
- Create once, use everywhere (if dependencies are met)

---

## File Structure Requirements

### Critical Rules

**SKILL.md naming:**
- ✅ Must be exactly `SKILL.md` (case-sensitive)
- ❌ No variations: `SKILL.MD`, `skill.md`, `Skill.md`

**Folder naming:**
- ✅ Use kebab-case: `notion-project-setup`
- ❌ No spaces: `Notion Project Setup`
- ❌ No underscores: `notion_project_setup`
- ❌ No capitals: `NotionProjectSetup`

**No README.md inside skill folder:**
- All documentation goes in SKILL.md or references/
- Use repo-level README for GitHub distribution only

**Recommended structure:**
```
your-skill-name/
├── SKILL.md              # Required
├── scripts/              # Optional - executable code
├── references/           # Optional - documentation
└── assets/              # Optional - templates, etc.
```

---

## YAML Frontmatter Best Practices

### Required Fields

```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

### Field Requirements

**name (required):**
- kebab-case only
- Must match folder name
- No "claude" or "anthropic" prefix (reserved)

**description (required):**
- **MUST include BOTH:**
  - What the skill does
  - When to use it (trigger conditions)
- Under 1024 characters
- No XML tags (< or >)
- Include specific trigger phrases users would say
- Mention file types if relevant

**Optional fields:**
- `license`: MIT, Apache-2.0, etc.
- `compatibility`: Environment requirements (1-500 chars)
- `allowed-tools`: Restrict tool access (e.g., `"mcp__ahrefs__*"`)
- `metadata`: Custom key-value pairs (author, version, mcp-server)

### Description Examples

✅ **Good - Specific and actionable:**
```yaml
description: Analyzes Figma design files and generates developer handoff
documentation. Use when user uploads .fig files, asks for "design specs",
"component documentation", or "design-to-code handoff".
```

✅ **Good - Includes trigger phrases:**
```yaml
description: Manages Linear project workflows including sprint planning,
task creation, and status tracking. Use when user mentions "sprint",
"Linear tasks", "project planning", or asks to "create tickets".
```

❌ **Bad - Too vague:**
```yaml
description: Helps with projects.
```

❌ **Bad - Missing triggers:**
```yaml
description: Creates sophisticated multi-page documentation systems.
```

---

## Writing Effective Instructions

### Recommended SKILL.md Structure

```markdown
---
name: your-skill
description: [What + When]
---

# Your Skill Name

## Instructions

### Step 1: [First Major Step]
Clear explanation of what happens.

Example:
```bash
python scripts/fetch_data.py --project-id PROJECT_ID
```
Expected output: [describe what success looks like]

### Step 2: [Next Step]
[Continue...]

## Examples

Example 1: [common scenario]
User says: "Set up a new marketing campaign"
Actions:
1. Fetch existing campaigns via MCP
2. Create new campaign with provided parameters
Result: Campaign created with confirmation link

## Troubleshooting

Error: [Common error message]
Cause: [Why it happens]
Solution: [How to fix]
```

### Be Specific and Actionable

✅ **Good:**
```markdown
Run `python scripts/validate.py --input {filename}` to check data format.

If validation fails, common issues include:
- Missing required fields (add them to the CSV)
- Invalid date formats (use YYYY-MM-DD)
```

❌ **Bad:**
```markdown
Validate the data before proceeding.
```

### Include Error Handling

```markdown
## Common Issues

### MCP Connection Failed
If you see "Connection refused":
1. Verify MCP server is running: Check Settings > Extensions
2. Confirm API key is valid
3. Try reconnecting: Settings > Extensions > [Your Service] > Reconnect
```

### Reference Bundled Resources Clearly

```markdown
Before writing queries, consult `references/api-patterns.md` for:
- Rate limiting guidance
- Pagination patterns
- Error codes and handling
```

### Use Progressive Disclosure

- Keep SKILL.md focused on core instructions
- Move detailed documentation to `references/`
- Link to reference files rather than inlining everything

---

## Planning and Design

### Start with Use Cases

Before writing any code, identify 2-3 concrete use cases.

**Good use case definition:**
```
Use Case: Project Sprint Planning
Trigger: User says "help me plan this sprint" or "create sprint tasks"
Steps:
1. Fetch current project status from Linear (via MCP)
2. Analyze team velocity and capacity
3. Suggest task prioritization
4. Create tasks in Linear with proper labels and estimates
Result: Fully planned sprint with tasks created
```

### Common Skill Categories

1. **Document & Asset Creation**
   - Creating consistent output (documents, designs, code)
   - Uses Claude's built-in capabilities
   - Example: frontend-design skill

2. **Workflow Automation**
   - Multi-step processes with consistent methodology
   - May coordinate multiple MCP servers
   - Example: skill-creator skill

3. **MCP Enhancement**
   - Workflow guidance for MCP tool access
   - Embeds domain expertise
   - Example: sentry-code-review skill

### Define Success Criteria

**Quantitative metrics:**
- Skill triggers on 90%+ of relevant queries
- Completes workflow in X tool calls (less than baseline)
- 0 failed API calls per workflow

**Qualitative metrics:**
- Users don't need to prompt about next steps
- Workflows complete without user correction
- Consistent results across sessions

---

## Testing Best Practices

### Testing Approach

**1. Triggering tests**
Goal: Ensure skill loads at right times

Test cases:
- ✅ Triggers on obvious tasks
- ✅ Triggers on paraphrased requests
- ❌ Doesn't trigger on unrelated topics

Example:
```
Should trigger:
- "Help me set up a new ProjectHub workspace"
- "I need to create a project in ProjectHub"
- "Initialize a ProjectHub project for Q4 planning"

Should NOT trigger:
- "What's the weather in San Francisco?"
- "Help me write Python code"
```

**2. Functional tests**
Goal: Verify correct outputs

Test cases:
- Valid outputs generated
- API calls succeed
- Error handling works
- Edge cases covered

**3. Performance comparison**
Goal: Prove skill improves results vs. baseline

Compare:
- Without skill: back-and-forth messages, failed API calls, tokens consumed
- With skill: automatic execution, minimal clarifications, successful API calls

### Pro Tip: Iterate on Single Task First

Most effective approach:
1. Iterate on a single challenging task until Claude succeeds
2. Extract the winning approach into a skill
3. Then expand to multiple test cases for coverage

**This leverages Claude's in-context learning and provides faster signal than broad testing.**

### Using skill-creator

The skill-creator skill can help you:
- Generate skills from natural language descriptions
- Review and flag common issues
- Suggest test cases
- Iterate on improvements

Usage:
```
"Use the skill-creator skill to help me build a skill for [your use case]"
```

### Iteration Based on Feedback

**Undertriggering signals:**
- Skill doesn't load when it should
- Users manually enabling it
- Solution: Add more detail and trigger phrases to description

**Overtriggering signals:**
- Skill loads for irrelevant queries
- Users disabling it
- Solution: Add negative triggers, be more specific

**Execution issues:**
- Inconsistent results
- API call failures
- Solution: Improve instructions, add error handling

---

## Common Patterns

### Pattern 1: Sequential Workflow Orchestration

Use when: Multi-step processes in specific order

Key techniques:
- Explicit step ordering
- Dependencies between steps
- Validation at each stage
- Rollback instructions for failures

### Pattern 2: Multi-MCP Coordination

Use when: Workflows span multiple services

Key techniques:
- Clear phase separation
- Data passing between MCPs
- Validation before next phase
- Centralized error handling

### Pattern 3: Iterative Refinement

Use when: Output quality improves with iteration

Key techniques:
- Explicit quality criteria
- Iterative improvement
- Validation scripts
- Know when to stop iterating

### Pattern 4: Context-Aware Tool Selection

Use when: Same outcome, different tools depending on context

Key techniques:
- Clear decision criteria
- Fallback options
- Transparency about choices

### Pattern 5: Domain-Specific Intelligence

Use when: Skill adds specialized knowledge beyond tool access

Key techniques:
- Domain expertise embedded in logic
- Compliance/validation before action
- Comprehensive documentation
- Clear governance

---

## Troubleshooting

### Skill Won't Upload

**Error: "Could not find SKILL.md in uploaded folder"**
- Cause: File not named exactly SKILL.md
- Solution: Rename to SKILL.md (case-sensitive)

**Error: "Invalid frontmatter"**
- Cause: YAML formatting issue
- Solution: Ensure `---` delimiters at start and end, proper indentation

**Error: "Invalid skill name"**
- Cause: Name has spaces or capitals
- Solution: Use kebab-case only

### Skill Doesn't Trigger

**Symptom:** Skill never loads automatically

Fix:
1. Revise description field to include trigger phrases
2. Make it less generic
3. Include specific tasks users would say

Debugging approach:
Ask Claude: "When would you use the [skill name] skill?"
Claude will quote the description back - adjust based on what's missing.

### Skill Triggers Too Often

**Solutions:**

1. Add negative triggers:
```yaml
description: Advanced data analysis for CSV files. Use for statistical
modeling, regression, clustering. Do NOT use for simple data exploration
(use data-viz skill instead).
```

2. Be more specific:
```yaml
# Too broad
description: Processes documents

# More specific
description: Processes PDF legal documents for contract review
```

### MCP Connection Issues

**Checklist:**
1. Verify MCP server is connected (Settings > Extensions)
2. Check authentication (API keys valid, not expired)
3. Test MCP independently without skill
4. Verify tool names are correct and case-sensitive

### Instructions Not Followed

**Common causes:**

1. **Instructions too verbose**
   - Keep concise, use bullet points
   - Move detailed reference to separate files

2. **Instructions buried**
   - Put critical instructions at top
   - Use `## Important` or `## Critical` headers

3. **Ambiguous language**
   ```markdown
   ❌ Bad: Make sure to validate things properly

   ✅ Good:
   CRITICAL: Before calling create_project, verify:
   - Project name is non-empty
   - At least one team member assigned
   - Start date is not in the past
   ```

4. **Model "laziness"**
   - Add explicit encouragement in instructions:
   ```markdown
   ## Performance Notes
   - Take your time to do this thoroughly
   - Quality is more important than speed
   - Do not skip validation steps
   ```
   - Note: Adding this to user prompts is more effective than in SKILL.md

**Advanced technique:** For critical validations, bundle a script that performs checks programmatically rather than relying on language instructions. Code is deterministic; language interpretation isn't.

### Large Context Issues

**Symptom:** Skill seems slow or responses degraded

**Solutions:**
1. Optimize SKILL.md size (keep under 5,000 words)
2. Move detailed docs to references/
3. Reduce enabled skills (evaluate if >20-50 enabled simultaneously)

---

## Distribution Best Practices

### Current Approach (2026)

**For Individual Users:**
1. Download skill folder
2. Zip the folder
3. Upload to Claude.ai via Settings > Capabilities > Skills
4. Or place in Claude Code skills directory

**For Organizations:**
- Admins can deploy skills workspace-wide
- Automatic updates
- Centralized management

### Recommended Distribution

**1. Host on GitHub:**
- Public repo for open-source skills
- Clear README with installation instructions
- Example usage and screenshots

**2. Link from MCP Documentation:**
- Explain value of using both together
- Provide quick-start guide

**3. Create Installation Guide:**
```markdown
## Installing the [Your Service] Skill

1. Download the skill:
   - Clone repo: `git clone https://github.com/yourcompany/skills`
   - Or download ZIP from Releases

2. Install in Claude:
   - Open Claude.ai > Settings > Skills
   - Click "Upload skill"
   - Select the skill folder (zipped)

3. Enable the skill:
   - Toggle on the [Your Service] skill
   - Ensure your MCP server is connected

4. Test:
   - Ask Claude: "Set up a new project in [Your Service]"
```

### Positioning Your Skill

**Focus on outcomes, not features:**

✅ **Good:**
```
The ProjectHub skill enables teams to set up complete project workspaces
in seconds—including pages, databases, and templates—instead of spending
30 minutes on manual setup.
```

❌ **Bad:**
```
The ProjectHub skill is a folder containing YAML frontmatter and Markdown
instructions that calls our MCP server tools.
```

**Highlight the MCP + Skills story:**
```
Our MCP server gives Claude access to your Linear projects. Our skills
teach Claude your team's sprint planning workflow. Together, they enable
AI-powered project management.
```

---

## Quick Checklist

### Before You Start
- [ ] Identified 2-3 concrete use cases
- [ ] Tools identified (built-in or MCP)
- [ ] Reviewed example skills
- [ ] Planned folder structure

### During Development
- [ ] Folder named in kebab-case
- [ ] SKILL.md file exists (exact spelling)
- [ ] YAML frontmatter has `---` delimiters
- [ ] `name` field: kebab-case, no spaces, no capitals
- [ ] `description` includes WHAT and WHEN
- [ ] No XML tags (< >) anywhere
- [ ] Instructions are clear and actionable
- [ ] Error handling included
- [ ] Examples provided
- [ ] References clearly linked

### Before Upload
- [ ] Tested triggering on obvious tasks
- [ ] Tested triggering on paraphrased requests
- [ ] Verified doesn't trigger on unrelated topics
- [ ] Functional tests pass
- [ ] Tool integration works (if applicable)
- [ ] Compressed as .zip file

### After Upload
- [ ] Test in real conversations
- [ ] Monitor for under/over-triggering
- [ ] Collect user feedback
- [ ] Iterate on description and instructions
- [ ] Update version in metadata

---

## Key Insights for MCP Builders

### Why Skills Matter for MCP

**Without skills:**
- Users connect your MCP but don't know what to do next
- Support tickets asking "how do I do X"
- Each conversation starts from scratch
- Inconsistent results
- Users blame your connector when issue is workflow guidance

**With skills:**
- Pre-built workflows activate automatically
- Consistent, reliable tool usage
- Best practices embedded
- Lower learning curve

### The Kitchen Analogy

- **MCP provides the kitchen:** Tools, ingredients, equipment (connectivity)
- **Skills provide the recipes:** Step-by-step instructions (knowledge)
- **Together:** Users accomplish complex tasks without figuring out every step

---

## Resources

**Official Documentation:**
- [Skills Documentation](https://docs.anthropic.com/en/docs/build-with-claude/skills)
- [API Reference](https://docs.anthropic.com/en/api/)
- [MCP Documentation](https://modelcontextprotocol.io/)

**Example Skills:**
- [GitHub: anthropics/skills](https://github.com/anthropics/skills)
- [Partner Skills Directory](https://claude.com/skills)

**Tools:**
- skill-creator skill (built into Claude.ai)
- Use: "Help me build a skill using skill-creator"

**Support:**
- [Claude Developers Discord](https://discord.gg/claude-dev)
- [GitHub Issues: anthropics/skills/issues](https://github.com/anthropics/skills/issues)

---

*Last updated: 2026-02-11*
*Source: The Complete Guide to Building Skills for Claude (Anthropic)*
