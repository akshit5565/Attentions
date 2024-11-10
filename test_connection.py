from neo4j import GraphDatabase

def test_connection():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "C9IsUnzVTguxioih2JxyvHJiCRfeV13howql3ALK4W0" 

    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 1")
        print("Connection successful. Sample data:", result.single())

    driver.close()

test_connection()
