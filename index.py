# -*- coding: utf-8 -*-

from StreamListener import *

myStreamListener = StreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
myStream.userstream()
