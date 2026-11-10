import streamlit as st

st.title("AI Financial Advisor")

user_question = st.text_input(
    "Ask a financial question:"
)

if user_question:
    st.success("AI response will appear here in the next version.")