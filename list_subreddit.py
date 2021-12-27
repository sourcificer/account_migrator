import os
from login import account_login

reddit = account_login()

list_of_subs = open('subLists.txt', 'w')
for subreddit in reddit.user.subreddits(limit=None):
    print(str(subreddit))
    list_of_subs.write(str(subreddit) + '\n')
list_of_subs.close()
