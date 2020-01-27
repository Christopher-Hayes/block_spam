import json
import requests
import os

# Some headers and GraphQL query data needs env variables to function
# The get followers event needs to be simulated in Postman or a browser
#     and specific values need to be copied from their to the environment
url = "https://www.instagram.com/graphql/query/"
# GraphQL query
query_id = os.environ['BLOCK_USER_INSTA_QUERY_ID']
querystring = {"query_hash":os.environ['BLOCK_USER_INSTA_QUERY_HASH'],"variables":'{"id":'+query_id+',"include_reel":true,"fetch_mutual":true,"first":24}'}
# Request headers
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache,no-cache",
    'cookie': os.environ['BLOCK_USER_INSTA_COOKIES'],
    'pragma': "no-cache",
    'x-requested-with': "XMLHttpRequest"
}

# Get followers
# Returns JSON
def get_followers():
    return json.loads(requests.request("GET", url, data="", headers=headers, params=querystring).text)
