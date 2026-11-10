import streamlit as st
import yfinance as yf

st.title("Stock Analysis")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

if ticker:
    stock = yf.Ticker(ticker)

    try:
        info = stock.info
        current_price = info.get("currentPrice", "N/A")

        st.metric("Current Price", current_price)

        hist = stock.history(period="1mo")

        st.subheader("Price History")
        st.line_chart(hist["Close"])

    except Exception as e:
        st.error(f"Error: {e}")