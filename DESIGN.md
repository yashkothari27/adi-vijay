# Design System Document: The Curated Collage

## 1. Overview & Creative North Star

### Creative North Star: "The Editorial Curator"
This design system moves away from the rigid, sterile grids of traditional SaaS portfolios and embraces the expressive, high-energy world of editorial collage. It is designed to feel like a living mood board—a physical space where professional precision meets creative spontaneity. 

The system achieves a premium feel by balancing **"The Frame"** (clean, structured, high-end layouts inspired by modern web architecture) with **"The Soul"** (overlapping elements, handwritten annotations, and sticker-like components). By using intentional asymmetry and a sophisticated tonal palette, we ensure the portfolio feels like a custom-built gallery rather than a templated site.

---

## 2. Colors

The palette is anchored in a sophisticated "Soft Pink" foundation, providing a warmer, more human alternative to clinical whites or greys.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders for sectioning. Boundaries must be defined solely through background color shifts. Use `surface-container-low` (#faf2f4) sections against the main `background` (#fff7f9) to create structure. This creates an "organic break" that feels high-end and editorial.

### Surface Hierarchy & Nesting
Treat the interface as stacked sheets of fine paper.
*   **Base:** `surface` (#fff7f9)
*   **Sectioning:** `surface-container-low` (#faf2f4) for large layout blocks.
*   **Interactive Cards:** `surface-container-lowest` (#ffffff) to provide a "pop" of brightness.
*   **Nesting:** When placing a card inside a section, the card must always be at least one tier lighter than the section it sits upon.

### The "Glass & Gradient" Rule
To add visual "soul," use `primary` (#714aaa) to `primary-container` (#bd93f9) gradients for high-impact CTAs. For floating "sticker" elements or navigation overlays, utilize Glassmorphism:
*   **Background:** `surface` at 70% opacity.
*   **Effect:** `backdrop-filter: blur(12px)`.

---

## 3. Typography

The typography strategy relies on high-contrast scaling to mimic high-end fashion magazines.

*   **Display (Space Grotesk):** Bold and condensed. Used for massive, authoritative headers (e.g., "PORTFOLIO"). It should feel intentional and slightly "too big," breaking into the margins to create energy.
*   **Headline (Space Grotesk):** Used for project titles and section headers. High-contrast and impactful.
*   **Title (Plus Jakarta Sans):** A bridge between the display headers and the body. It provides a modern, clean framing for project metadata.
*   **Body (Plus Jakarta Sans):** Optimized for readability. Use `on_surface_variant` (#4a4451) for longer descriptions to reduce visual fatigue.
*   **Labels (Inter):** Small, all-caps, or utility text. These function as the "metadata" of the collage.

---

## 4. Elevation & Depth

### The Layering Principle
Depth is achieved through **Tonal Layering**. Instead of shadows, shift the surface token. A white card (`surface-container-lowest`) on a soft pink background (`surface`) provides all the "lift" needed for a clean, modern look.

### Ambient Shadows
When an element must "float" (like a sticker or a hover-state card):
*   **Blur:** 40px – 60px.
*   **Opacity:** 4% – 8%.
*   **Color:** Use a tinted shadow (`#4a4451` at low alpha) rather than pure black to maintain the warmth of the palette.

### The "Ghost Border" Fallback
If accessibility requires a container boundary, use a "Ghost Border":
*   **Token:** `outline-variant` (#ccc3d3).
*   **Opacity:** 15%.
*   **Width:** 1px.

---

## 5. Components

### Project Cards
*   **Styling:** No borders. Use `surface-container-lowest` (#ffffff).
*   **Hover Effect:** Scale 102%, increase `Ambient Shadow` to 10%, and reveal a "handwritten" annotation (e.g., "View Case Study") in `tertiary` (#5c6300).
*   **Layout:** Mix aspect ratios (16:9 vs 4:5) within the same grid to reinforce the collage aesthetic.

### Buttons
*   **Primary:** Solid `primary` (#714aaa) with `on_primary` text. High rounding (`rounded-xl`).
*   **Secondary:** Glassmorphic background with a `Ghost Border`.
*   **Tertiary:** Text-only with a `secondary` (#006e2b) underline that mimics a highlighter stroke.

### Stickers & Annotations
*   **The Sticker:** Small, high-contrast chips using `secondary_container` (#55fe7e) or `tertiary_fixed` (#e1ea7e). These should be slightly rotated (2-3 degrees) to break the grid.
*   **Handwritten Notes:** Use a script-style font or SVG paths for arrows and notes pointing to specific UI details in project showcases.

### Experience Timeline
*   **Structure:** Avoid a vertical line. Use a series of `surface-container-high` blocks that "step" down the page, using `Spacing 16` to create significant breathing room between eras.

---

## 6. Do's and Don'ts

### Do
*   **Do** overlap elements. Let a project image bleed into a text block or a "sticker" sit on the edge of a card.
*   **Do** use asymmetrical margins. A project description might be offset by `Spacing 10` on the left but `Spacing 20` on the right.
*   **Do** use color to categorize. Use `lavender` for Branding, `teal` for UI/UX, and `yellow` for Research.

### Don't
*   **Don't** use 100% black (#000000). Always use `on_background` (#1e1b1c) to keep the look editorial and soft.
*   **Don't** align everything to a center axis. This system thrives on the "edge-to-edge" tension found in magazine layouts.
*   **Don't** use drop shadows on text. Keep typography crisp; let the background color shifts do the work of creating hierarchy.