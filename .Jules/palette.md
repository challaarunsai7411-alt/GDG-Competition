# Palette's Journal

## 2025-05-18 - Accessibility First
**Learning:** This codebase lacked basic accessibility features like "Skip to main content" and unique IDs, which are fundamental for keyboard and screen reader users.
**Action:** Always check for unique IDs and skip links in the observation phase.

## 2025-05-19 - Defensive Coding for UI Widgets
**Learning:** The image carousel broke completely because the data array (descriptions) was shorter than the image list. In static sites without type safety, implicit dependencies between DOM elements and JS data structures are fragile.
**Action:** When working with vanilla JS widgets, verify that data arrays match the DOM element count to prevent runtime crashes.
