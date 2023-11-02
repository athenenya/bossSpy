from src import connections
import espeakng
import os
import subprocess
import logging

#log configuration
#logging.basicConfig(filename='bossSpy.log', encoding='utf-8', level=logging.DEBUG)

#log usage.
#logging.debug('This message should go to the log file')

def get_smtp_object():
    pass

def getEmails():
    unread_count = connections.get_unread_count()
    if unread_count > 2:
        # Scream.
        connections.get_espeak(unread_count)

getEmails()