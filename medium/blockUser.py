import requests
import os

# Constants
url = "https://medium.com/_/graphql"
headers = {
        'authority': "medium.com",
        'method': "POST",
        'path': "/_/graphql",
        'scheme': "https",
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'cache-control': "no-cache,no-cache",
        'content-length': "289",
        'content-type': "application/json",
        'cookie': os.environ['BLOCK_USER_MEDIUM_COOKIES'],
        'graphql-operation': "UserBlockMutation",
        'origin': "https://medium.com",
        'pragma': "no-cache",
        'user-agent': os.environ['BLOCK_USER_MEDIUM_USER_AGENT']
        }
user_id=os.environ['BLOCK_USER_MEDIUM_USER_ID']

# Block user by userID
def block_user(targetUserId):
    payload = "{\"operationName\":\"UserBlockMutation\",\"variables\":{\"targetUserId\":\"" + targetUserId + "\",\"userId\":\"" + user_id + "\"},\"query\":\"mutation UserBlockMutation($targetUserId: ID!, $userId: ID!) {\\n  blockUser(userId: $userId, targetUserId: $targetUserId) {\\n    id\\n    isBlocking\\n    __typename\\n  }\\n}\\n\"}"
    return requests.request("POST", url, data=payload, headers=headers)


# run test
# response = block_user('userid')
# print(response.text)
