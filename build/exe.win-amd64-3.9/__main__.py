from src import connections
import espeakng
import os
import subprocess

def get_smtp_object():
    pass

def getEmails():
    unread_count = connections.get_unread_count()
    if unread_count > 2:
        # Scream.
        connections.get_espeak(unread_count)

getEmails()