FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "slackbot.py"]
