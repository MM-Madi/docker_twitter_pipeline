# twitter_docker_pipeline

This repository contains one of my projects as a data science student taken from my student repo (copy of finalized files), in it i developed a 5 docker container pipeline with the following functions:
Container 1 - uses the twitter-api to collect tweets with a specific hashtag__
Container 2 - stores the tweets in a mongoDB data container__
Container 3 - an ETL that extracts the tweets, conducts sentiment analysis, and re-stores them with their scores in a postGres data base
Container 4 - stores the output of etl in a postGres data base
Container 5 - posts the tweet and its sentiment in a slack-chanel-bot


The repository includes the following folders and files:
* docker_compose.yml - docker containers composition
* tweepy_collector:
  docker_file
  requierments.txt
  tweepy_collector - script that uses the twitter-api to collect tweets with the hashtag Ukraine and stores them in a mongoDB database
* etl:
  docker_file
  requierments
  etl - script that connects to mongoDB data-base, extracts tweets, conducts sentiment analysis, and re-stores them in a postGres database
* slackbot:
  docker_file
  requierments
  slackbot - script that connects to postGres database, extracts a random tweet and posts it to a slack-bot 
