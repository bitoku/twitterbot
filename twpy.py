#-*- coding: utf-8 -*-
import tweepy

consumer_key = "6XrmYPP8XSpZaM5iLqKiWWSGUQ0uXcg"
consumer_secret = "K3m1G9ULZdgxCam8qdyOR6lqpToMjq589QwJHG7mU9FEO"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
print("Access:", auth.get_authorization_url())
verifier = input("Verifier:")
auth.get_access_token(verifier)
print("Access Token:", auth.access_token)
print("Access Token Secret:", auth.access_token_secret)