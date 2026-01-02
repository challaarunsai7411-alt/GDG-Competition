# Palette's Journal

## 2025-05-18 - Accessibility First
**Learning:** This codebase lacked basic accessibility features like "Skip to main content" and unique IDs, which are fundamental for keyboard and screen reader users.
**Action:** Always check for unique IDs and skip links in the observation phase.

## 2025-10-26 - Secure and Accessible External Links
**Learning:** External links (`target="_blank"`) were missing both security attributes (`rel="noopener noreferrer"`) and screen reader context (`visually-hidden` text). This is a common pattern in static sites.
**Action:** Standardize all external links to include security attributes and hidden helper text.
