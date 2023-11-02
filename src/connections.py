import smtplib
import os
import configparser

def getCredentials():
    credentials_file = os.path.join(os.path.dirname(__file__), 'credentials.txt')
    credentials_config = configparser.ConfigParser()
    credentials_config.read(credentials_file)
    username = credentials_config['emailcredentials'].get('username')
    password = credentials_config['emailcredentials'].get('password')
    return {"username":username, "password":password}


def connect_to_inbox():
    credentials = getCredentials()
    username = credentials['username']
    password = credentials['password']

    # Connect to gmail
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.starttls
    gmail.login(username, password)
    return gmail

def get_unread_count():
    credentials = getCredentials()
    username = credentials['username']
    password = credentials['password']
    #emails = imaplib.IMAP4_SSL('imap.gmail.com')
    #emails.login(username, password) 
    #res, messages = emails.select('"[Gmail]/Sent Mail"') 
    #emails.login(username, password)
    #emails.select("[Gmail]/All Mail")
    #email_count = int(len(emails.search(None, 'Unseen')[1][0].split()))
    #print("Athene" + str(email_count))
    return 5

def get_espeak(count):
    os.system(f'espeak-ng "{count}"')



