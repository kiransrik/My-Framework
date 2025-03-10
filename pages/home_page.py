from playwright.sync_api import Page
from utils import config

class HomePage:
    def __init__(self, page: Page):
        self.page = page  #Store the Playwright page object

    def load(self):
        self.page.goto(config.BASE_URL) #Open Arqiva website
        self.page.screenshot(path=f"screenshots/{self.page.title().lower().replace(' ', '_')}.png") #Capture the screenshot of the home page

    def verify_homepage_title(self):
        assert "Arqiva" in self.page.title(), "Homepage title did not match"  #Verify the homepage title
        missing_element_selector = "text=NonExistentElement"
        assert self.page.locator(missing_element_selector).count() == 0, "Unexpected element found!" #Verify for missing element
