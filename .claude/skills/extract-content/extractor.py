#!/usr/bin/env python3
"""
Ahrefs Blog Content Extractor

Extracts article content and metadata from Ahrefs blog URLs.
Uses curl + Python parsing (WebFetch fails due to JS rendering).

Usage:
    python3 extractor.py <url> <output_dir>

Example:
    python3 extractor.py https://ahrefs.com/blog/keyword-research/ ./update-pipeline/1-extracted/
"""

import re
import html as html_lib
import subprocess
import sys
from datetime import date
from pathlib import Path


def fetch_html(url: str) -> str:
    """Fetch HTML content using curl."""
    result = subprocess.run(
        ['curl', '-s', '-L', url],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Failed to fetch URL: {result.stderr}")
    return result.stdout


def clean_text(text: str) -> str:
    """Remove HTML tags and clean whitespace."""
    text = re.sub(r'<[^>]+>', '', text)
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def html_to_markdown(html_content: str) -> str:
    """Convert HTML content to markdown."""
    md = html_content

    # Remove script, style, noscript
    md = re.sub(r'<script[^>]*>.*?</script>', '', md, flags=re.DOTALL)
    md = re.sub(r'<style[^>]*>.*?</style>', '', md, flags=re.DOTALL)
    md = re.sub(r'<noscript>.*?</noscript>', '', md, flags=re.DOTALL)

    # Handle headings
    def heading_replace(level):
        def replacer(m):
            text = clean_text(m.group(1))
            return f'\n{"#" * level} {text}\n'
        return replacer

    md = re.sub(r'<h1[^>]*>(.*?)</h1>', heading_replace(1), md, flags=re.DOTALL)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', heading_replace(2), md, flags=re.DOTALL)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', heading_replace(3), md, flags=re.DOTALL)
    md = re.sub(r'<h4[^>]*>(.*?)</h4>', heading_replace(4), md, flags=re.DOTALL)

    # Handle links
    md = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f'[{clean_text(m.group(2))}]({m.group(1)})',
        md, flags=re.DOTALL
    )

    # Handle images (data-src for lazy loaded)
    md = re.sub(r'<img[^>]*data-src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)', md)
    md = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)', md)

    # Handle lists
    md = re.sub(
        r'<li[^>]*>(.*?)</li>',
        lambda m: f'\n- {clean_text(m.group(1))}',
        md, flags=re.DOTALL
    )
    md = re.sub(r'</?[uo]l[^>]*>', '', md)

    # Handle bold/italic
    md = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<b>(.*?)</b>', r'**\1**', md, flags=re.DOTALL)
    md = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', md, flags=re.DOTALL)

    # Handle blockquotes
    md = re.sub(
        r'<blockquote[^>]*>(.*?)</blockquote>',
        lambda m: '\n> ' + clean_text(m.group(1)) + '\n',
        md, flags=re.DOTALL
    )

    # Handle paragraphs
    md = re.sub(
        r'<p[^>]*>(.*?)</p>',
        lambda m: f'\n{clean_text(m.group(1))}\n',
        md, flags=re.DOTALL
    )

    # Remove remaining HTML tags
    md = re.sub(r'<[^>]+>', '', md)

    # Unescape HTML entities
    md = html_lib.unescape(md)

    # Clean up whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = re.sub(r' {2,}', ' ', md)

    return md.strip()


def extract_metadata(html: str) -> dict:
    """Extract metadata from HTML."""
    metadata = {}

    # Title
    title = re.search(r'<title>([^<]+)</title>', html)
    metadata['title'] = clean_text(title.group(1)) if title else 'Unknown'

    # Description
    desc = re.search(r'<meta name="description" content="([^"]+)"', html)
    metadata['description'] = html_lib.unescape(desc.group(1)) if desc else 'Not found'

    # Canonical URL
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    metadata['canonical'] = canonical.group(1) if canonical else 'Unknown'

    # Published date
    pub_date = re.search(r'"datePublished":"([^"]+)"', html)
    metadata['published'] = pub_date.group(1)[:10] if pub_date else 'Unknown'

    # Modified date
    mod_date = re.search(r'"dateModified":"([^"]+)"', html)
    metadata['modified'] = mod_date.group(1)[:10] if mod_date else 'Unknown'

    # Author (from Ahrefs blog author link)
    author_link = re.search(r'href="https://ahrefs\.com/blog/author/([^/]+)/"', html)
    metadata['author'] = author_link.group(1).replace('-', ' ').title() if author_link else 'Unknown'

    return metadata


def extract_content(html: str) -> str:
    """Extract main article content."""
    # Find content area
    content_match = re.search(
        r'class="[^"]*(?:entry-content|post-content)[^"]*"[^>]*>(.*?)(?=<div class="(?:sidebar|related|comments|footer|share|widget))',
        html, re.DOTALL | re.IGNORECASE
    )

    if not content_match:
        return ''

    raw_content = content_match.group(1)

    # Remove non-content elements (Ahrefs blog specific)
    raw_content = re.sub(
        r'<div[^>]*class="[^"]*author[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>',
        '', raw_content, flags=re.DOTALL
    )
    raw_content = re.sub(
        r'<div[^>]*class="[^"]*table-of-contents[^"]*"[^>]*>.*?</div>',
        '', raw_content, flags=re.DOTALL
    )
    raw_content = re.sub(
        r'<div[^>]*class="[^"]*performance[^"]*"[^>]*>.*?</div>',
        '', raw_content, flags=re.DOTALL
    )
    # Remove article performance widget
    raw_content = re.sub(
        r'<div[^>]*class="[^"]*article-performance[^"]*"[^>]*>.*?</div>\s*</div>',
        '', raw_content, flags=re.DOTALL
    )
    # Remove email subscription form
    raw_content = re.sub(
        r'<div[^>]*class="[^"]*subscription[^"]*"[^>]*>.*?</div>',
        '', raw_content, flags=re.DOTALL
    )
    raw_content = re.sub(
        r'<form[^>]*>.*?</form>',
        '', raw_content, flags=re.DOTALL
    )

    return raw_content


def extract_structure(raw_content: str) -> list:
    """Extract heading structure from raw HTML content."""
    heading_positions = []

    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', raw_content, re.DOTALL):
        heading_positions.append((m.start(), 2, clean_text(m.group(1))))
    for m in re.finditer(r'<h3[^>]*>(.*?)</h3>', raw_content, re.DOTALL):
        heading_positions.append((m.start(), 3, clean_text(m.group(1))))

    heading_positions.sort(key=lambda x: x[0])

    structure_lines = []
    for pos, level, text in heading_positions:
        if text and len(text) > 2:
            indent = '  ' * (level - 2)
            structure_lines.append(f"{indent}- {text}")

    return structure_lines


def count_stats(markdown: str) -> dict:
    """Count various statistics from markdown content."""
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', markdown)
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', markdown)

    return {
        'word_count': len(markdown.split()),
        'images': len(images),
        'internal_links': len([l for l in links if 'ahrefs.com' in l[1]]),
        'external_links': len([l for l in links if 'ahrefs.com' not in l[1]]),
        'h2_count': len(re.findall(r'^## ', markdown, re.MULTILINE)),
        'h3_count': len(re.findall(r'^### ', markdown, re.MULTILINE)),
    }


def extract_article(url: str, output_dir: str) -> str:
    """Main extraction function."""
    # Fetch HTML
    html = fetch_html(url)

    # Extract metadata
    metadata = extract_metadata(html)

    # Extract raw content
    raw_content = extract_content(html)

    # Extract structure before converting
    structure = extract_structure(raw_content)

    # Convert to markdown
    markdown_content = html_to_markdown(raw_content)

    # Remove intro cruft (performance data, TOC) - find first real paragraph
    # Look for common article start patterns
    intro_patterns = [
        r'^.*?(?=\w{20,})',  # Skip until substantial text
    ]

    # Clean up intro cruft from markdown
    # Remove "Article PerformanceData..." section
    markdown_content = re.sub(
        r'^Article PerformanceData.*?Contents\s*',
        '', markdown_content, flags=re.DOTALL
    )
    # Remove "Get the week's best marketing content..." subscription text
    markdown_content = re.sub(
        r'Get the week\'s best marketing content.*?human:\s*',
        '', markdown_content, flags=re.DOTALL | re.IGNORECASE
    )

    # Clean up footer cruft
    # Remove "Keep Learning" related posts section
    markdown_content = re.sub(
        r"This post's estimated monthly organic search traffic\..*$",
        '', markdown_content, flags=re.DOTALL
    )
    # Remove trailing "Keep Learning" section
    markdown_content = re.sub(
        r'Keep Learning\s*\[.*$',
        '', markdown_content, flags=re.DOTALL
    )
    # Remove trailing "Copy link" and Article Performance section
    markdown_content = re.sub(
        r'\n\s*Copy link\s*Article PerformanceData.*$',
        '', markdown_content, flags=re.DOTALL
    )
    # Remove just "Copy link" at end
    markdown_content = re.sub(
        r'\n\s*Copy link\s*$',
        '', markdown_content, flags=re.DOTALL
    )

    # Clean leading/trailing whitespace
    markdown_content = markdown_content.strip()

    # Count stats
    stats = count_stats(markdown_content)

    # Generate output
    output = f"""# {metadata['title']}

**Source URL**: {metadata['canonical']}
**Extracted**: {date.today()}
**Published**: {metadata['published']}
**Last Modified**: {metadata['modified']}
**Author**: {metadata['author']}
**Word Count**: {stats['word_count']}
**Meta Description**: {metadata['description']}

---

## Content

{markdown_content}

---

## Extraction Notes

- **Images found**: {stats['images']} images (URLs preserved, not downloaded)
- **Internal links**: {stats['internal_links']} links to ahrefs.com
- **External links**: {stats['external_links']} links to other domains
- **H2 sections**: {stats['h2_count']}
- **H3 sections**: {stats['h3_count']}

---

## Original Structure

{chr(10).join(structure)}
"""

    # Derive slug and save
    slug = metadata['canonical'].rstrip('/').split('/')[-1]
    output_path = Path(output_dir) / f"{slug}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        f.write(output)

    return str(output_path)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 extractor.py <url> <output_dir>")
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2]

    output_path = extract_article(url, output_dir)
    print(f"Extracted to: {output_path}")
