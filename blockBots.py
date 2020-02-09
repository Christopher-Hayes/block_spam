import medium.main as md
import insta.main as insta

print('Blocking social media accounts that follow spam...')
print('\n================= MEDIUM.COM ==================')
md.followers_json()
print('\n=============== INSTAGRAM.COM =================')
insta.block_spammers()
print('===============================================')
