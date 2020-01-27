# block_spam

Medium + Instagram Follow-Spam Blocker. Python scripts that go through your followers and when a follower is following over a specified threshold (ie following 1,500 accounts), the script blocks their profile.

I'm sure for some people this doesn't really matter. Personally, I don't post a whole lot, so I'm only really interested in having friends + real people as followers. I find it mildly annoying when I get a bunch notifications about these bot accounts following me. So, I created a script to automatically weed out these accounts.

⚠️ Code provided as is, this is just a small side project that I don't intend spending a whole lot of time on. Especially when the point of the project is to save time. This code makes requests to the Medium.com and Instagram.com servers, authentication is done by reusing cookies from web brower requests. If anyone really wants to use this code, you'll need to copy-paste the cookies from the browser into environment variables (I'm not about to push my cookies to a public repo) with names that are the same as the ones used in the code. A graphql request will also need to be simulated for Instagram.

With cookie/header/graphql data loaded into environmental variables. The code would be run with:

    python3 blockBots.py

----

## Requred environmental variables

**Instagram**
```
export BLOCK_USER_INSTA_COOKIES=''
export BLOCK_USER_INSTA_CSRF=""
export BLOCK_USER_INSTA_AJAX=""
export BLOCK_USER_INSTA_WHITELIST="USERNAME1,USERNAME2,USERNAME3"
export BLOCK_USER_INSTA_QUERY_HASH=""
export BLOCK_USER_INSTA_QUERY_ID=""
```
*"WHITELIST" is not a header, that variable is a list of follower usernames that follow a lot of people, but you don't want to block.*
*QUERY_HASH, and QUERY_ID are not headers either, those are for the GraphQL request, to find those you'll need to block a user in the browser, then look for that GraphQL request.*

**Medium**
```
export BLOCK_USER_MEDIUM_USERNAME=""
export BLOCK_USER_MEDIUM_COOKIES="
export BLOCK_USER_MEDIUM_USER_ID=""
```
