# -*- coding: utf-8 -*-

import os
import tweepy

def get_env_variable(var_name):
    try:
        return os.environ(var_name)
    except KeyError:
        import io
        import configparser
        env_file = os.environ.get("PROJECT_ENV_FILE", ".env")
        config = io.StringIO()
        config.write("[DATA]\n")
        config.write(open(env_file).read())
        config.seek(0, os.SEEK_SET)
        cp = configparser.ConfigParser()
        cp.read_file(config)
        value = dict(cp.items("DATA"))[var_name]
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        elif value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        os.environ.setdefault(var_name, value)
        return value

consumer_key = get_env_variable("CONSUMER_KEY")
consumer_secret = get_env_variable("CONSUMER_SECRET")
access_token = get_env_variable("ACCESS_TOKEN")
access_token_secret = get_env_variable("ACCESS_TOKEN_SECRET")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
