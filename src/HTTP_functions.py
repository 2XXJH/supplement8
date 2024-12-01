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

def get_beeceptor_info():
    """
    Sends a GET request to https://echo.free.beeceptor.com and extracts 
    the Postman-Token and IP address from the response.

    Returns:
        tuple: A tuple containing the Postman-Token (str) and the IP address (str).
    """
    url = "https://echo.free.beeceptor.com"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to get a valid response.")
    response_json = response.json()
    postman_token = response_json.get('Postman-Token', '')
    ip_address = response_json.get('ipAddress', '')
    return postman_token, ip_address

def post_beeceptor_hello():
    """
    Sends a POST request to https://echo.free.beeceptor.com with a JSON payload
    containing {"hello": "world"}.

    Returns:
        dict: The JSON response from the server.
    """
    url = "https://echo.free.beeceptor.com"
    payload = {"hello": "world"}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise Exception("Failed to send POST request.")
    return response.json()
