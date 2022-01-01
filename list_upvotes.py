import os

from login import account_login

import praw

reddit = account_login()

list_of_upvotes = open('upvoteLists.txt', 'w')
for item in reddit.user.me().upvoted(limit=None):
    list_of_upvotes.write(item.id + '\n')
list_of_upvotes.close()
