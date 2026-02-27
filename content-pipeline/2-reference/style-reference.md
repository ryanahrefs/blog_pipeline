# Style Reference Article

**Purpose**: Gold-standard example for voice, tone, and structure
**Updated**: 2026-02-17
**Source**: "What Is llms.txt, and Should You Care About It?" by Ryan Law (April 22, 2025)

---

## What Is llms.txt, and Should You Care About It?

Developers and marketers are being told to add llms.txt files to their sites to help large language models (LLMs) "understand" their content.

But what exactly is llms.txt, who's using it, and—more importantly—should you care?

### What is llms.txt?

llms.txt is a proposed standard for helping LLMs access and interpret structured content from websites. You can read the full proposal on llmstext.org.

In a nutshell, it's a text file designed to tell LLMs where to find the good stuff: API documentation, return policies, product taxonomies, and other context-rich resources. The goal is to remove ambiguity by giving language models a curated map of high-value content, so they don't have to guess what matters.

[SCREENSHOT: A screenshot from the proposed standard over on https://llmstxt.org/.]

In theory, this sounds like a good idea. We already use files like robots.txt and sitemap.xml to help search engines understand what's on a site and where to look. Why not apply the same logic to LLMs?

But importantly, no major LLM provider currently supports llms.txt. Not OpenAI. Not Anthropic. Not Google.

As I said in the intro, llms.txt is a proposed standard. I could also propose a standard (let's call it please-send-me-traffic-robot-overlords.txt), but unless the major LLM providers agree to use it, it's pretty meaningless.

That's where we're at with llms.txt: it's a speculative idea with no official adoption.

> **Don't sleep on robots.txt**
>
> llms.txt might not impact your visibility online, but robots.txt definitely does.
>
> You can use Ahrefs' Site Audit to monitor hundreds of common technical SEO issues, including problems with your robots.txt file that might seriously hamper your visibility (or even stop your site from being crawled).

### llms.txt example

Here's what an llms.txt file looks like in practice. This is a screenshot of Anthropic's actual llms.txt file:

[SCREENSHOT: Anthropic's llms.txt file]

At its core, llms.txt is a Markdown document (a kind of specially formatted text file). It uses H2 headers to organize links to key resources. Here's a sample structure you could use:

```markdown
# llms.txt
## Docs
- /api.md
A summary of API methods, authentication, rate limits, and example requests.
- /quickstart.md
A setup guide to help developers start using the platform quickly.
## Policies
- /terms.md
Legal terms outlining service usage.
- /returns.md
Information about return eligibility and processing.
## Products
- /catalog.md
A structured index of product categories, SKUs, and metadata.
- /sizing-guide.md
A reference guide for product sizing across categories.
```

You can make your own llms.txt in minutes:

1. Start with a basic Markdown file.
2. Use H2s to group resources by type.
3. Link to structured, markdown-friendly content.
4. Keep it updated.
5. Host it at your root domain: https://yourdomain.com/llms.txt

You can create it yourself or use a free llms.txt generator (like this one) to make it for you.

I've read about some developers also experimenting with LLM-specific metadata in their llms.txt files, like token budgets or preferred file formats (but there's no evidence that this is respected by crawlers or LLM models).

### Who's using it (if anyone)?

You can see a list of companies using llms.txt at directory.llmstxt.cloud—a community-maintained index of public llms.txt files.

Here are a few examples:

- **Mintlify**: Developer documentation platform.
- **Tinybird**: Real-time data APIs.
- **Cloudflare**: Lists performance and security docs.
- **Anthropic**: Publishes a full Markdown map of its API docs.

But what about the big players?

So far, no major LLM provider has formally adopted llms.txt as part of their crawler protocol:

- **OpenAI (GPTBot)**: Honors robots.txt but doesn't officially use llms.txt.
- **Anthropic (Claude)**: Publishes its own llms.txt, but doesn't state that its crawlers use the standard.
- **Google (Gemini/Bard)**: Uses robots.txt (via User-agent: Google-Extended) to manage AI crawl behavior, with no mention of llms.txt support.
- **Meta (LLaMA)**: No public crawler or guidance, and no indication of llms.txt usage.

This highlights an important point: creating an llms.txt is not the same as enforcing it in crawler behavior. Right now, most LLM vendors treat llms.txt as an interesting idea, and not something that they've agreed to prioritize and follow.

### So is llms.txt actually useful?

In my opinion, no, not yet.

There's no evidence that llms.txt improves AI retrieval, boosts traffic, or enhances model accuracy. And no provider has committed to parsing it.

But it's also very easy to set up. If you already have structured content like product pages or developer docs, compiling an llms.txt is trivial. It's a Markdown file, hosted on your own website. There might be no observed benefit, but there's also no risk. If LLMs do eventually follow it as a standard, there might be some small advantage to being early adopters.

I think llms.txt is gaining traction because we all want to influence LLM visibility, but we lack the tools to do it. So we latch onto ideas that feel like control.

But in my personal view, llms.txt is a solution in search of a problem. Search engines already crawl and understand your content using existing standards like robots.txt and sitemap.xml. LLMs use much of the same infrastructure.

As Google's John Mueller put it in a Reddit post recently:

> AFAIK none of the AI services have said they're using LLMs.TXT (and you can tell when you look at your server logs that they don't even check for it). To me, it's comparable to the keywords meta tag – this is what a site-owner claims their site is about … (Is the site really like that? well, you can check it. At that point, why not just check the site directly?)
>
> — John Mueller, Search Advocate, Google

Disagree with me, or want to share an example to the contrary? Message me on LinkedIn or X.

---

## Style Notes

This article exemplifies key patterns to replicate:

### Voice Markers
- **Casual first-person**: "As I said in the intro...", "In my opinion, no, not yet."
- **Sentence starters with conjunctions**: "But importantly...", "But what about the big players?"
- **Humor/wit**: "please-send-me-traffic-robot-overlords.txt"
- **Direct opinions stated as fact**: "llms.txt is a solution in search of a problem"

### BLUF Examples
- "llms.txt is a proposed standard for helping LLMs access and interpret structured content from websites." (Definition opener)
- "In my opinion, no, not yet." (Direct answer to section question)

### Transition Patterns
- Rhetorical questions: "Why not apply the same logic to LLMs?"
- "But" pivots: "But importantly, no major LLM provider currently supports llms.txt."
- Direct address: "But what about the big players?"

### Specificity Markers
- Named companies: OpenAI, Anthropic, Google, Cloudflare, Mintlify
- Named people with titles: "Google's John Mueller"
- Direct quotes from authoritative sources
- Numbered lists with concrete steps

### Anecdote Structure
- Setup → Context → Opinion → Evidence → Implication
- Example: The "I could also propose a standard" humor makes a point while being memorable

### CTA Pattern
- Conversational, invites disagreement: "Disagree with me, or want to share an example to the contrary? Message me on LinkedIn or X."

---

## Writing Rules

Beyond voice and style, follow these rules to avoid common draft issues:

### Replace Weasel Words with Specifics

Vague language sounds authoritative but says nothing. Always replace with concrete details.

| Weasel Phrase | Problem | Fix |
|---------------|---------|-----|
| "several benefits" | Which benefits? | List them: "analytics access, Rich Pin eligibility, and higher domain scores" |
| "significantly impact" | How much? What kind? | Be specific: "drive referral traffic and earn backlinks" |
| "drive results" | What results? | "increase organic traffic by 20%" |
| "best practices" | Says nothing | List the actual practices |
| "optimize your content" | How? | "add keywords to titles and compress images" |
| "leverage" | Corporate speak | "use" |
| "robust" / "comprehensive" | Meaningless | Describe what makes it strong or complete |

**Example from reference article:**
- NOT: "llms.txt provides several benefits for your site"
- YES: "llms.txt tells LLMs where to find API documentation, return policies, and product taxonomies"

### Define Jargon on First Use

Don't assume readers know technical terms. Define inline on first use.

**Formats:**
- Dash definition: "Open Graph tags—bits of code that tell platforms your page title and image—are required."
- Parenthetical: "Use long-tail keywords (longer, specific phrases like 'small bathroom ideas for apartments')."
- Follow-up: "You need Schema markup. This is structured data that helps search engines understand your content."

**Example from reference article:**
- "llms.txt is a Markdown document (a kind of specially formatted text file)"
- Defines "Markdown document" immediately for non-technical readers

### Avoid AI-Sounding Phrases

These patterns signal generic AI content. Never use them:

| Pattern | Why It's Bad |
|---------|--------------|
| "In today's digital landscape" | Empty preamble |
| "Let's dive in" | Generic filler |
| "Game-changer" / "Revolutionary" | Hyperbole without evidence |
| "Unlock the power of" | Marketing fluff |
| "Take X to the next level" | Vague promise |
| "This isn't X... it's Y" | Overused dramatic reveal |

**Instead:** State things directly. "Pinterest SEO works because Pinterest is a search engine" not "Pinterest SEO isn't just marketing... it's a game-changer that unlocks the power of visual discovery."
