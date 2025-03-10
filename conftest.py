import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """Launch a browser instance for the entire test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test with video recording enabled."""
    context = browser.new_context(
        record_video_dir="videos/",  # Save videos here
        record_video_size={"width": 1280, "height": 720}  # Set resolution
    )
    page = context.new_page()
    yield page
    context.close()
