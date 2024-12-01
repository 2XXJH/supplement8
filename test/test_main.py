import pytest
import requests
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from HTTP_functions import get_request




#
def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # A sample URL that returns JSON
    status_code, response_text = get_request(url)
    assert status_code == 200
    assert isinstance(response_text, dict)  # Should return a dictionary for JSON response

def test_get_request_error():
    url = "https://jsonplaceholder.typicode.com/invalid_url"
    with pytest.raises(Exception):
        get_request(url)

@patch('requests.get')
def test_get_beeceptor_info(mock_get):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"Postman-Token": "abcd1234", "ipAddress": "192.168.1.1"}'
    mock_get.return_value = mock_response

    postman_token, ip_address = get_beeceptor_info()

    assert postman_token == "abcd1234"
    assert ip_address == "192.168.1.1"
