import os
from dotenv import load_dotenv

import praw

load_dotenv()


def account_login():
    reddit = praw.Reddit(
        client_id=os.getenv('reddit_client_id'),
        client_secret=os.getenv('reddit_client_secret'),
        username=os.getenv('reddit_username'),
        password=os.getenv('reddit_password'),
        user_agent='account migrator'
    )
    return reddit
