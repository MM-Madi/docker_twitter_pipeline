# Docker pipeline for tweet collection and analysis

This repository contains one of my projects as a data science student where I developed a 5 docker container pipeline as follows:<br />
<img width="737" alt="docker_project" src="https://user-images.githubusercontent.com/99167342/173928945-7c047897-2be9-4815-a39f-75658700a0af.png">

<ins>The repository includes the following folders and files:</ins>
* **docker_compose.yml** - docker containers composition
* tweepy_collector:<br />
  **docker_file**<br />
  **requierments.txt**<br />
  **tweepy_collector.py** - script that uses the twitter-api to collect tweets with the hashtag Ukraine and stores them in a mongoDB database
* etl:<br />
  **docker_file**<br />
  **requierments.txt**<br />
  **etl.py** - script that connects to mongoDB data-base, extracts tweets, conducts sentiment analysis, and re-stores them in a postGres database
* slackbot:<br />
  **docker_file**<br />
  **requierments.txt**<br />
  **slackbot.py** - script that connects to postGres database, extracts a random tweet and posts it to a slack-bot 
