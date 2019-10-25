# import twilio
from twilio.rest import Client  # client creates a twilio object in our code that allows us to communicate with a twilio account

# for csv files
import pandas as pd

# codes required by twilio. These are specific to the twilio account being used.
account_sid = 'AC4141b76e99a2898f4f535c7e026a37ab'
auth_token = 'b5b74bb177bcbb81a26569ab53c2fd15'

# make our twilio client
client = Client(account_sid, auth_token)

#
sender = '+12052728434'
numbers = pd.read_csv('numbers.csv', names=['phone']).phone.tolist()[1:] # list of the phone numbers
blacklist = pd.read_csv('blacklist.csv', names=['phone']).phone.tolist()[1:] # list of blacklisted numbers

# Hardcoding numbers into the file is not a good way to store the data, instead use files for them
# numbers = ['+15063270183', '+15063270183'] # example numbers to send to
# blacklist = ['+10123456789'] # numbers we don't want to send to

# set() ignores duplicates, recievers = numbers excluding those blacklisted
recievers = list(set(numbers).difference(set(blacklist)))  # would normally get this from a csv file that client gives, etc.

for reciever in recievers:
    # string we will text out via SMS
    text = 'yay!\n\nHey subscriber! Do you want to check out our new product?' + \
    		'\n\nReply Y to be given the link.' + \
    		'\n\nReply B to be blacklisted and stop recieving texts from us.'

    # Use the client to send the SMS text
    client.messages.create(to=reciever, from_=sender, body=text)
