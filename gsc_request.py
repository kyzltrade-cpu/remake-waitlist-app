import asyncio
import sys
import subprocess
import os
from playwright.async_api import async_playwright

async def launch_chrome():
    print("Stopping any existing Google Chrome instances...")
    subprocess.run("killall 'Google Chrome' || pkill -9 -f 'Google Chrome'", shell=True, capture_output=True)
    await asyncio.sleep(2)
    
    print("Launching headful Google Chrome on port 9222...")
    cmd_str = "'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=/Users/kyzl/chrome_remake_profile"
    subprocess.Popen(cmd_str, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    await asyncio.sleep(5)

async def check_and_request_indexing():
    # Make sure Chrome is running and responding
    try:
        import urllib.request
        urllib.request.urlopen("http://127.0.0.1:9222/json/version", timeout=3)
        print("✅ Active Chrome session detected on port 9222.")
    except Exception:
        print("⚠️ Chrome not responding on port 9222. Restarting...")
        await launch_chrome()
    
    browser = None
    page = None
    try:
        print("Connecting Playwright over CDP...")
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            context = browser.contexts[0]
            page = context.pages[0] if context.pages else await context.new_page()
            
            # CRITICAL: Set large viewport size to expand collapsed GSC search bar!
            print("Setting viewport size to 1920x1080...")
            await page.set_viewport_size({"width": 1920, "height": 1080})
            
            print("Navigating to Google Search Console...")
            await page.goto("https://search.google.com/search-console?resource_id=sc-domain:remake.beauty")
            await page.wait_for_load_state("load")
            await asyncio.sleep(10) # Wait for page and lazy widgets to stabilize
            
            print("Taking dashboard screenshot...")
            await page.screenshot(path="/Users/kyzl/remake-waitlist-app/gsc_dashboard.png")
            
            inspect_input = page.locator('input[aria-label*="Inspect any URL"]').first
            if await inspect_input.count() > 0:
                print("Found GSC URL search input! Typing URL...")
                await inspect_input.click()
                await page.keyboard.press("Meta+A")
                await page.keyboard.press("Backspace")
                await inspect_input.fill("https://remake.beauty/")
                await page.keyboard.press("Enter")
                print("Submitted URL for inspection. Waiting for GSC to fetch indexing data (approx 25-35s)...")
                await asyncio.sleep(35)
                
                await page.screenshot(path="/Users/kyzl/remake-waitlist-app/gsc_inspection_result.png")
                html_content = await page.content()
                
                # Check indexing status (English / Chinese fallback)
                is_on_google = False
                if "url is on google" in html_content.lower() or "網址已在 Google" in html_content or "is on google" in html_content.lower():
                    is_on_google = True
                    print("✅ The URL https://remake.beauty/ IS ALREADY on Google index!")
                else:
                    print("⚠️ The URL https://remake.beauty/ is currently NOT on Google index.")
                
                # Check if we can click the "Request Indexing" / "要求建立索引" button
                print("Looking for 'Request indexing' or '要求建立索引' button...")
                result = await page.evaluate("""() => {
                    const el = Array.from(document.querySelectorAll('div, span, button')).find(
                        el => {
                            const txt = el.textContent.trim().toLowerCase();
                            return txt === 'request indexing' || txt === '要求建立索引';
                        }
                    );
                    if (el) {
                        el.click();
                        return 'Success: Clicked Request Indexing!';
                    }
                    return 'Error: Request indexing button not found!';
                }""")
                print(f"Click Result: {result}")
                
                if "Success" in result:
                    print("Waiting for indexing request test and submission (60-120s)...")
                    for i in range(15):
                        await asyncio.sleep(10)
                        await page.screenshot(path=f"/Users/kyzl/remake-waitlist-app/gsc_submission_loading_{i}.png")
                        new_content = await page.content()
                        if "indexing requested" in new_content.lower() or "got it" in new_content.lower() or "已要求建立索引" in new_content or "我知道了" in new_content or "提交" in new_content:
                            print("🎉 Indexing successfully requested!")
                            # Automatically dismiss the success modal popup
                            await page.evaluate("""() => {
                                const btn = Array.from(document.querySelectorAll('div, span, button')).find(
                                    el => el.textContent.trim() === 'Got it' || el.textContent.trim() === '我知道了' || el.textContent.trim() === 'Dismiss' || el.textContent.trim() === '關閉'
                                );
                                if (btn) btn.click();
                            }""")
                            break
                
            else:
                print("❌ Inspection search box not visible or could not be found.")
                
            print("Checking GSC Sitemaps status to see if remake.beauty sitemap is submitted...")
            await page.goto("https://search.google.com/search-console/sitemaps?resource_id=sc-domain:remake.beauty")
            await page.wait_for_load_state("load")
            await asyncio.sleep(5)
            await page.screenshot(path="/Users/kyzl/remake-waitlist-app/gsc_sitemaps_status.png")
            print("Took sitemaps status screenshot!")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        if page:
            try:
                await page.screenshot(path="/Users/kyzl/remake-waitlist-app/gsc_error.png")
            except Exception:
                pass
    finally:
        if browser:
            try:
                await browser.close()
            except Exception:
                pass

if __name__ == "__main__":
    asyncio.run(check_and_request_indexing())
