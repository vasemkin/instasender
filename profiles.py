import json
from instaloader import Instaloader, Profile

with open('auth.json') as f:
    auth = json.load(f)

login_name = auth['login']

target_profile = auth['target_profile']


loader = Instaloader()

# login
try:
    loader.load_session_from_file(login_name)
except FileNotFoundError:
    loader.context.log("Session file does not exist yet - Logging in.")
if not loader.context.is_logged_in:
    loader.interactive_login(login_name)
    loader.save_session_to_file()

profile = Profile.from_username(loader.context, target_profile)
followers = profile.get_followers()

loader.context.log()
loader.context.log('Profile {} has {} followers. Writing to file'.format(profile.username, profile.followers))
loader.context.log()

followers_file = open('followers.txt', 'a')

for follower in followers:
    followers_file.write(follower.username + '\n')

loader.context.log('Finished.')

followers_file.close()