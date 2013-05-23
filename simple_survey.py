#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

import praw
import re
import sys

# pull in onboard data and establish connection
username = open("username.txt", "r").read().rstrip()
password = open("password.txt", "r").read().rstrip()
user_agent = ("simple praw script for "
              "tabulating survey results "
              "by Charlie Pashayan")
reddit = praw.Reddit(user_agent = user_agent)
reddit.login(username = username, password = password)

# pull desired submissions
submission_id = open("submission_id.txt", "r").read().rstrip()
submission = reddit.get_submission(submission_id = submission_id)

# compile the results of the survey
survey_says = {}
for comment in submission.comments:
    ans_pattern = re.compile("\\[(?P<choice>.*?)\\]")
    match = ans_pattern.search(comment.body)
    if not match:
        continue
    choice = match.group("choice")
    if choice not in survey_says:
        survey_says[choice] = 0
    survey_says[choice] += 1

# report results in the submission body
magic_string = "Results:"
selftext = submission.selftext.split(magic_string)
if len(selftext) == 1:
    print "No space for results."
    sys.exit(1)
for choice in survey_says:
    old = ("\\\\\\[%s\]:\s*\d+" % (choice))
    new = ("\\[%s\]: %d" % (choice, survey_says[choice]))
    selftext[-1] = re.sub(old, new, selftext[-1])
selftext = magic_string.join(selftext)
submission.edit(selftext)
