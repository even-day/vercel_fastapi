import requests
token = 'secret_NfGNOHhDG8lzncErmTdau7gTJvvuZ5Pn0ZOALHfFDhh'
r = requests.request(
        "GET",
        "https://api.notion.com/v1/databases/622e8dc9dd9c4ac4b1201f980e657abe",#字符串为页面id
        headers={"Authorization": "Bearer " + token, "Notion-Version": "2022-06-28"},
    )
print(r.text)
