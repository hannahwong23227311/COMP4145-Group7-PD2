import re

import streamlit as st
import yfinance as yf

st.title("Stock Analysis")
st.caption("Yahoo Finance data can be delayed, incomplete, or unavailable.")

ticker = st.text_input("Enter stock symbol", "AAPL").strip().upper()

if ticker:
    if not re.fullmatch(r"[A-Z0-9.^=-]{1,15}", ticker):
        st.error("Enter a valid ticker symbol using letters, numbers, '.', '^', '=', or '-'.")
        st.stop()

    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="6mo", auto_adjust=False)
        info = stock.info
    except Exception as error:
        st.error(f"Could not retrieve data for {ticker} from Yahoo Finance: {error}")
        st.stop()

    if history.empty:
        st.warning(f"No recent price history was returned for {ticker}.")
        st.stop()

    latest_close = float(history["Close"].dropna().iloc[-1])
    current_price = info.get("currentPrice")
    if not isinstance(current_price, (int, float)):
        current_price = latest_close

    market_cap = info.get("marketCap")
    pe_ratio = info.get("trailingPE")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current price", f"${current_price:,.2f}")
    col2.metric(
        "Market cap",
        f"${market_cap:,.0f}" if isinstance(market_cap, (int, float)) else "Unavailable",
    )
    col3.metric(
        "P/E ratio",
        f"{pe_ratio:.2f}" if isinstance(pe_ratio, (int, float)) else "Unavailable",
    )

    st.subheader("Six-month closing price")
    st.line_chart(history["Close"])

    st.subheader("Company")
    st.write(info.get("longBusinessSummary") or "No company description is available.")
