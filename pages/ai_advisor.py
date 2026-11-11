import requests
import streamlit as st

API_URL = "https://genai.hkbu.edu.hk/api/v1/chat/completions"
MODEL = "gpt-6-luna"

st.title("AI Financial Advisor")
st.caption(
    "Ask general questions about investing and market concepts. AI responses "
    "may be inaccurate and are not personalized financial advice."
)

api_key = st.text_input("HKBU GenAI API key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask a question about investing...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    if not api_key:
        st.warning("Enter your HKBU GenAI API key to receive an answer.")
    else:
        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Explain financial and market concepts in clear language. "
                        "Do not claim certainty, fabricate current market data, or "
                        "present responses as personalized financial advice."
                    ),
                },
                *st.session_state.messages,
            ],
        }
        try:
            response = requests.post(
                API_URL,
                json=payload,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                timeout=45,
            )
            response.raise_for_status()
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
            if not isinstance(answer, str) or not answer.strip():
                raise ValueError("The API returned an empty or invalid answer.")
        except requests.HTTPError as error:
            detail = error.response.text[:1000] if error.response is not None else str(error)
            st.error(f"AI API returned an error: {detail}")
        except requests.RequestException as error:
            st.error(f"Could not reach the AI API: {error}")
        except (ValueError, KeyError, IndexError, TypeError) as error:
            st.error(f"Could not read the AI API response: {error}")
        else:
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )
            with st.chat_message("assistant"):
                st.write(answer)
