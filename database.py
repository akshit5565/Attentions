from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            return session.run(query, parameters)

neo4j_conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="14eb024649811a644153c077197977cf31104a8a485e14f85178d94d93311717")
