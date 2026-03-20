# CLAUDE.md

## Project overview

Personal academic website for Rickard Brännvall, hosted on GitHub Pages at `rickardbrannvall.github.io`.

## Structure

- `index.html` — Landing page: biography, profile links, 3 most recent news items, recent projects
- `news/index.html` — Full chronological news & updates (newest first), LinkedIn-post style items
- `papers/index.html` — Full publication list with supplementary material links
- `cartoon.jpg` — Profile image
- `poster/` — Conference posters (PDF/PNG)

## Conventions

- Plain HTML/CSS, no build tools or frameworks
- Inline `<style>` block per page
- Simple navigation: blue links at top of each page (Home, News & Updates, Papers)
- Papers split into two thematic sections: "Privacy-Preserving ML and Health Data" and "Edge Data Centers and Other Topics"
- Papers listed in reverse chronological order within each section
- News items in reverse chronological order; front page shows only 3 most recent
- HTML entities used for special characters (e.g. `&ndash;`, `&mdash;`, `&ldquo;`, `&rdquo;`)
- Profile links: LinkedIn, RISE, ResearchGate, Google Scholar, ORCID
