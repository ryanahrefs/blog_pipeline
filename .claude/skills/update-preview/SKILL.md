---
name: update-preview
description: Generate a diff preview showing proposed changes from update audits
argument-hint: [slug]
allowed-tools: Read, Write, Bash
---

# Update Preview Skill

Generate an HTML diff preview that shows the original article alongside proposed changes from the update audits, with changes highlighted.

## Input

**Article slug** - The slug identifier (e.g., `programmatic-seo`)

The skill reads from:
- `./update-pipeline/1-extracted/[slug].md` - Original content
- `./update-pipeline/2-update-claims/[slug].md` - Claims audit
- `./update-pipeline/3-update-ahrefs-mentions/[slug].md` - Ahrefs mentions audit
- `./update-pipeline/4-update-topic-gaps/[slug].md` - Topic gaps audit

---

## Workflow

### Phase 1: Load Source Files

1. **Read the original extracted content** from `1-extracted/[slug].md`
2. **Read all available audit files** (some may not exist):
   - `2-update-claims/[slug].md`
   - `3-update-ahrefs-mentions/[slug].md`
   - `4-update-topic-gaps/[slug].md`

### Phase 2: Parse Changes

Extract all proposed changes from the audit files:

#### From Claims Audit

Look for `UPDATE_STAT` and `REFRESH_SOURCE` entries:

```markdown
**Original:**
```
[exact text to find]
```

**Suggested replacement:**
```
[new text]
```
```

Parse into change objects:
```json
{
  "type": "claim",
  "category": "UPDATE_STAT",
  "original": "exact text from article",
  "replacement": "new text with updated stat",
  "reason": "Pinterest user count updated from 450M to 498M"
}
```

#### From Ahrefs Mentions Audit

Look for recommended additions:

```markdown
**Relevant section:**
> [quote from article]

**Suggested insertion:**
> "[new text to add]"
```

Parse into:
```json
{
  "type": "ahrefs_mention",
  "category": "NEW_FEATURE",
  "location": "after section quote",
  "insertion": "new text to add",
  "reason": "Brand Radar launched since publication"
}
```

#### From Topic Gaps Audit

Look for critical/significant gaps:

```markdown
### 1. [Topic Name]

**Recommended action:** Add new H2 section

**Suggested heading:** "[heading text]"

**Placement:** After "[existing section name]"
```

Parse into:
```json
{
  "type": "topic_gap",
  "category": "CRITICAL",
  "heading": "New Section Title",
  "placement": "after existing section",
  "estimated_words": 300
}
```

### Phase 3: Generate Diff HTML

Create an HTML file with three panels:

1. **Left Panel: Original Content**
   - Full article as extracted
   - Sections that will change highlighted in yellow
   - Click to scroll to corresponding change

2. **Right Panel: Proposed Changes**
   - Same structure as original
   - Deletions shown with ~~strikethrough~~ and red background
   - Additions shown with green background
   - New sections shown with green left border

3. **Bottom Panel: Change Summary**
   - List of all changes grouped by type
   - Click to jump to location in diff view
   - Accept/reject checkboxes (visual only, for review)

---

## HTML Template Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Preview: [Article Title]</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
        }

        .header {
            background: #1a1a2e;
            color: white;
            padding: 20px;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header h1 { font-size: 1.5rem; margin-bottom: 8px; }
        .header .meta { font-size: 0.875rem; opacity: 0.8; }

        /* Review Progress */
        .review-progress {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid rgba(255,255,255,0.2);
        }

        .progress-counts {
            display: flex;
            gap: 12px;
            font-size: 0.875rem;
        }

        .count-accepted { color: #28a745; }
        .count-rejected { color: #dc3545; }
        .count-pending { color: #ffc107; }

        .progress-bar {
            flex: 1;
            height: 8px;
            background: rgba(255,255,255,0.2);
            border-radius: 4px;
            overflow: hidden;
            display: flex;
        }

        .progress-fill {
            height: 100%;
            transition: width 0.3s ease;
        }

        .accepted-fill { background: #28a745; width: 0%; }
        .rejected-fill { background: #dc3545; width: 0%; }

        .btn-export {
            padding: 8px 16px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: opacity 0.2s;
        }

        .btn-export:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .btn-export:not(:disabled):hover {
            background: #218838;
        }

        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            padding: 20px;
            max-width: 1800px;
            margin: 0 auto;
        }

        .panel {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .panel-header {
            background: #f8f9fa;
            padding: 12px 16px;
            border-bottom: 1px solid #e9ecef;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .panel-header .badge {
            font-size: 0.75rem;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 500;
        }

        .badge-original { background: #e9ecef; color: #495057; }
        .badge-updated { background: #d4edda; color: #155724; }

        .panel-content {
            padding: 20px;
            max-height: calc(100vh - 200px);
            overflow-y: auto;
            line-height: 1.6;
        }

        /* Typography */
        .panel-content h1 { font-size: 1.75rem; margin: 0 0 16px 0; }
        .panel-content h2 { font-size: 1.25rem; margin: 24px 0 12px 0; color: #1a1a2e; }
        .panel-content h3 { font-size: 1rem; margin: 16px 0 8px 0; }
        .panel-content p { margin: 0 0 12px 0; }
        .panel-content ul, .panel-content ol { margin: 0 0 12px 20px; }
        .panel-content li { margin: 4px 0; }

        /* Diff highlighting */
        .diff-delete {
            background: #ffeef0;
            text-decoration: line-through;
            color: #cb2431;
            padding: 2px 4px;
            border-radius: 3px;
        }

        .diff-insert {
            background: #e6ffed;
            color: #22863a;
            padding: 2px 4px;
            border-radius: 3px;
        }

        .diff-modified {
            background: #fff5b1;
            border-left: 3px solid #f9c513;
            padding-left: 12px;
            margin-left: -15px;
        }

        .diff-new-section {
            background: #f0fff4;
            border-left: 4px solid #28a745;
            padding: 16px;
            margin: 16px 0;
            border-radius: 0 8px 8px 0;
        }

        .diff-new-section::before {
            content: "NEW SECTION";
            display: block;
            font-size: 0.75rem;
            font-weight: 600;
            color: #28a745;
            margin-bottom: 8px;
            letter-spacing: 0.05em;
        }

        /* Change annotations */
        .change-annotation {
            display: inline-block;
            font-size: 0.7rem;
            padding: 2px 6px;
            border-radius: 3px;
            margin-left: 8px;
            vertical-align: middle;
            font-weight: 500;
        }

        .annotation-claim { background: #fff3cd; color: #856404; }
        .annotation-ahrefs { background: #cce5ff; color: #004085; }
        .annotation-topic { background: #d4edda; color: #155724; }

        /* Summary panel */
        .summary-panel {
            grid-column: 1 / -1;
            margin-top: 20px;
        }

        .change-list {
            display: grid;
            gap: 12px;
        }

        .change-item {
            display: grid;
            grid-template-columns: auto 1fr auto;
            gap: 12px;
            padding: 12px;
            background: #f8f9fa;
            border-radius: 6px;
            align-items: start;
        }

        .change-type {
            font-size: 0.75rem;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: 4px;
            white-space: nowrap;
        }

        .type-claim { background: #fff3cd; color: #856404; }
        .type-ahrefs { background: #cce5ff; color: #004085; }
        .type-topic { background: #d4edda; color: #155724; }

        .change-details { font-size: 0.875rem; }
        .change-details .change-title { display: block; margin-bottom: 4px; }
        .change-details .change-reason { color: #6c757d; font-size: 0.8rem; display: block; margin-top: 8px; }

        .change-content {
            background: #f8f9fa;
            padding: 8px;
            border-radius: 4px;
            margin: 8px 0;
            font-size: 0.8rem;
        }

        .original-text {
            color: #cb2431;
            margin-bottom: 4px;
        }

        .original-text::before {
            content: "- ";
            font-weight: bold;
        }

        .replacement-text {
            color: #22863a;
        }

        .replacement-text::before {
            content: "+ ";
            font-weight: bold;
        }

        .change-actions {
            display: flex;
            gap: 8px;
        }

        .change-actions button {
            padding: 6px 12px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .btn-accept { background: #28a745; color: white; }
        .btn-reject { background: #dc3545; color: white; }
        .btn-accept:hover { background: #218838; }
        .btn-reject:hover { background: #c82333; }

        /* Decision states */
        .change-item.accepted {
            border-left: 4px solid #28a745;
            background: #f0fff4;
        }

        .change-item.accepted .btn-accept {
            background: #155724;
        }

        .change-item.accepted .btn-accept::before {
            content: "✓ ";
        }

        .change-item.accepted button:disabled {
            opacity: 0.6;
            cursor: default;
        }

        .change-item.rejected {
            border-left: 4px solid #dc3545;
            opacity: 0.6;
        }

        .change-item.rejected .change-details strong {
            text-decoration: line-through;
        }

        .change-item.rejected .btn-reject {
            background: #721c24;
        }

        .change-item.rejected .btn-reject::before {
            content: "✗ ";
        }

        .change-item.rejected button:disabled {
            opacity: 0.6;
            cursor: default;
        }

        .btn-reset {
            background: transparent;
            color: #6c757d;
            font-size: 0.75rem;
            padding: 4px 8px;
            border: 1px solid #6c757d;
            display: none;
        }

        .change-item.accepted .btn-reset,
        .change-item.rejected .btn-reset {
            display: inline-block;
        }

        .btn-reset:hover {
            background: #f8f9fa;
        }

        /* Sync scrolling indicator */
        .scroll-sync {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #1a1a2e;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.875rem;
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Update Preview: {{TITLE}}</h1>
        <div class="meta">
            <span>Original: {{ORIGINAL_DATE}}</span> ·
            <span>{{TOTAL_CHANGES}} proposed changes</span> ·
            <span>Generated: {{PREVIEW_DATE}}</span>
        </div>
        <div class="review-progress">
            <div class="progress-counts">
                <span class="count-accepted">0 accepted</span>
                <span class="count-rejected">0 rejected</span>
                <span class="count-pending">{{TOTAL_CHANGES}} pending</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill accepted-fill"></div>
                <div class="progress-fill rejected-fill"></div>
            </div>
            <button class="btn-export" disabled>Download Update Plan</button>
        </div>
    </div>

    <div class="container">
        <div class="panel">
            <div class="panel-header">
                <span>Original Content</span>
                <span class="badge badge-original">As Published</span>
            </div>
            <div class="panel-content" id="original">
                {{ORIGINAL_CONTENT}}
            </div>
        </div>

        <div class="panel">
            <div class="panel-header">
                <span>With Proposed Changes</span>
                <span class="badge badge-updated">{{TOTAL_CHANGES}} Changes</span>
            </div>
            <div class="panel-content" id="updated">
                {{UPDATED_CONTENT}}
            </div>
        </div>

        <div class="panel summary-panel">
            <div class="panel-header">
                <span>Change Summary</span>
            </div>
            <div class="panel-content">
                <div class="change-list">
                    {{CHANGE_LIST}}
                </div>
            </div>
        </div>
    </div>

    <div class="scroll-sync">Scroll synced</div>

    <script>
        // Sync scrolling between panels
        const original = document.getElementById('original');
        const updated = document.getElementById('updated');
        let isSyncing = false;

        function syncScroll(source, target) {
            if (isSyncing) return;
            isSyncing = true;
            const percentage = source.scrollTop / (source.scrollHeight - source.clientHeight);
            target.scrollTop = percentage * (target.scrollHeight - target.clientHeight);
            setTimeout(() => isSyncing = false, 50);
        }

        original.addEventListener('scroll', () => syncScroll(original, updated));
        updated.addEventListener('scroll', () => syncScroll(updated, original));

        // ========================================
        // Interactive Accept/Reject Functionality
        // ========================================

        const STORAGE_KEY = 'update-preview-decisions-{{SLUG}}';

        // Load decisions from localStorage
        function loadDecisions() {
            try {
                return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
            } catch (e) {
                return {};
            }
        }

        // Save a decision to localStorage
        function saveDecision(changeId, decision) {
            const decisions = loadDecisions();
            if (decision === null) {
                delete decisions[changeId];
            } else {
                decisions[changeId] = decision;
            }
            localStorage.setItem(STORAGE_KEY, JSON.stringify(decisions));
            updateUI();
        }

        // Update all UI elements based on current decisions
        function updateUI() {
            const decisions = loadDecisions();
            const cards = document.querySelectorAll('.change-item');
            let accepted = 0, rejected = 0, pending = 0;

            cards.forEach(card => {
                const id = card.dataset.changeId;
                const decision = decisions[id];
                const acceptBtn = card.querySelector('.btn-accept');
                const rejectBtn = card.querySelector('.btn-reject');

                // Reset state
                card.classList.remove('accepted', 'rejected');
                acceptBtn.disabled = false;
                rejectBtn.disabled = false;

                if (decision === 'accepted') {
                    card.classList.add('accepted');
                    acceptBtn.disabled = true;
                    rejectBtn.disabled = true;
                    accepted++;
                } else if (decision === 'rejected') {
                    card.classList.add('rejected');
                    acceptBtn.disabled = true;
                    rejectBtn.disabled = true;
                    rejected++;
                } else {
                    pending++;
                }
            });

            // Update progress counts
            document.querySelector('.count-accepted').textContent = `${accepted} accepted`;
            document.querySelector('.count-rejected').textContent = `${rejected} rejected`;
            document.querySelector('.count-pending').textContent = `${pending} pending`;

            // Update progress bar
            const total = cards.length;
            const acceptedWidth = (accepted / total) * 100;
            const rejectedWidth = (rejected / total) * 100;
            document.querySelector('.accepted-fill').style.width = `${acceptedWidth}%`;
            document.querySelector('.rejected-fill').style.width = `${rejectedWidth}%`;

            // Enable/disable export button
            const exportBtn = document.querySelector('.btn-export');
            exportBtn.disabled = pending > 0;
        }

        // Set up button click handlers
        document.querySelectorAll('.change-item').forEach(card => {
            const acceptBtn = card.querySelector('.btn-accept');
            const rejectBtn = card.querySelector('.btn-reject');
            const resetBtn = card.querySelector('.btn-reset');
            const changeId = card.dataset.changeId;

            acceptBtn.addEventListener('click', () => {
                saveDecision(changeId, 'accepted');
            });

            rejectBtn.addEventListener('click', () => {
                saveDecision(changeId, 'rejected');
            });

            resetBtn.addEventListener('click', () => {
                saveDecision(changeId, null);
            });
        });

        // Export decisions to markdown file
        function exportDecisions() {
            const decisions = loadDecisions();
            const accepted = [];
            const rejected = [];

            document.querySelectorAll('.change-item').forEach(card => {
                const id = card.dataset.changeId;
                const data = {
                    type: card.dataset.changeType || 'UNKNOWN',
                    title: card.querySelector('.change-title')?.textContent || '',
                    original: card.querySelector('.original-text')?.textContent || '',
                    replacement: card.querySelector('.replacement-text')?.textContent || '',
                    reason: card.querySelector('.change-reason')?.textContent || ''
                };

                if (decisions[id] === 'accepted') {
                    accepted.push(data);
                } else if (decisions[id] === 'rejected') {
                    rejected.push(data);
                }
            });

            const markdown = generateMarkdown(accepted, rejected);
            downloadFile('{{SLUG}}-update-plan.md', markdown);
        }

        function generateMarkdown(accepted, rejected) {
            const date = new Date().toISOString().split('T')[0];
            let md = `# Update Plan: {{SLUG}}

Generated: ${date}
Source: /update-pipeline/5-update-preview/{{SLUG}}.html

`;

            if (accepted.length > 0) {
                md += `## Accepted Changes (${accepted.length})\n\n`;
                accepted.forEach((change, i) => {
                    md += `### ${i + 1}. ${change.title}\n`;
                    md += `**Type:** ${change.type}\n`;
                    if (change.original) {
                        md += `**Original:** ${change.original.replace(/^- /, '')}\n`;
                    }
                    if (change.replacement) {
                        md += `**Replacement:** ${change.replacement.replace(/^\+ /, '')}\n`;
                    }
                    if (change.reason) {
                        md += `**Reason:** ${change.reason}\n`;
                    }
                    md += '\n';
                });
            }

            if (rejected.length > 0) {
                md += `## Rejected Changes (${rejected.length})\n\n`;
                rejected.forEach((change, i) => {
                    md += `### ${i + 1}. ${change.title}\n`;
                    md += `**Type:** ${change.type}\n`;
                    md += `**Reason for rejection:** [Add your reason]\n\n`;
                });
            }

            return md;
        }

        function downloadFile(filename, content) {
            const blob = new Blob([content], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        // Set up export button
        document.querySelector('.btn-export').addEventListener('click', exportDecisions);

        // Initialize UI on page load
        updateUI();
    </script>
</body>
</html>
```

---

## Output Generation

### Step 1: Convert Original Content

Convert the extracted markdown to HTML, preserving structure.

### Step 2: Apply Changes to Updated Panel

For each change from the audits:

**For claim updates (UPDATE_STAT, REFRESH_SOURCE):**
```html
<!-- In original panel -->
<span class="diff-modified">Pinterest has over 450 million monthly active users</span>

<!-- In updated panel -->
<span class="diff-delete">450 million</span>
<span class="diff-insert">498 million</span>
<span class="change-annotation annotation-claim">Updated stat</span>
```

**For new Ahrefs mentions:**
```html
<!-- In updated panel, after relevant section -->
<p class="diff-insert">
    You can track your programmatic pages using Ahrefs' Rank Tracker...
    <span class="change-annotation annotation-ahrefs">New feature</span>
</p>
```

**For topic gap additions:**
```html
<!-- In updated panel -->
<div class="diff-new-section">
    <h2>Common Programmatic SEO Mistakes</h2>
    <p>[Placeholder content for new section - ~300 words recommended]</p>
</div>
```

### Step 3: Generate Change List

Create summary items for each change:

```html
<div class="change-item" data-change-id="claims-1" data-change-type="UPDATE_STAT">
    <span class="change-type type-claim">CLAIM</span>
    <div class="change-details">
        <strong class="change-title">Pinterest user count outdated</strong>
        <div class="change-content">
            <div class="original-text">Pinterest has over 450 million monthly active users</div>
            <div class="replacement-text">Pinterest has over 498 million monthly active users</div>
        </div>
        <span class="change-reason">Updated from 450M to 498M based on Q4 2025 earnings</span>
    </div>
    <div class="change-actions">
        <button class="btn-accept">Accept</button>
        <button class="btn-reject">Reject</button>
        <button class="btn-reset">Reset</button>
    </div>
</div>
```

**Change ID Format:**
- Claims: `claims-1`, `claims-2`, etc.
- Ahrefs mentions: `ahrefs-1`, `ahrefs-2`, etc.
- Topic gaps: `topics-1`, `topics-2`, etc.

---

## Template Placeholders

When generating the HTML, replace these placeholders:

| Placeholder | Value |
|-------------|-------|
| `{{TITLE}}` | Article title from extracted content |
| `{{SLUG}}` | Kebab-case slug (e.g., `programmatic-seo`) |
| `{{ORIGINAL_DATE}}` | Last-Modified date from extracted content |
| `{{PREVIEW_DATE}}` | Current date (YYYY-MM-DD) |
| `{{TOTAL_CHANGES}}` | Count of all changes from audits |
| `{{ORIGINAL_CONTENT}}` | HTML-converted original content |
| `{{UPDATED_CONTENT}}` | HTML with diff highlighting applied |
| `{{CHANGE_LIST}}` | Generated change-item cards |

---

## Output

Save to `./update-pipeline/5-update-preview/[slug].html`

Then open in browser:
```bash
open ./update-pipeline/5-update-preview/[slug].html
```

---

## Example Usage

```
/update-preview programmatic-seo
```

**Reads from:**
- `./update-pipeline/1-extracted/programmatic-seo.md`
- `./update-pipeline/2-update-claims/programmatic-seo.md`
- `./update-pipeline/3-update-ahrefs-mentions/programmatic-seo.md`
- `./update-pipeline/4-update-topic-gaps/programmatic-seo.md`

**Creates:**
- `./update-pipeline/5-update-preview/programmatic-seo.html`

---

## Features

### Synchronized Scrolling
Both panels scroll together, keeping the same relative position so you can compare changes in context.

### Change Highlighting

| Change Type | Original Panel | Updated Panel |
|-------------|----------------|---------------|
| Stat update | Yellow highlight | Strikethrough + green insertion |
| Source refresh | Yellow highlight | Updated link |
| New Ahrefs mention | — | Green highlighted paragraph |
| New section | — | Green-bordered block |
| Content removal | Yellow highlight | Red strikethrough |

### Interactive Accept/Reject

Each change card supports:
- **Accept button:** Mark change for inclusion (green left border, checkmark)
- **Reject button:** Mark change for exclusion (red left border, strikethrough)
- **Reset button:** Clear decision and return to pending state

Decisions persist via localStorage (`update-preview-decisions-[slug]`) so you can:
- Review changes across multiple sessions
- Refresh the page without losing progress
- Come back later to finish reviewing

### Progress Tracking

Sticky header shows:
- Count of accepted, rejected, and pending changes
- Progress bar with green (accepted) and red (rejected) fills
- Export button (enabled only when all changes reviewed)

### Export Update Plan

When all changes are reviewed, click "Download Update Plan" to generate a markdown file:

```markdown
# Update Plan: programmatic-seo

Generated: 2026-03-03
Source: /update-pipeline/5-update-preview/programmatic-seo.html

## Accepted Changes (3)

### 1. Zapier stats (4x growth)
**Type:** UPDATE_STAT
**Original:** "800,632 pages" and "306,000 monthly traffic"
**Replacement:** "21,867 pages" and "1,270,496 monthly traffic"
**Reason:** Updated to current Ahrefs data

## Rejected Changes (1)

### 1. Nomadlist example removal
**Type:** UPDATE_STAT
**Reason for rejection:** [Add your reason]
```

This file can be used as input for a future `/update-draft` skill.

---

## Handling Missing Audits

If an audit file doesn't exist, skip it gracefully:
- Note in the preview header which audits were included
- Only show changes from available audits
- Don't fail if some audits are missing

---

## Quality Checklist

| Check | Requirement |
|-------|-------------|
| Original loads | Extracted content renders correctly |
| Changes applied | All audit changes reflected in updated panel |
| Diff highlighting | Additions green, deletions red |
| Scroll sync | Panels scroll together |
| Change count | Header shows correct total |
| Opens in browser | Auto-opens after generation |
| Accept/Reject | Buttons update card state and progress |
| Persistence | Decisions survive page refresh (localStorage) |
| Progress bar | Fills as changes are reviewed |
| Export enabled | Button activates when 0 pending |
| Export output | Downloads valid markdown file |
