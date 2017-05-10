#-*- coding: utf-8 -*-
import tweepy
from myoauth import api

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

