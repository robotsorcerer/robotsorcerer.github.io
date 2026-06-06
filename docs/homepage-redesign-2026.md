# Homepage Redesign Session — June 2026

## Overview

This session implemented a comprehensive visual redesign of scriptedonachip.com's homepage, transforming from a traditional static layout to a modern, animated experience with rich graphics, carousel animations, and dynamic overlays.

## Key Changes

### 1. Bio Snippet Section Beautification

**File**: `_includes/cv.md` (lines 1–29)

**Changes**:
- Added full-width background image (`/assets/research-bg.jpg`) with dark gradient overlay
- Implemented two-column layout for first paragraph with custom SVG dawn illustration
- SVG features:
  - Gradient background (sunrise colors: #ff6b35 → #f7931e → #e8f3fb)
  - Sun circle with opacity
  - Mountain landscape silhouette
  - Cyclist figure
  - 60×50px inline SVG, flex-shrink: 0
- Applied consistent text styling: white color, text-shadow for readability, 0.88–0.9rem font-size
- Second paragraph maintains layout without image, full width

**Styling**:
- Background: `url(/assets/research-bg.jpg) center/cover no-repeat`
- Overlay gradient: `linear-gradient(135deg, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.45) 50%, rgba(0,0,0,0.55) 100%)`
- Min-height: 280px, border-radius: 0.5rem
- Z-index layering: SVG and text at z-index 10 above gradient

### 2. Hero Section Restructuring

**File**: `index.md`

**Changes**:
- Replaced centered card layout with 1×4 column grid background image system
- Grid contains four research domain images:
  1. `wcm_radiation.jpg` (Weill Cornell Medicine)
  2. `lab_setup.jpg` (Laboratory setup)
  3. `amazon_warehouse.jpg` (Amazon robotics context)
  4. `surgical_robotics.jpg` (Surgical robotics domain)
- Overlaid hero content (photo, name, subtitle, chips, links) absolutely positioned at center
- Dark gradient overlay for text readability over images

**Content Styling**:
- Name ("Lekan Molu"): #FFB84D (golden accent), 2rem font-size, 700 weight, text-shadow
- Subtitle: White color, 600 weight, "Researcher · AI · Control · Autonomous Systems"
- Chips (AI, Autonomous Systems, Robotics, Control): 0.75rem font-size, 0.35rem 0.7rem padding, 0.3rem border-radius
- Links: Social media + RSS feed with icon styling

### 3. Featured News Sections with Animated Overlays

**File**: `_includes/cv.md`

Three featured news items added before the regular news feed loop:

#### Item 1: Starling Murmuration (May 29)
- **Style**: Two-column image layout side-by-side
- **Images**: `starlings_funnel.jpg`, `starlings_split.jpg`
- **Overlay**: Auto-scrolling text duplicated for seamless wrapping
- **Animation**: 20-second infinite loop, linear
- **Container**: Full-width section with custom scrolling text

#### Item 2: Robodiff Release (May 24)
- **Style**: Full-width GIF background
- **GIF**: `robodiff.gif` (extracted from YouTube video via ffmpeg)
- **Overlay**: Auto-scrolling text (18-second animation)
- **Logo**: WCM (Weill Cornell Medicine) SVG overlay in top-right corner, white background, static position
- **Layout**: Centered text on dark semi-transparent background

#### Item 3: IFAC/WCM Trauma (April 16)
- **Style**: Full-width GIF background
- **GIF**: `wcm_trauma.gif` (YouTube video extract, 2:59–3:20)
- **Overlay**: Auto-scrolling text (16-second animation)
- **Logo**: WCM SVG overlay (top-right, white background)

**Common Features**:
- Text duplicated in DOM for seamless wrapping in infinite animation
- Semi-transparent dark background for text readability
- Custom `@keyframes` for horizontal scrolling
- Gap spacing between duplicated text for breathing room

### 4. Bio-Timeline Transformation to Infinite Carousel

**File**: `_includes/cv.md` (lines 31–117)

**Transformation**:
- **Original**: Static 3-column grid layout
- **New**: Single-row infinite auto-scrolling carousel with manual scroll capability

**Implementation**:

**CSS** (lines 31–73):
```css
@keyframes bioScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

**Container Styling** (`.bio-timeline-scroll`):
- `overflow-x: auto; overflow-y: hidden`
- Custom scrollbar: 6px height
- Track: `var(--accent-soft)` (#e8f3fb)
- Thumb: `var(--accent)` (#1a6fa8), hover to `var(--accent-dark)` (#124e78)
- Border-radius: 3px

**Wrapper** (`.bio-timeline-wrapper`):
- Display: flex with 1.5rem gap
- Animation: `bioScroll 20s linear infinite`
- Pause on hover: `animation-play-state: paused`

**Item Styling** (`.bio-tl-item`):
- Fixed width: 320px (flex: 0 0 320px)
- Padding: 1.25rem
- Left border: 3px solid accent color
- Background: white (var(--card-bg))
- Box-shadow: subtle (0 2px 4px rgba(0,0,0,0.08))

**Timeline Entries** (11 total):
1. 2026–Present: Senior Research Scientist, Amazon IRG
2. 2025–Present: Researcher & Founder, Stealth Research Lab
3. 2021–2025: Senior Researcher, Microsoft Research Lab (NYC)
4. 2019–2021: Adjunct Faculty, Brandeis University
5. 2019–2021: Postdoctoral Researcher, UPenn (transferred from UChicago)
6. 2018: Research Intern (Robot Learning), Preferred Networks, Tokyo
7. 2016: Hardware Engineer IV, Amazon Robotics (Advanced Robotics Lab), MA
8. 2014–2019: PhD Student, University of Texas at Dallas + Visiting Student, UT Southwestern
9. 2011–2013: Student, University of Sheffield (Automatic Control)
10. 2009–2011: Supply Chain Manager, Coca-Cola Hellenic Bottling Company
11. Duplicate set of all 10 items for infinite loop seamlessness

**Key Details**:
- Items duplicated in HTML to allow seamless infinite scrolling
- Animation translates wrapper -50% (exactly to halfway point where duplicate begins)
- Manual scrollbar allows users to scroll and inspect any timeline entry
- Scrollbar wraps around infinitely via the duplicated item set
- Animation pauses on hover for accessibility and user control
- 20-second animation cycle for smooth, readable pacing

### 5. 2016 | 2018 Timeline Entry Split

**File**: `_includes/cv.md`

**Change**:
- **Original**: Single combined entry "2016 | 2018 Hardware Engineer, Amazon Robotics (Advanced Robotics Lab), MA | Research Intern (Robot Learning), Preferred Networks, Tokyo"
- **New**: Two separate `.bio-tl-item` cards:
  1. **2018**: Research Intern (Robot Learning), Preferred Networks, Tokyo
  2. **2016**: Hardware Engineer IV (Intern), Amazon Robotics (Advanced Robotics Lab), MA

**Rationale**: Improves readability in carousel format; each role gets dedicated visual emphasis and space.

### 6. Jekyll Hot-Reload Fix

**File**: `deploy.sh`

**Change**:
```bash
# Before:
bundle exec jekyll build && bundle exec jekyll serve --no-watch

# After:
bundle exec jekyll serve --force_polling
```

**Rationale**:
- `--no-watch` flag completely disables file watching, requiring server restart for any changes
- `--force_polling` enables polling-based file watching without hitting iNotify ulimit (common Linux limit issue)
- Allows static assets (CSS, JS, images) and templates to hot-reload during local development without server restart

## Design System Alignment

All changes maintain consistency with existing CSS variables:
- **Accent**: #1a6fa8 (primary interactive color)
- **Accent-dark**: #124e78 (hover state)
- **Accent-soft**: #e8f3fb (light background)
- **Background**: #f8f5f1 (page background)
- **Card-bg**: #ffffff (card background)
- **Text**: #2c2c2c (primary text)
- **Muted**: #6b7280 (secondary text)
- **Border**: #e2ddd8 (divider lines)
- **Nav-bg**: #1a2a40 (navbar background)

## Assets Required

- `/assets/research-bg.jpg` — Bio snippet background
- `/assets/wcm_radiation.jpg` — Hero column 1
- `/assets/lab_setup.jpg` — Hero column 2
- `/assets/amazon_warehouse.jpg` — Hero column 3
- `/assets/surgical_robotics.jpg` — Hero column 4
- `/assets/starlings_funnel.jpg` — Starling news item
- `/assets/starlings_split.jpg` — Starling news item
- `/assets/robodiff.gif` — Robodiff GIF background
- `/assets/wcm_trauma.gif` — IFAC/WCM trauma GIF

## Testing Checklist

- [ ] Hero section displays 1×4 grid with proper image positioning
- [ ] Hero content overlays correctly centered on images
- [ ] Bio snippet renders with SVG and gradient overlay
- [ ] Featured news items scroll text infinitely without jumping
- [ ] WCM logo overlays display correctly (static position)
- [ ] Bio-timeline carousel scrolls smoothly at 20 seconds
- [ ] Scrollbar visible and interactive underneath carousel
- [ ] Timeline pauses on hover
- [ ] 2016 and 2018 entries display as separate cards
- [ ] Responsive behavior on mobile (hero, timeline scaling)
- [ ] Jekyll hot-reload works: `./deploy.sh` picks up CSS and asset changes without restart

## Future Enhancements

- Add keyboard navigation to bio-timeline carousel (arrow keys)
- Implement touch/swipe gestures for mobile carousel interaction
- Add fade-in animations on page load
- Optimize GIF file sizes for faster load times
- Consider lazy-loading for large background images

## Session Timeline

- Beautified Bio Snippet with SVG graphics and gradient overlays
- Restructured hero banner to 1×4 column image layout with overlay pattern
- Created featured news sections with animated text and GIF backgrounds
- Transformed bio-timeline to infinite auto-scrolling carousel with scrollbar
- Split 2016|2018 timeline entry into two separate cards
- Fixed Jekyll file watching for hot-reload development workflow
