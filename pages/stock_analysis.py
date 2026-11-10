import streamlit as st
import yfinance as yf

st.title("Stock Analysis")

ticker = st.text_input("Enter Stock Symbol", "AAPL")

if ticker:

    try:
        stock = yf.Ticker(ticker)

        info = stock.info

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Current Price",
            f"${info.get('currentPrice', 'N/A')}"
        )

        col2.metric(
            "Market Cap",
            f"{info.get('marketCap', 'N/A'):,}"
        )

        col3.metric(
            "P/E Ratio",
            info.get('trailingPE', 'N/A')
        )

        hist = stock.history(period="6mo")

        st.subheader("Price Trend")

        st.line_chart(hist["Close"])

        st.subheader("Company")

        st.write(
            info.get("longBusinessSummary", "No description available.")
        )

    except Exception as e:
        st.error(e)