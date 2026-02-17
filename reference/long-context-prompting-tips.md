# Long Context Prompting Tips

**Source**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips
**Saved**: 2026-02-17

---

> While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models in the extended-thinking-tips documentation.

Claude's extended context window (200K tokens for Claude 3 models) enables handling complex, data-rich tasks. This guide will help you leverage this power effectively.

## Essential tips for long context prompts

### 1. Put longform data at the top

Place your long documents and inputs (~20K+ tokens) near the top of your prompt, above your query, instructions, and examples. This can significantly improve Claude's performance across all models.

> Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs.

### 2. Structure document content and metadata with XML tags

When using multiple documents, wrap each document in `<document>` tags with `<document_content>` and `<source>` (and other metadata) subtags for clarity.

**Example multi-document structure:**

```xml
<documents>
  <document index="1">
    <source>annual_report_2023.pdf</source>
    <document_content>
      {{ANNUAL_REPORT}}
    </document_content>
  </document>
  <document index="2">
    <source>competitor_analysis_q2.xlsx</source>
    <document_content>
      {{COMPETITOR_ANALYSIS}}
    </document_content>
  </document>
</documents>

Analyze the annual report and competitor analysis. Identify strategic advantages and recommend Q3 focus areas.
```

### 3. Ground responses in quotes

For long document tasks, ask Claude to quote relevant parts of the documents first before carrying out its task. This helps Claude cut through the "noise" of the rest of the document's contents.

**Example quote extraction:**

```xml
You are an AI physician's assistant. Your task is to help doctors diagnose possible patient illnesses.

<documents>
  <document index="1">
    <source>patient_symptoms.txt</source>
    <document_content>
      {{PATIENT_SYMPTOMS}}
    </document_content>
  </document>
  <document index="2">
    <source>patient_records.txt</source>
    <document_content>
      {{PATIENT_RECORDS}}
    </document_content>
  </document>
  <document index="3">
    <source>patient01_appt_history.txt</source>
    <document_content>
      {{PATIENT01_APPOINTMENT_HISTORY}}
    </document_content>
  </document>
</documents>

Find quotes from the patient records and appointment history that are relevant to diagnosing the patient's reported symptoms. Place these in <quotes> tags. Then, based on these quotes, list all information that would help the doctor diagnose the patient's symptoms. Place your diagnostic information in <info> tags.
```

---

## Related Resources

- **Prompt library**: Curated selection of prompts for various tasks and use cases
- **GitHub prompting tutorial**: Example-filled tutorial covering prompt engineering concepts
- **Google Sheets prompting tutorial**: Lighter weight interactive spreadsheet version
