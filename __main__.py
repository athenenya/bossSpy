from src import connections, ErrorHelper
import espeakng
import os
import subprocess
import logging
import sched
import time

logging.basicConfig(filename='bossSpy.log', encoding='utf-8', level=logging.Error)

#log usage.
#logging.debug('This message should go to the log file')

def get_smtp_object():
    pass

def getEmails():
    unread_count = connections.get_unread_count()
    writeLog('Get Emails Rain')
    if unread_count > 2:
        # Scream.
        connections.get_espeak(unread_count)

def checkProcess():
    pass

def writeLog(text):
    try:
        #stream = open('bossSpy.log', '+a')
        #stream.Write(text)
        #stream.close()
        logging.debug(text)
    except Exception as exception:
        ErrorHelper.displayError('an error has occured')


event_schedule = sched.scheduler(time.time, time.sleep)
event_schedule.enter(30, 1, getEmails, (s,))
event_schedule.enter(30, 1, checkProcess, (s,))
event_schedule.run()
