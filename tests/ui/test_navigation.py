import pytest
from pages.navigation_page import NavigationPage

def test_navigation_about(page): 
    """
    This test verifies that the 'About' dropdown menu functions correctly
    by navigating to specific pages and checking their titles.
    """
    # Create an instance of the NavigationPage class
    navigation_page = NavigationPage(page)
    # Call the method to interact with the 'About' dropdown
    navigation_page.navigate_about_dropdown()
