# Import the flask framework
from flask import Flask

# this is needed to respond to any textas that come in
from twilio.twiml.messaging_response import MessagingResponse

# Create our flask app
web_app = Flask(__name__)

# basic web app
# def flask_url():
#     return 'Hello'
# web_app.add_url_rule('/', 'flask_url', flask_url)


def sms_reply():

    # Create a repsonse object to handle the twiml language
    automatic_response = MessagingResponse()

    # Put a message in our response object
    automatic_response.message('This is an automatic reply from Python and Twilio!')

    # Return the message to our flask website
    return str(automatic_response)


web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['POST'])

# code starts here
if __name__ == '__main__':
    # run this flask app on our local server port 5000
    web_app.run()
