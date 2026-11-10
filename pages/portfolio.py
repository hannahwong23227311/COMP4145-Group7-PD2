import streamlit as st
import yfinance as yf

st.title("Portfolio Tracker")

stocks = st.text_input(
    "Enter stocks separated by commas",
    "AAPL,MSFT,NVDA"
)

if stocks:

    tickers = [s.strip() for s in stocks.split(",")]

    total_price = 0

    for ticker in tickers:

        try:
            stock = yf.Ticker(ticker)

            price = stock.info["currentPrice"]

            st.write(
                f"✅ {ticker}: ${price}"
            )

            total_price += price

        except:
            st.write(
                f"❌ {ticker}: unavailable"
            )

    st.divider()

    st.metric(
        "Portfolio Value (1 share each)",
        f"${total_price:.2f}"
    )