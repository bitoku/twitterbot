#-*- coding: utf-8 -*-
import tweepy

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

consumer_key = "0TPMQJbwpOVVMTNnBYvNoHJhi"
consumer_secret = "uAkjG7qvhM6xfws2XHSVWaq3RnfnZg6LIeNX5kGLzwWYlALE8i"
access_token = "855078016086458369-6XrmYPP8XSpZaM5iLqKiWWSGUQ0uXcg"
access_secret = "K3m1G9ULZdgxCam8qdyOR6lqpToMjq589QwJHG7mU9FEO"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

myStreamListener = StreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())
myStream.userstream()