import pymongo
import tweepy
import twitter_keys

# connect to mongodb container
client_docker = pymongo.MongoClient(host="mongodb",port=27017)
db = client_docker.collect_tweets



# Collect tweets (#Food)
client = tweepy.Client(bearer_token=twitter_keys.Bearer_Token)

query = "#Food -is:retweet -is:reply -is:quote -has:links lang:en"
search_tweets = client.search_recent_tweets(query=query,tweet_fields=['id','created_at','text'], max_results=20)
print(search_tweets)
print(type(search_tweets))

for tweet in search_tweets.data:
    record = {'text': tweet.text, 'id': tweet.id, 'created_at': tweet.created_at}
    db.collect_tweets.insert_one(document=record)
