# import tweepy

# API_KEY ="API KEY"
# API_SECRET = "API SECRET"
# ACCESS_TOKEN = "ACCESS TOKEN"
# ACCESS_SECRET = "ACCESS SECRET"
# BEARER_TOKEN = "BEARER TOKEN"

# client = tweepy.Client(bearer_token = BEARER_TOKEN)

# username = "GIVE YOUR USERNAME"
# user = client.get_user(username=username,user_fields=["public_metrics"])

# if user.data:
#     print("User ID",user.data.id)
#     print("Username",user.data.username)
#     print("Name:",user.data.name)
#     print("Followers count:",user.data.public_metrics["followers_count"])
# else:
#     print("USER NOT FOUND")

import tweepy

BEARER_TOKEN = "GIVE YOUR BEARER TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

username = "USERNAME"
user = client.get_user(username=username,user_fields=["public_metrics"])

if user.data:
    print(user.data.id)
    print(user.data.username)
    print(user.data.name)
    print(user.data.public_metrics["followers_count"])

else:
    print("user does not exist")