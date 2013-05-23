#! /usr/bin/python

import praw

user_agent = ("simple praw script for "
              "finding FIXED posts "
              "by Charlie Pashayan")
reddit = praw.Reddit(user_agent = user_agent)
v_fixed = []
submission_generator = reddit.get_new(limit = 1000)
for submission in submission_generator:
    title = submission.title
    if "[fixed]" in title.lower(): # smash case for simplicity
        v_fixed.append(title)
print "The following %d posts might not make much sense ..." % (len(v_fixed))
for fixed in v_fixed:
    print "\t%s" % (fixed)

