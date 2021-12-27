import os

from login import account_login

import praw

reddit = account_login()

list_of_saves = open('saveLists.txt', 'w')
list_of_saves_comments = open('saveComments.txt', 'w')
for item in reddit.user.me().saved(limit=None):
    if isinstance(item, praw.models.Submission):
        list_of_saves.write(item.id + '\n')
    else:
        list_of_saves_comments.write(item.id + '\n')
list_of_saves.close()
list_of_saves_comments.close()
