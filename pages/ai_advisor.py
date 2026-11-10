import streamlit as st

st.title("AI Financial Advisor")

st.write(
    "Ask questions about stocks, investing and risk management."
)

question = st.chat_input(
    "Ask a question..."
)

if question:

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        st.write(
            "GPT-6-Luna integration will be connected in the next version."
        )