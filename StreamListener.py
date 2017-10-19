# -*- coding: utf-8 -*-
import tweepy
from myoauth import api
import graph


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.in_reply_to_user_id == api.me().id:
            print("recieved \"" + status.text + "\"")
            # extract the body
            word = status.text.split(" ", 1)
            tweet = "@" + status.user.screen_name + " " + status.user.name + "「" + word + "」"
            # tweet the same word
            api.update_status(status=tweet, in_reply_to_status_id=status.id)
            with graph.driver.session() as session:
                if session.read_transaction(graph.find_node, word):
                    session.write_transaction(graph.create_relationship, word, before_word)
                else:
                    session.write_transaction(graph.create_node, word)

    def on_error(self, status_code):
        print("Got an error code " + status_code)
        if status_code == 420:
            return False

    def on_timeout(self):
        print("Time out...")
        return True
