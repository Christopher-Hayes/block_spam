import json
import requests
import os

# Block user {} - .format() replaces the {}
url = "https://www.instagram.com/web/friendships/{}/block/"
# Headers - create env variables for certain headers (required for auth)
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache,no-cache",
    'content-length': "0",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': os.environ['BLOCK_USER_INSTA_COOKIES'],
    'origin': "https://www.instagram.com",
    'pragma': "no-cache",
    'user-agent': os.environ['BLOCK_USER_INSTA_USER_AGENT'],
    'x-csrftoken': os.environ['BLOCK_USER_INSTA_CSRF'],
    'x-ig-app-id': os.environ['BLOCK_USER_INSTA_APP_ID'],
    'x-instagram-ajax': os.environ['BLOCK_USER_INSTA_AJAX'],
    'x-requested-with': "XMLHttpRequest"
}

# Block user 'user_id'
def block_user(user_id):
    json_resp = json.loads(requests.request("POST", url.format(user_id), data="", headers=headers).text)
    return json_resp['status'] == 'ok', json_resp
