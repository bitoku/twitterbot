# -*- coding: utf-8 -*-

from getenv import *
from neo4j.v1 import GraphDatabase, basic_auth

graphenedb_bolt_url = get_env_variable("GRAPHENEDB_BOLT_URL")
graphenedb_bolt_user = get_env_variable("GRAPHENEDB_BOLT_USER")
graphenedb_bolt_password = get_env_variable("GRAPHENEDB_BOLT_PASSWORD")

driver = GraphDatabase.driver(graphenedb_bolt_url, auth=basic_auth(graphenedb_bolt_user, graphenedb_bolt_password))


def create_node(tx, word):
    tx.run("CREATE (n:Word {{word:'{w}'}})".format(w=word))


def create_relationship(tx, begin, end):
    tx.run("('{begin}')-[r:]->('{end}')".format(begin=begin, end=end))


def count_node(tx, word):
    result = list(tx.run("MATCH (n:Word)"
                         "WHERE n.word = '{word}'"
                         "RETURN count(n)", word=word))
    return result[0][0]


def find_node(tx, word):
    if count_node(tx, word) > 0:
        return True
    else:
        return False
