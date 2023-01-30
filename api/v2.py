import random, string
import requests


def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    # V2B_SUB_REL_URL = '/api/v1/user/getSubscribe'
    home_urls = (
        # 'https://www.yifei999.com',
        # 'https://www.funkyun.xyz'
        # 'https://console.ly520.me',
        # 'https://www.ckcloud.xyz',
        # 'https://fastestcloud.xyz',
        # 'https://www.ckcloud.xyz',
        # 'https://fastestcloud.xyz',
        # 'https://shan-cloud.xyz',
        # 'http://hneko.xyz',
        # 'https://www.ckcloud.xyz',
        # 'https://user.bafang.vip',
        # 'https://cloud.hhygj.xyz',
        'https://feiniaoyun.top',
        # 'https://fastestcloud.xyz',
        'https://www.dgycom.com',
    )
    subscription_dict = {}
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
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
                response = requests.post(current_url + V2B_REG_REL_URL, data=form_data, headers=header)
                subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                subscription_dict[current_url] = subscription_url
                return subscription_dict
            except:
                print("获取订阅失败")
            i += 1
            # print(f'Number succeeded: {i}\t{subscription_url}')
