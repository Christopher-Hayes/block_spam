import requests

def get_val(start, end, text):
    k1 = text.find(start) + len(start)
    k2 = text.find(end, k1)
    return text[k1:k2]

def get_ratio(username):
    url = 'https://medium.com/@' + username
    response = requests.request("GET", url)
    str_resp = response.text

    # Parse data
    followingCount = get_val('followingCount":', ',', str_resp)
    followerCount = get_val('followerCount":', ',', str_resp)

    return (followingCount, followerCount)

# Testing
# a, b = get_ratio('username')
# print('Following: {}\nFollowers: {}'.format(a, b))
