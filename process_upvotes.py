import os

from praw import reddit
from login import account_login

reddit = account_login()

list_of_upvotes = open('upvoteLists.txt', 'r')
for line in list_of_upvotes:
    print(line.strip())
    try:
        reddit.submission(line.strip()).upvote()
    except:
        continue
list_of_upvotes.close()
