import requests

def get_request(url):
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
