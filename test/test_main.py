import pytest
import requests
from unittest.mock import patch

# Test for get_request function
def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # A sample URL that returns JSON
    status_code, response_text = get_request(url)
    assert status_code == 200
    assert isinstance(response_text, dict)  # Should return a dictionary for JSON response

def test_get_request_error():
    url = "https://jsonplaceholder.typicode.com/invalid_url"
    with pytest.raises(Exception):
        get_request(url)
