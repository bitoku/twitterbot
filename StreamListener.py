# -*- coding: utf-8 -*-
import tweepy
from myoauth import api
import graph


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.in_reply_to_user_id == api.me().id:
            print("received \"" + status.text + "\"")
            with graph.driver.session() as session:
                # extract the body from the original tweet
                word = status.text.split(" ", 1)

                if status.in_reply_to_status_id != NULL:
                    # if the word is a reply, then tweet a word related with two before words.
                    if api.get_status(status.in_reply_to_status_id).user.id == api.me().id:
                        if session.read_transaction(graph.find_node, word):
                            # if there is the word in db, then tweet a word connected with the received word randomly
                            session.write_transaction(graph.create_relationship, word, before_word)
                        else:
                            session.write_transaction(graph.create_node, word)
                else:
                    # if the word is the first word, then tweet a word from db randomly.
                    # TODO
                    pass

                # api.update_status(status=tweet, in_reply_to_status_id=status.id)

    def on_error(self, status_code):
        print("Got an error code " + status_code)
        if status_code == 420:
            return False

    def on_timeout(self):
        print("Time out...")
        return True
