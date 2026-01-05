import os
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

def verify_fixes():
    # Setup paths
    repo_root = Path(os.getcwd())
    events_path = repo_root / "GDC competition" / "events.html"
    comp_path = repo_root / "GDC competition" / "comp.html"

    screenshot_dir = Path("/home/jules/verification")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        print("--- Verifying Carousel Fix in events.html ---")
        page.goto(events_path.as_uri())

        # Click next 4 times to get to the previously crashing index
        # Use a more robust selector: text="Next"
        next_btn = page.get_by_role("button", name="Next")
        for i in range(4):
            next_btn.click()
            page.wait_for_timeout(500) # Wait for transition

        # Assert the description updated correctly (showing the fix works)
        desc_title = page.locator(".description h2")
        expect(desc_title).to_have_text("Community Q&A")
        print("Carousel navigated successfully to 'Community Q&A'")

        # Screenshot the carousel
        page.screenshot(path=screenshot_dir / "carousel_fix.png")
        print(f"Screenshot saved to {screenshot_dir / 'carousel_fix.png'}")

        print("\n--- Verifying Typo Fix in comp.html ---")
        page.goto(comp_path.as_uri())

        # Assert the navbar brand text
        navbar_brand = page.locator(".navbar-brand")
        expect(navbar_brand).to_contain_text("Google Developer Groups")
        print("Navbar text verified: 'Google Developer Groups'")

        # Screenshot the navbar
        navbar = page.locator("nav.navbar")
        navbar.screenshot(path=screenshot_dir / "navbar_typo_fix.png")
        print(f"Screenshot saved to {screenshot_dir / 'navbar_typo_fix.png'}")

        browser.close()

if __name__ == "__main__":
    verify_fixes()
