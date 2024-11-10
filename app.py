import streamlit as st
import requests

st.title("Academic Research Assistant")

topic = st.text_input("Enter research topic")

if st.button("Search"):
    response = requests.get(f"http://localhost:8000/search?topic={topic}")
    papers = response.json()
    for paper in papers:
        st.write(f"**{paper['title']}** by {paper['authors']} ({paper['year']})")
        st.write(paper['summary'])

if st.button("Summarize"):
    response = requests.get(f"http://localhost:8000/summarize?topic={topic}")
    summaries = response.json()
    st.write("Summaries of recent research:")
    for summary in summaries:
        st.write(summary)

if st.button("Future Research Directions"):
    response = requests.get(f"http://localhost:8000/future_works?topic={topic}")
    suggestions = response.json()
    st.write("Suggested future research directions:")
    for suggestion in suggestions:
        st.write(suggestion)
