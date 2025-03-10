import requests

def test_api_status():
    """
    This function tests whether the API endpoint is accessible and returns a successful response.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")  # Send a GET request to the API endpoint
    # Assert that the response status code is 200 (OK), indicating a successful request
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}" 
