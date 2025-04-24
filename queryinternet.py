import streamlit as st
st.title("This is an app built for giving you updates on topics requested by you ")
question = st.text_input("Please ask a question")
if st.button("Request") :
    from langchain_community.tools import DuckDuckGoSearchRun
    search_tool = DuckDuckGoSearchRun()
    results = search_tool.invoke(question)
    st.write(results)
