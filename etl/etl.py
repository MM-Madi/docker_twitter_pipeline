# ETL Script -  takes tweets from mongodb container, transforms and Analyzes Tweets, push to MyPstgres container

import pymongo
import sqlalchemy
import cred
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# connect to Mongodb
client_docker = pymongo.MongoClient(host="mongodb",port=27017)
db = client_docker.collect_tweets

# extract tweets from mongoDB
tweets = db.collect_tweets.find()

# connect to postgres
DATABASE = 'analyzed_tweets'
PORT = '5432'
USER = cred.user
PASSWORD = cred.password
HOST = 'mypostgres'

conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
engine = sqlalchemy.create_engine(conn_string,echo=False)

# Create table in Postgres (for output)
query = "CREATE TABLE IF NOT EXISTS tweets_syn (tweet VARCHAR(500), sentiment NUMERIC);"
engine.execute(query)

# initiate Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()
mentions_regex= '@[A-Za-z0-9]+'               # tweet cleaning (remove mentions)

# for each tweet - extract text, analyze score and push in Postgres
for document in tweets:
    text = re.sub(mentions_regex, '', document['text'])
    print(text)
    score = analyzer.polarity_scores(text)
    print(score)
    compound_score = score['compound']
    print(compound_score)
    engine.execute('''INSERT INTO tweets_syn VALUES (%s,%s);''', (text, compound_score))
