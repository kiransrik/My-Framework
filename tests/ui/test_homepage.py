import pytest
from pages.home_page import HomePage

def test_homepage_loads_correctly(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.verify_homepage_title()
