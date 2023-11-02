from src import connections, ErrorHelper
import espeakng
import os
import subprocess
import logging
import sched
import time
import subprocess
from datetime import datetime

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
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    for line in proc.stdout:
        if line.rstrip():
            # only print lines that are not empty
            # # decode() is necessary to get rid of the binary string (b')
            # # rstrip() to remove `\r\n`
            logging.debug(f"{line.decode().rstrip()} running on {now}")


def writeLog(text):
    try:
        #stream = open('bossSpy.log', '+a')
        #stream.Write(text)
        #stream.close()
        logging.error(text)
    except Exception as exception:
        ErrorHelper.displayError('an error has occured')


event_schedule = sched.scheduler(time.time, time.sleep)
event_schedule.enter(30, 1, getEmails, (s,))
event_schedule.enter(30, 1, checkProcess, (s,))
event_schedule.run()
