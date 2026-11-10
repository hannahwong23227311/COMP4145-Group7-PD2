import streamlit as st
import yfinance as yf

st.title("Portfolio Tracker")

stocks = st.text_input(
    "Enter stock symbols separated by commas",
    "AAPL,MSFT,NVDA"
)

if stocks:

    tickers = [x.strip() for x in stocks.split(",")]

    for ticker in tickers:

        try:
            stock = yf.Ticker(ticker)
            price = stock.info.get("currentPrice")

            st.write(f"**{ticker}** : ${price}")

        except:
            st.write(f"{ticker}: Data unavailable")