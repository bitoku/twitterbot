# -*- coding: utf-8 -*-

import os
import tweepy
from getenv import *


consumer_key = get_env_variable("TWITTER_CONSUMER_KEY")
consumer_secret = get_env_variable("TWITTER_CONSUMER_SECRET")
access_token = get_env_variable("TWITTER_ACCESS_TOKEN")
access_token_secret = get_env_variable("TWITTER_ACCESS_TOKEN_SECRET")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
