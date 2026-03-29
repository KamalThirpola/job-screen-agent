from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://example.com")
    page.screenshot(path="screenshot.png")

    time.sleep(5)  # 👈 ये add करो

    browser.close()