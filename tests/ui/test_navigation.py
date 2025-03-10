import pytest
from pages.navigation_page import NavigationPage

def test_navigation_about(page):  # Use 'page' instead of 'browser'
    navigation_page = NavigationPage(page)
    navigation_page.navigate_about_dropdown()
