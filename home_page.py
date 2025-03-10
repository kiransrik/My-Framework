from playwright.sync_api import Page
from utils import config

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(config.BASE_URL)
        self.page.screenshot(path=f"screenshots/{self.page.title().lower().replace(' ', '_')}.png")

    def verify_homepage_title(self):
        assert "Arqiva" in self.page.title(), "Homepage title did not match"