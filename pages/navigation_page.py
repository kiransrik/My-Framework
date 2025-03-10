from playwright.sync_api import Page
from utils import config

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page  # Store the Playwright page object

    def navigate_about_dropdown(self):    # Click the "About" button to open the dropdown
        self.page.goto(config.BASE_URL)
        self.page.click("text=About")
        # List of menu items and expected titles
        menu_items = {
            "About Arqiva": "About Arqiva",
            "Arqiva Life": "Arqiva Life",
            "Leadership": "Leadership"
        }

        for item_text, expected_page_title in menu_items.items():
            # Click each dropdown item
            self.page.wait_for_selector(f"text={item_text}")  # Ensure the element is present
            self.page.click(f"text={item_text}")
            # Verify the page titles           
            assert self.page.title() == expected_page_title, f"Title mismatch for {item_text}! Expected: {expected_page_title}, Found: {self.page.title()}"  
             # Take a screenshot of each visited page
            self.page.screenshot(path=f"screenshots/{item_text.lower().replace(' ', '_')}.png")

            # Navigate back and reopen the dropdown for the next item
            self.page.go_back()
            self.page.click("text=About")
