# -*- coding: utf-8 -*-

from getenv import *
from neo4j.v1 import GraphDatabase, basic_auth

graphenedb_bolt_url = get_env_variable("GRAPHENEDB_BOLT_URL")
graphenedb_bolt_user = get_env_variable("GRAPHENEDB_BOLT_USER")
graphenedb_bolt_password = get_env_variable("GRAPHENEDB_BOLT_PASSWORD")

driver = GraphDatabase.driver(graphenedb_bolt_url, auth=basic_auth(graphenedb_bolt_user, graphenedb_bolt_password))


def create_node(tx, word):
    tx.run("CREATE (n:Word {word:'{w}'})".format(w=word))


def create_relationship(tx, word1, word2):
    tx.run("MATCH (a:Word),(b:Word)"
           "WHERE a.word='{word1}' AND b.word='{word2}'"
           "CREATE (a)-[r:RELATE]->(b);".format(word1=word1, word2=word2))


def shortest_path(tx, word1, word2):
    result = tx.run("MATCH p=shortestPath("
                    "('{word1}'-[*]-'{word2}')"
                    "RETURN p").format(word1=word1, word2=word2)
    return result


def count_node(tx, word):
    result = list(tx.run("MATCH (n:Word)"
                         "WHERE n.word = '{word}'"
                         "RETURN count(n)".format(word=word)))
    return result[0][0]


def count_relationship(tx, word1, word2):
    result = list(tx.run("MATCH (a:Word)-[r]-(b:Word)"
                         "WHERE a.word='{word1} AND b.word='{word2}"
                         "RETURN count(r)".format(word1=word1, word2=word2)))
    return result[0][0]


def find_node(tx, word):
    if count_node(tx, word) > 0:
        return True
    else:
        return False


def find_relationship(tx, word1, word2):
    if count_relationship(tx, word1, word2) > 0:
        return True
    else:
        return False
