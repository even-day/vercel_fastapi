import random, string
import requests


def get_hub_url(hub_url):
    subscription_dict = {}
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    header = {
        'Referer': hub_url,
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    form_data = {
        'email': ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12)) + '@gmail.com',
        'password': 'autosub_v2b',
        'invite_code': '',
        'email_code': ''
    }
    try:
        response = requests.post(hub_url + V2B_REG_REL_URL, data=form_data, headers=header)
        subscription = f'{hub_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
        subscription_dict["link"] = subscription
    except:
        print("获取订阅失败")
    # print(f'Number succeeded: {i}\t{subscription_url}')
    return subscription_dict
