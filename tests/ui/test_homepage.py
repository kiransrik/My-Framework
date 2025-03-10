import pytest
from pages.home_page import HomePage

def test_homepage_loads_correctly(page):
    # Create an instance of the HomePage class
    home_page = HomePage(page)
    # Load the homepage
    home_page.load()
    # Verify that the homepage title
    home_page.verify_homepage_title()
