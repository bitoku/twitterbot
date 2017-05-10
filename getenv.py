# -*- coding: utf-8 -*-

import os

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
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
        value = dict(cp.items("DATA"))[var_name.lower()]
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        elif value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        os.environ.setdefault(var_name, value)
        return value
