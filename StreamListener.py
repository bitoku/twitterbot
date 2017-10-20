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
                B_word = status.text.split(" ", 1)
                create_node(B_word)

                # if the word is a reply, then tweet a word related with two before words.
                if status.in_reply_to_status_id != NULL:
                    A_prev_tweet = api.get_status(status.in_reply_to_status_id)
                    if A_prev_tweet.user.id == api.me().id:
                        B_prev_tweet = api.get_status(A_prev_tweet.in_reply_to_status_id)
                        A_prev_word = A_prev_tweet.text.split(" ", 1)
                        B_prev_word = B_prev_tweet.text.split(" ", 1)

                        word = self.choice_word(A_prev_word, B_prev_word)
                        tweet = "@" + status.user.screen_name + " " + word
                        api.update_status(status=tweet, in_reply_to_status_id=status.id)

                        session.write_transaction(graph.create_relationship, B_word, A_prev_word)
                        session.write_transaction(graph.create_relationship, B_word, B_prev_word)
                else:
                    # if the word is the first word, then tweet a word from db randomly.
                    # TODO
                    pass


    def choice_word(self, word1, word2):
        pass

    def on_error(self, status_code):
        print("Got an error code " + status_code)
        if status_code == 420:
            return False

    def on_timeout(self):
        print("Time out...")
        return True
