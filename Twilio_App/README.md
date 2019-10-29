<h1>Interactive Text Automation App!</h1>

Uses twilio to interact with a user or multiple users given phone numbers from a CSV file, based on an input of 'Y' or 'B' the app will respond differently. 'Y' will send a response, and 'B' will add your number to the /blacklist/ so you won't recieve a message from the app again. The blacklisted numbers are contained within the 'blacklist.csv' file and are updated when a user responds with 'B'. The app also supports the sending of media (images/video).

Makes use of Pandas for handling CSV files, Flask and NGROK for creating the web app with POST containing the individual user response and NGROK for tunneling into our local flask app to make the data contained in it publicly available for twilio to use (address has to be changed in twilio whenever NGROK is reset) as well as twilio itself for managing our SMS texts!

Getting started:

1. install NGROK from https://ngrok.com
2. run the command: ./ngrok http 5000 and leave it running
3. change your twilio configuration Messaging at https://www.twilio.com/console/phone-numbers/incoming to: ((yourngrokaddress))/sms
4. add your personal phone number(s) to the numbers.csv file
5. add your account_sid, auth_token, and twilio number(sender) to the full_app.py file and save it
5. open another terminal window and run the python file: python full_app.py

You'll recieve a text message to your number prompting a response and the app takes care of the rest!
