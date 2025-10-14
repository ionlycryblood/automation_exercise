import pytest
from playwright.sync_api import sync_playwright

from pages.mainpage import MainPage


#import allure

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.on("console", lambda msg: print(">>", msg.text))
        page.on("pageerror", lambda exc: print("!!", exc))
        yield page
        browser.close()


@pytest.fixture()
def load(page):
    main_page = MainPage(page)
    page.goto('https://automationexercise.com/',
        wait_until="domcontentloaded",
        timeout=60000
    )
    main_page.should_be_loaded()
    return main_page
