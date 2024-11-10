# main.py
from fastapi import FastAPI
from database import neo4j_conn
from search_agent import search_papers
from summarize_agent import summarize_papers
from qa_agent import answer_question
from future_works_agent import generate_future_works

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Academic Research Assistant API is running"}

@app.get("/search")
def search(topic: str):
    query = """
    MATCH (p:Paper)
    RETURN p.title AS title, p.authors AS authors, p.year AS year, p.summary AS summary
    """
    papers = neo4j_conn.query(query)
    results = [{"title": record["title"], "authors": record["authors"], "year": record["year"], "summary": record["summary"]} for record in papers]
    return {"papers": results}

@app.get("/summarize")
def summarize(topic: str):
    query = """
    MATCH (p:Paper)-[:HAS_TOPIC]->(t:Topic {name: $topic})
    RETURN p.title AS title, p.authors AS authors, p.year AS year, p.summary AS summary
    """
    papers = neo4j_conn.query(query, {"topic": topic})
    summaries = summarize_papers([{"title": record["title"], "authors": record["authors"], "year": record["year"], "summary": record["summary"]} for record in papers])
    return {"summaries": summaries}

@app.get("/qa")
def question_answering(topic: str, question: str):
    try:
        query = """
        MATCH (p:Paper)-[:HAS_TOPIC]->(t:Topic {name: $topic})
        RETURN p.summary AS summary
        """
        results = neo4j_conn.query(query, {"topic": topic})
        context = " ".join([record["summary"] for record in results])
        answer = answer_question(question, context)
        return {"answer": answer}
    except Exception as e:
        print("Error in question-answering endpoint:", e)
        return {"error": str(e)}

@app.get("/future_works")
def future_works(topic: str):
    query = """
    MATCH (p:Paper)-[:HAS_TOPIC]->(t:Topic {name: $topic})
    RETURN p.title AS title, p.authors AS authors, p.year AS year, p.summary AS summary
    """
    papers = neo4j_conn.query(query, {"topic": topic})
    summaries = summarize_papers([{"title": record["title"], "authors": record["authors"], "year": record["year"], "summary": record["summary"]} for record in papers])
    future_work_suggestions = generate_future_works(summaries)
    return {"future_work_suggestions": future_work_suggestions}
