import streamlit as st
import yfinance as yf

st.title("Stock Analysis")

ticker = st.text_input("Stock Symbol", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)

    info = stock.info

    st.metric(
        "Current Price",
        info.get("currentPrice", "N/A")
    )

    hist = stock.history(period="1mo")

    st.line_chart(hist["Close"])