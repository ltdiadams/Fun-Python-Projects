from twilio.rest import Client
import time
import schedule
import praw
import random

def job():

    # credentials for your twilio number
    account_sid = 'YOUR_TWILIO_SID'
    auth_token = 'YOUR_AUTH_TOKEN'

    client = Client(account_sid, auth_token)
    sender = 'YOUR_TWILIO_NUM'
    reciever = 'RECIEVER_NUM'

    reddit = praw.Reddit(client_id='REDDIT_APP_ID',
                         client_secret='REDDIT_APP_SECRET',
                         user_agent='Meme script')

    meme = reddit.subreddit('memes').random()

    # compose text message with message and meme
    text = "Meme of the day!"
    client.messages.create(to=reciever, from_=sender, body=text, media_url=meme.url)

schedule.every().day.at("11:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)