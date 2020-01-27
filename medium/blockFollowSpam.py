import requests
import json
import medium.followratio as fr
import medium.blockUser as bu
import os

# BLOCK USERS AT THIS FOLLOWING COUNT AND HIGHER
follow_block_at = 500

username=os.environ['BLOCK_USER_MEDIUM_USERNAME']
url = f'https://medium.com/@{username}/followers'

payload = ""
headers = {
    'authority': "medium.com",
    'method': "GET",
    'path': f'/@{username}/followers',
    'scheme': "https",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache,no-cache",
    'cookie': os.environ['BLOCK_USER_MEDIUM_COOKIES'],
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1"
    }

def followers_json():
    print('Getting profile information..')
    response = requests.request("GET", url, data=payload, headers=headers)
    print('Parsing profile information..\n')
    str_resp = response.text
    start_k = str_resp.find(start) + 7
    end_k = str_resp.find(end, start_k)
    trim_resp = response.text[start_k : end_k]
    json_resp = json.loads(trim_resp)
    users_blocked = 0
    for v in json_resp:
        name = json_resp[v]['name']
        username = json_resp[v]['username']
        user_id = json_resp[v]['userId']
        following, followers = fr.get_ratio(username)
        print('name: {}\n\tusername: {}\n\tfollowing: {}\n\tfollowers: {}\n\t'.format(name, username, following, followers))
        if int(following) > follow_block_at:
            print('------------------------------------------\n\tBLOCKING USER: {}\n------------------------------------------'.format(username))
            print('User block server response: {}\n'.format(bu.block_user(user_id).text))
            users_blocked += 1
    print('Users Blocked: {}'.format(users_blocked))

start = '"User":{'
end = ',"Social":'
