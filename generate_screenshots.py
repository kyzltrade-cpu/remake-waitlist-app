from playwright.sync_api import sync_playwright
import os

sizes = {
    "6.5-inch": {"width": 1284, "height": 2778},
    "5.5-inch": {"width": 1242, "height": 2208}
}

base_url = "file://" + os.path.abspath("appstore_gen.html")

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

with sync_playwright() as p:
    browser = p.chromium.launch()
    for size_name, dim in sizes.items():
        page = browser.new_page(viewport={"width": dim["width"], "height": dim["height"]})
        for i in range(4):
            page.goto(f"{base_url}?i={i}")
            # wait for fonts and images to load
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500) # give it a moment to render fonts
            
            output_path = f"screenshots/{size_name}_{i+1}.png"
            page.screenshot(path=output_path)
            print(f"Generated {output_path}")
    browser.close()
