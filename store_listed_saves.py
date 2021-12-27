import os
from login import account_login

reddit = account_login()

list_of_saves = open('saveLists.txt', 'r')
for line in list_of_saves:
    print(line.strip())
    reddit.submission(line.strip()).save()
list_of_saves.close()

list_of_saves_comments = open('saveComments.txt', 'r')
for line in list_of_saves_comments:
    print(line.strip())
    reddit.comment(line.strip()).save()
list_of_saves_comments.close()
