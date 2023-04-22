import requests


def return_raw(url):
    headers = {
        'User-Agent': 'Rule2Clash'
    }
    response = requests.get(url, headers=headers, timeout=5000).text
    return response
