# twitter_docker_pipeline

This repository contains one of my projects as a data science student taken from my student repo (copy of finalized files), in it i developed a 5 docker container pipeline with the following functions:<br />
**Container 1** - uses the twitter-api to collect tweets with a specific hashtag<br />
**Container 2** - stores the tweets in a mongoDB data container<br />
**Container 3** - an ETL that extracts the tweets, conducts sentiment analysis, and re-stores them with their scores in a postGres data base<br />
**Container 4** - stores the output of etl in a postGres data base<br />
**Container 5** - posts the tweet and its sentiment in a slack-chanel-bot<br />


The repository includes the following folders and files:
* docker_compose.yml - docker containers composition
* tweepy_collector:<br />
  docker_file<br />
  requierments.txt<br />
  tweepy_collector - script that uses the twitter-api to collect tweets with the hashtag Ukraine and stores them in a mongoDB database
* etl:<br />
  docker_file<br />
  requierments<br />
  etl - script that connects to mongoDB data-base, extracts tweets, conducts sentiment analysis, and re-stores them in a postGres database
* slackbot:<br />
  docker_file<br />
  requierments<br />
  slackbot - script that connects to postGres database, extracts a random tweet and posts it to a slack-bot 
