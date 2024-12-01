import pytest
import requests
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from HTTP_functions import get_request




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
