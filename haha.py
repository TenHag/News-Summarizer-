import streamlit as st
from Prototype_URL import get_articles
from Summarize_Function import summarize


st.title("Summarizer")

query = st.text_input("Search:")

if st.button("Search"):
    all_articles = get_articles(query)

    for i, article in enumerate(all_articles):
        st.subheader(article['title'])
        st.write(summarize(article['text']))
        st.markdown(f"[Link to Original Article]({article['url']})")
        
