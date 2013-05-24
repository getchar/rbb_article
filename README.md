This repository contains scripts I've written as examples for a [tutorial](http://www.nonbird.com/rbb_article/redditbottutorial.html) I wrote about making Reddit bots.  Each script is meant to illustrate some functionality having to do with Reddit bots.  And they're designed to make sense when revealed in sequential pieces, interspersed with long passages of English text.

What this means is that scripts don't do anything useful and they feature what might seem like some poor design decisions if you weren't reading them generously and hadn't been aprised of what I just told you.  So beware.  I'm sorry.

With that out of the way, I'll run through the scripts below and explain what they do.  And if you have any interest in writing a Reddit bot of your own, please read [my tutorial](http://www.nonbird.com/rbb_article/redditbottutorial.html) and you can also check out my own Reddit bot, [`CannedPostResponder`](https://github.com/getchar/cannedpostresponder).

`fixed_finder.py`

This just scans the first 1000 submissions on [http://reddit.com/new](http://www.reddit.com/new) and compiles a list of all the ones with "[FIXED]" in their titles, then reports the list to the user.

`simple_survey.py`

This script scans through the comments posted in response to a survey question, pulls out the answers then modifies the original post to reflect the current count of the votes.  For the sake of keeping things simple, it's a little picky about the formatting of the question and the answers, but of all the scripts in my tutorial, this one comes the closest to being useful, which it would certainly be if it were a little more robust and user friendly.

`pull_mail.py`

This script sits on top of a user's inbox, making local copies of everything it finds.  It also marks everything as read, meaning you probably don't want to run it on your own inbox.  And it runs forever until told to stop by another process.  It's purpose is to introduce interprocess communication and Python's `signal` module.

`kill_pm.py`

This script sends a signal to `pull_mail.py`, letting it know when it's time to shut down as soon as it finishes the loop it's currently on.  

`pull_mail_with_exceptions.py`

This script is identical to `pull_mail.py` except that it wraps the innermost loop, containing the calls to the Reddit API, in a try/except block, to catch and ignore any HTTP errors that could plausibly be caused by temporary (i.e. non-fatal) network conditions.