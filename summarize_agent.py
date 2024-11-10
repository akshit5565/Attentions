from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_papers(papers):
    summaries = [summarizer(paper['summary'])[0]['summary_text'] for paper in papers]
    return summaries
