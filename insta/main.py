import insta.blockUser as bu
import insta.getFollowers as gf
import insta.getUser as gu
import os

# Don't block those non-spammers that actually follow 1500+ people O.o
# This is placed in an env variable like this (comma deliminitor):
# export BLOCK_USER_INSTA_WHITELIST="USERNAME1,USERNAME2,USERNAME3"
BLOCK_WHITELIST = os.environ['BLOCK_USER_INSTA_WHITELIST'].split(',') 
# Followers that follow more than this threshold will be auto blocked (Block follow-spammers)
FOLLOW_THRESHOLD=1500

def block_spammers():
    # Returns JSON
    json_resp = gf.get_followers()
    followers = json_resp['data']['user']['edge_followed_by']['edges']
    # Log what users get blocked
    out = open('blocked_instagram.txt', 'a')
    blockedCount = 0
    for f in followers:
        d = f['node']
        user_id = d['id']
        username = d['username']
        full_name = d['full_name']
        following = gu.get_user_following(username)
        # Block users over specified follow threshold
        block = following > FOLLOW_THRESHOLD
        print('\t{}:\n\t\tusername: {}\n\t\tFollowing: {}\n'.format(full_name, username, following))
        if (block and not username in BLOCK_WHITELIST):
            status = bu.block_user(user_id)
            if (status):
                print('---------- BLOCKED USER {} -----------'.format(username))
                # Log what users get blocked
                out.write(username + '\n')
                blockedCount += 1
            else:
                print('---------- ERROR: FAILED TO BLOCK USER {} ---------'.format(username))
    out.close()
    print('\tBlocked Users: {}\n'.format(blockedCount))
