import requests

url = "https://www.instagram.com/{}/"
headers = {}

def get_user_following(username):
    html = requests.request("GET", url.format(username), data="", headers=headers).text
    start_str = '"edge_follow":{"count":'
    s = html.index(start_str) + len(start_str)
    e = html.index('}', s)
    return int(html[s:e].replace(',', ''))
