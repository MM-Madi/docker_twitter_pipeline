# Slack-Bot Script -  takes analyzed tweets from PostGres, post to Slack
import pandas as pd
import requests
import sqlalchemy
import cred
import json
import time

# connect to postgres  
DATABASE = 'analyzed_tweets'
PORT = '5432'
USER = cred.user
PASSWORD = cred.password
HOST = 'mypostgres'

conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
engine = sqlalchemy.create_engine(conn_string,echo=False)

time.sleep(10)

# Select and extract random tweet
result = engine.execute('SELECT tweet FROM tweets_syn OFFSET floor(random() * (SELECT COUNT(*) FROM tweets_syn)) LIMIT 1;')

# post to slack
webhook_url = cred.url
data = {'text': result}
requests.post(url=webhook_url, json = data)
