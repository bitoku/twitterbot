#-*- coding: utf-8 -*-
import tweepy

consumer_key = "0TPMQJbwpOVVMTNnBYvNoHJhi"
consumer_secret = "uAkjG7qvhM6xfws2XHSVWaq3RnfnZg6LIeNX5kGLzwWYlALE8i"
access_token = "855078016086458369-6XrmYPP8XSpZaM5iLqKiWWSGUQ0uXcg"
access_secret = "K3m1G9ULZdgxCam8qdyOR6lqpToMjq589QwJHG7mU9FEO"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

api.update_status("Hello, twitter!")