# -*- coding: utf-8 -*-
import tweepy
import os
from bottle import route, run

@route("/")


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        if status.in_reply_to_user_id==api.me().id:
            tweet="@"+status.user.screen_name+" "+ \
                status.user.name+"「"+status.text.split(" ", 1)[1]+"」"
            api.update_status(status=tweet)

    def on_error(self, status_code):
        if status_code == 420:
            return False

consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN_KEY"]
access_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

myStreamListener = StreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
myStream.userstream()

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
