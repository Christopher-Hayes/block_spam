import medium.blockFollowSpam as md
import insta.blockSpammers as insta

print('Blocking social media accounts that follow spam...')
print('\n================= MEDIUM.COM ==================')
md.followers_json()
print('\n=============== INSTAGRAM.COM =================')
insta.block_spammers()
print('===============================================')
