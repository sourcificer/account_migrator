import os
from login import account_login

reddit = account_login()

list_of_subs = open('subLists.txt', 'r')
for line in list_of_subs:
    print(line.strip())
    reddit.subreddit(line.strip()).subscribe()
list_of_subs.close()
