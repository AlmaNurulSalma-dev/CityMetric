from playwright.sync_api import sync_playwright
import time

OUT = r"C:\Users\kinet\OneDrive\Documents\PROJECT-ALMAAA\CityMetric\output"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 900})

    # ── Overview ──────────────────────────────────────────────────────────────
    page.goto("http://localhost:8501")
    page.wait_for_selector('[data-testid="stAppViewContainer"]', timeout=25000)
    time.sleep(5)
    page.screenshot(path=f"{OUT}/screenshot_overview.png")
    print("Saved: screenshot_overview.png")

    # ── World Map ─────────────────────────────────────────────────────────────
    page.get_by_text("World Map").click()
    time.sleep(5)
    page.screenshot(path=f"{OUT}/screenshot_map.png")
    print("Saved: screenshot_map.png")

    # ── Cluster Analysis ──────────────────────────────────────────────────────
    page.get_by_text("Cluster Analysis").click()
    time.sleep(3)
    page.screenshot(path=f"{OUT}/screenshot_clusters.png")
    print("Saved: screenshot_clusters.png")

    # ── City Comparison ───────────────────────────────────────────────────────
    page.get_by_text("City Comparison").click()
    time.sleep(3)
    page.screenshot(path=f"{OUT}/screenshot_comparison.png")
    print("Saved: screenshot_comparison.png")

    browser.close()
    print("Done.")
