import streamlit as st
import pandas as pd

st.title("Market Data Dashboard")

# Load dataset
df = pd.read_csv("stock_data.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Stock selection
symbols = sorted(df["Symbol"].unique())

selected_stock = st.selectbox(
    "Select a Stock",
    symbols
)

# Filter data
filtered = df[df["Symbol"] == selected_stock]

# Metrics
latest_price = filtered["Close"].iloc[-1]
highest_price = filtered["High"].max()
lowest_price = filtered["Low"].min()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Latest Price",
    f"${latest_price:.2f}"
)

col2.metric(
    "Highest Price",
    f"${highest_price:.2f}"
)

col3.metric(
    "Lowest Price",
    f"${lowest_price:.2f}"
)

# Price chart
st.subheader("Closing Price Trend")
st.line_chart(
    filtered.set_index("Date")["Close"]
)

# Volume chart
st.subheader("Trading Volume")
st.bar_chart(
    filtered.set_index("Date")["Volume"]
)

# Recent records
st.subheader("Latest Data")
st.dataframe(
    filtered.tail(10),
    use_container_width=True
)