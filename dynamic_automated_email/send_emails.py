# SMTP app

# import the the SMTP lib, SMTP = simple main transfer protocol. Protocol we follow to send emails
import smtplib

# Import MIME text format lib. MIME = multipurpose internet mail extensions
# It's an intenet standard we follow to encode email contents like: attachments, pictures, links, text, etc.
from email.mime.text import MIMEText

# Import python's email utility package
import email.utils

# for reading csv files
import pandas as pd

# Which email this is being sent from
sender_email = 'LoganDiA1999@gmail.com'
sender_name = 'Logan DiAdams'
# password so we can log into user's account
password = 'pbd5g5pf'

# read csv file using pandas
column_names = ['name', 'email']
data = pd.read_csv("email_list.csv", names=column_names)

# Who this email is being sent to
# recipient_email = 'alexvoid44@gmail.com'

recipient_emails = data.email.tolist()[1:]  # ['deckerdaniel48@gmail.com', 'jonnydoereceiver@gmail.com']
recipient_names = data.name.tolist()[1:]  # ['Dan Decker', 'John Doe']

html_file = open("email_contents.html", "r")

# Message body, use html5 on line editor
email_html = html_file.read()
'''
	<p><em><span style="text-decoration: underline;"><span style="color: #ff0000; text-decoration: underline;">Yo what is up homedawg?</span></span></em></p>
	<p>Have you checked out my:</p>
	<ul>
	<li><strong>Youtube</strong></li>
	<li><strong>Website</strong></li>
	<li><strong>Instagram</strong></li>
	</ul>
	<p>?</p>
	<p>Hope you're having a wicked ole day&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></p>
	<p>That is all.</p>
	<p><a href="https://www.google.com/search?q=ight+imma+head+out+memes&amp;sxsrf=ACYBGNTTpGCqJsEjgZUIMCpfq46XccVA8A:1571799002374&amp;source=lnms&amp;tbm=isch&amp;sa=X&amp;ved=0ahUKEwjy-sbJr7HlAhXtmeAKHTWpAB4Q_AUIEigB&amp;biw=900&amp;bih=921#imgrc=vSHmhy4cI45XNM:"><img src="https://www.dailydot.com/wp-content/uploads/2019/09/spongebob-ight-imma-head-out-meme.jpg" alt="" width="450" height="225" /></a></p>
'''

# our function


def broadcast_email():
    print('\nBroadcasting email...\n')

# loop through entire email list
    for recipient_name, recipient_email in zip(recipient_names, recipient_emails):

        # get message ready in email format, give html functionality
        message = MIMEText(email_html, 'html')
        message.add_header('Content-Type', 'text/html')

        # print(type(message))
        # print(message)

        # populate the message object with data. Good practice. Follow protocol and industry standard
        message['To'] = email.utils.formataddr((recipient_name, recipient_email))
        message['From'] = email.utils.formataddr((sender_name, sender_email))
        message['Subject'] = 'Hey check this shit out :D'

        # setup the email server. Gmail host, and use a common port (googled these things lol)
        server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP domain host, common SMTP port
        # hotmail: smtp.live.com
        # aol: smtp.aol.com
        # yahoo: smtp.mail.yahoo.com

        # turn transport layer security. All SMTP commands after this will be encrypted
        server.starttls()

        # log in to the sender's email account
        server.login(sender_email, password)

        # print(message.as_string())

        # send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # cleanup
        server.quit()

        # confirm it was sent for the client
        print('Sent to ' + recipient_name + ' at ' + recipient_email)

    print('\nEmail broadcasted\n')


# call our code to send the emails
broadcast_email()
