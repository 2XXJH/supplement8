import requests

def get_request(url):
    """
    Sends an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to which the GET request will be sent.

    Returns:
        tuple: A tuple containing the status code (int) and the response text (str or dict).
            If the response contains JSON data, the text will be returned as a dictionary.

    Raises:
        Exception: If the status code is between 400 and 499 (inclusive).
    """
    response = requests.get(url)
    status_code = response.status_code
    response_text = response.text

    if 'application/json' in response.headers.get('Content-Type', ''):
        try:
            response_text = response.json()
        except ValueError:
            raise Exception('Invalid JSON in response.')

    if 400 <= status_code <= 499:
        raise Exception(f"Client error with status code: {status_code}")

    return status_code, response_text
