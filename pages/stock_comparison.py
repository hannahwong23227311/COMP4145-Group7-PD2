import streamlit as st
import pandas as pd

st.title("Stock Comparison")

df = pd.read_csv("stock_data.csv")

stock1 = st.selectbox(
    "Stock 1",
    sorted(df["Symbol"].unique())
)

stock2 = st.selectbox(
    "Stock 2",
    sorted(df["Symbol"].unique()),
    index=1
)

s1 = df[df["Symbol"] == stock1]
s2 = df[df["Symbol"] == stock2]

col1, col2 = st.columns(2)

with col1:
    st.subheader(stock1)
    st.metric(
        "Latest Price",
        f"${s1['Close'].iloc[-1]:.2f}"
    )

with col2:
    st.subheader(stock2)
    st.metric(
        "Latest Price",
        f"${s2['Close'].iloc[-1]:.2f}"
    )