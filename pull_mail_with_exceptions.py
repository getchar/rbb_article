#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

import praw
import time # for sleep
import signal # for setting up signal handler and signal constant
import os # for working with file paths

full_path = os.path.abspath(__file__)
source_dir = os.path.dirname(full_path) + os.sep
archive_dir = source_dir + "mail_sack" + os.sep

# pull in onboard data and establish connection
username = open(source_dir + "username.txt", "r").read().rstrip()
password = open(source_dir + "password.txt", "r").read().rstrip()
user_agent = ("simple praw script for "
              "archiving and clearing an inbox "
              "by Charlie Pashayan")
reddit = praw.Reddit(user_agent = user_agent)
reddit.login(username = username, password = password)

keep_on = True
def kill_handler(sig, frame):
    global keep_on
    keep_on = False
signal.signal(signal.SIGUSR1, kill_handler)

# loop through unread mail forever
while (keep_on):
    try:
        for mail in reddit.get_unread():
            tempname = ".tmp%d.txt" % (os.getpid())
            fname = (mail.subject + "-" + 
                     mail.id + 
                     ".txt")
            fcontents = "\n".join(["from: " + mail.author.name,
                                   "re: " + mail.subject,
                                   mail.body])
            open(archive_dir + tempname, "w").write(fcontents)
            os.rename(archive_dir + tempname, archive_dir + fname) # avoid race conditions
            mail.mark_as_read()
            if not keep_on:
                break

    except requests.exceptions.HTTPError as err:
        if err.response.status_code in [502, 503, 504]:
            # these errors may only be temporary
            pass
        else:
            # assume other errors are fatal
            print str(err)
            print "Terminating"
    time.sleep(600)
