import requests

def search_papers(topic):
    url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&start=0&max_results=5"
    response = requests.get(url)
    return []
