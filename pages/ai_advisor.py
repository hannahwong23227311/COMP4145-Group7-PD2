import streamlit as st

st.title("AI Financial Advisor")

question = st.text_input("Ask a financial question")

if question:
    st.info("GPT-6-Luna integration coming next.")