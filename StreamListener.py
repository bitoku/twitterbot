#-*- coding: utf-8 -*-
import tweepy
from myoauth import api
import graph

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.in_reply_to_user_id==api.me().id:
            print("recieved \"" + status.text +"\"")
            tweet="@"+status.user.screen_name+" "+ \
                status.user.name+"「"+status.text.split(" ", 1)[1]+"」"
            api.update_status(status=tweet)
            with graph.driver.session() as session:
                session.write_transaction(graph.create_node, status.text.split(" ", 1)[1])

    def on_error(self, status_code):
        print("Got an error code " + status_code)
        if status_code == 420:
            return False

    def on_timeout(self):
        print("Time out...")
        return True

