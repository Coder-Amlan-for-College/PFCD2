import tweepy

BEARER_TOKEN = "GIVE YOUR BEARER TOKEN"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "Python Programming"

recent_tweets = client.search_recent_tweets(query=query,max_results=15)

for tweet in recent_tweets.data:
    print(f"Tweet: {tweet.text}\n")