# import twilio
from twilio.rest import Client  # client creates a twilio object in our code that allows us to communicate with a twilio account

# Import the flask framework
from flask import Flask, request

# this is needed to respond to any textas that come in
from twilio.twiml.messaging_response import MessagingResponse

# for csv files
import pandas as pd

# codes required by twilio. These are specific to the twilio account being used.
account_sid = 'AC4141b76e99a2898f4f535c7e026a37ab'
auth_token = 'b5b74bb177bcbb81a26569ab53c2fd15'

# make our twilio client
client = Client(account_sid, auth_token)

#
sender = '+12052728434'
numbers = pd.read_csv('numbers.csv', names=['phone']).phone.tolist()[1:]  # list of the phone numbers
blacklist = pd.read_csv('blacklist.csv', names=['phone']).phone.tolist()[1:]  # list of blacklisted numbers

# Hardcoding numbers into the file is not a good way to store the data, instead use files for them
# numbers = ['+15063270183', '+15063270183'] # example numbers to send to
# blacklist = ['+10123456789'] # numbers we don't want to send to

# set() ignores duplicates, recievers = numbers excluding those blacklisted
recievers = list(set(numbers).difference(set(blacklist)))  # would normally get this from a csv file that client gives, etc.

# Broadcast the initial text to get subscribers aware


def broadcast():

	# import time
	# time.sleep(1000)

    for reciever in recievers:
        # string we will text out via SMS
        text = 'yay!\n\nHey subscriber! Do you want to check out our new product?' + \
            '\n\nReply Y to be given the link.' + \
            '\n\nReply B to be blacklisted and stop recieving texts from us.'

        # Use the client to send the SMS text
        client.messages.create(to=reciever, from_=sender, body=text, media_url='https://i.kym-cdn.com/photos/images/original/001/560/860/462.jpg')


# Create our flask app
web_app = Flask(__name__)

# basic web app
# def flask_url():
#     return 'Hello'
# web_app.add_url_rule('/', 'flask_url', flask_url)


def sms_reply():

    if request.method == 'POST':  # if a text comes in

        # Getting the incoming data from the subscriber
        number = request.form['From']
        message_body = request.form['Body']

        # if they reply Y
        if message_body == 'Y':
            response_text = 'https://logandiadams.me/'

        # if they request to blacklisted
        if message_body == 'B':
            blacklist.append(number)
            df = pd.DataFrame(blacklist, columns=['phone'])
            df.to_csv('blacklist.csv', index=False)
            response_text = "Okay you won't be hearing from me again!"

    # Create a repsonse object to handle the twiml language
    automatic_response = MessagingResponse()

    # Put a message in our response object
    automatic_response.message(response_text)

    # Return the message to our flask website
    return str(automatic_response)


web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['POST'])

# code starts here
if __name__ == '__main__':

    # broadcast inital text
    broadcast()

    # run this flask app on our local server port 5000
    web_app.run()
