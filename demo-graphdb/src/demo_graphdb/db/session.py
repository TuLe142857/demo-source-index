# db/session.py

from .driver import Neo4jDriver


def execute(query: str, **params):

    driver = Neo4jDriver.driver()

    with driver.session() as session:

        result = session.run(
            query,
            **params
        )

        return list(result)