import instaloader

# Instantiate
L = instaloader.Instaloader()

# Login or load session
username = 'j_gedd_' # your username
password = 'wouldntyouliketoknowweatherboy' # your password
L.login(username, password) # (login)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)

# List of usernames that YOU are following
follow_list = [followee.username for followee in profile.get_followees()]

# List of usernames that are following YOU
followers_list = [follower.username for follower in profile.get_followers()]

# Finding the difference between the lists (People you follow, but who don't follow back)
non_followers = [user for user in follow_list if user not in followers_list]

print('People who do not follow you back:', ', '.join(non_followers))
