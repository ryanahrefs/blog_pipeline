---
name: ahrefs-urls
description: Construct Ahrefs app URLs for Site Explorer reports
---

# Ahrefs URL Construction

Construct URLs to access Ahrefs Site Explorer reports in the web app.

## Base URL

`https://app.ahrefs.com/v2-site-explorer`

## URL Patterns

There are two patterns for how `mode` is passed:

**Pattern A — mode in path** (most reports):
```
/v2-site-explorer/{report}/{mode}?target={target}
```

**Pattern B — mode in query** (v3 paid reports, site-structure, page-inspect):
```
/v2-site-explorer/{report}?mode={mode}&target={target}
```

## Mode Values

| Mode | Meaning |
|------|---------|
| `subdomains` | Domain + all subdomains (default for domain analysis) |
| `exact` | Single URL only |
| `prefix` | All URLs under a path |
| `domain` | Root domain without subdomains (rarely used) |

## Report Slugs

**Backlinks:**

| Report | Slug | Mode in | Example |
|--------|------|---------|---------|
| Backlinks | `backlinks` | path | `/v2-site-explorer/backlinks/subdomains?target=example.com` |
| Referring Domains | `refdomains` | path | `/v2-site-explorer/refdomains/subdomains?target=example.com` |
| Anchors | `anchors` | query | `/v2-site-explorer/anchors?target=example.com` |
| Broken Backlinks | `broken-backlinks` | query | `/v2-site-explorer/broken-backlinks?target=example.com` |
| Best by Links | `best-by-links` | query | `/v2-site-explorer/best-by-links?target=example.com` |

**Organic Search:**

| Report | Slug | Mode in | Example |
|--------|------|---------|---------|
| Organic Keywords | `organic-keywords` | path | `/v2-site-explorer/organic-keywords/subdomains?country=us&target=example.com` |
| Top Pages | `top-pages` | path | `/v2-site-explorer/top-pages/subdomains?target=example.com` |
| Organic Competitors | `organic-competitors` | path | `/v2-site-explorer/organic-competitors/subdomains?country=us&target=example.com` |
| Site Structure | `site-structure` | query | `/v2-site-explorer/site-structure?country=us&mode=subdomains&target=example.com` |

**Paid Search:**

| Report | Slug | Mode in | Example |
|--------|------|---------|---------|
| Ads (text ad copy) | `ads-v3` | query | `/v2-site-explorer/ads-v3?mode=subdomains&target=example.com` |
| Paid Pages (landing pages) | `paid-pages-v3` | query | `/v2-site-explorer/paid-pages-v3?mode=subdomains&country=de&target=example.com` |
| Paid Keywords | `paid-keywords-v3` | query | `/v2-site-explorer/paid-keywords-v3?mode=subdomains&target=example.com` |

## Common Query Parameters

| Parameter | Values | Notes |
|-----------|--------|-------|
| `target` | domain or URL | Required in all reports |
| `country` | lowercase ISO code: `us`, `fr`, `de`, or `all` | For organic/paid reports. Note: lowercase in URLs, uppercase in API/MCP |
| `mode` | `subdomains`, `exact`, `prefix`, `domain` | When in query string (Pattern B) |
| `compareDate` | `dontCompare` or `YYYY-MM-DD` | Date comparison |
| `volume_type` | `monthly` | Search volume mode |

## Examples

**Organic keywords for a domain in the UK:**
```
https://app.ahrefs.com/v2-site-explorer/organic-keywords/subdomains?country=uk&target=example.com
```

**Backlinks for a specific page:**
```
https://app.ahrefs.com/v2-site-explorer/backlinks/exact?target=https://example.com/blog/post/
```

**Referring domains for a domain:**
```
https://app.ahrefs.com/v2-site-explorer/refdomains/subdomains?target=example.com
```
