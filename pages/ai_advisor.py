import streamlit as st
import requests

st.title("AI Financial Advisor")

with st.sidebar:

    st.markdown("## SmartInvestor AI")

    st.caption(
        "Investment Analytics Platform"
    )

    st.divider()

    st.caption(
        "COMP4145 Project Development 2"
    )

    st.caption(
        "Group 7"
    )

# API Key Input

api_key = st.text_input(
    "HKBU GenAI API Key",
    type="password"
)

# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input

prompt = st.chat_input(
    "Ask a question about investments..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    if api_key:

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-6-luna",
            "messages": [
                {
                    "role": "system",
                    "content": """
                    You are a financial advisor.
                    Explain market concepts clearly.
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:

            response = requests.post(
                "https://genai.hkbu.edu.hk/api/v1/chat/completions",
                json=payload,
                headers=headers
            )

            result = response.json()

            answer = result["choices"][0]["message"]["content"]

            with st.chat_message("assistant"):
                st.write(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            st.error(
                f"API Error: {e}"
            )

    else:

        st.warning(
            "Please enter your HKBU GenAI API key."
        )