# Palette's Journal

## 2025-05-18 - Accessibility First
**Learning:** This codebase lacked basic accessibility features like "Skip to main content" and unique IDs, which are fundamental for keyboard and screen reader users.
**Action:** Always check for unique IDs and skip links in the observation phase.

## 2025-05-18 - Skip Link Target Verification
**Learning:** When adding a skip link, always verify the target ID exists in the file, as reviewers might miss it if it's outside the diff context.
**Action:** Explicitly check for target ID existence before or during the PR to avoid confusion.
