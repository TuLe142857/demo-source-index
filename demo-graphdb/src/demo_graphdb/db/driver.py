# db/driver.py

from neo4j import GraphDatabase


class Neo4jDriver:

    _driver = None

    @classmethod
    def connect(cls, uri, user, password):

        if cls._driver is None:
            cls._driver = GraphDatabase.driver(
                uri,
                auth=(user, password)
            )

    @classmethod
    def driver(cls):
        return cls._driver

    @classmethod
    def close(cls):
        if cls._driver:
            cls._driver.close()