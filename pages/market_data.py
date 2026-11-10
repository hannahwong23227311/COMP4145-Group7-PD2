import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Market Data Dashboard",
    page_icon="📈",
)

st.title("📈 Market Data Dashboard")
st.write("Explore historical stock market data.")

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("stock_data.csv")
    df["Date"] = pd.to_datetime(
        df["Date"],
        utc=True,
        errors="coerce"
    )
    return df

df = load_data()

# Stock Selection
symbols = sorted(df["Symbol"].unique())

selected_stock = st.selectbox(
    "Select a Stock",
    symbols
)

# Filter by Stock
filtered = df[df["Symbol"] == selected_stock].copy()

# Date Range Filter
st.subheader("Date Filter")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "Start Date",
        filtered["Date"].min().date()
    )

with col2:
    end_date = st.date_input(
        "End Date",
        filtered["Date"].max().date()
    )

filtered = filtered[
    (filtered["Date"] >= pd.Timestamp(start_date, tz="UTC"))
    &
    (filtered["Date"] <= pd.Timestamp(end_date, tz="UTC"))
]

# Safety Check
if filtered.empty:
    st.warning("No data available for the selected date range.")
    st.stop()

# Metrics
latest_price = filtered["Close"].iloc[-1]
highest_price = filtered["High"].max()
lowest_price = filtered["Low"].min()
avg_volume = filtered["Volume"].mean()

st.subheader(f"{selected_stock} Summary")

col1, col2, col3, col4 = st.columns(4)

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

col4.metric(
    "Average Volume",
    f"{avg_volume:,.0f}"
)

# Price Chart
st.subheader("📊 Closing Price Trend")

price_chart = filtered.set_index("Date")["Close"]

st.line_chart(price_chart)

# Volume Chart
st.subheader("📦 Trading Volume")

volume_chart = filtered.set_index("Date")["Volume"]

st.bar_chart(volume_chart)

# OHLC Data
st.subheader("Market Statistics")

stats_col1, stats_col2 = st.columns(2)

with stats_col1:
    st.write(f"**Average Open:** ${filtered['Open'].mean():.2f}")
    st.write(f"**Average High:** ${filtered['High'].mean():.2f}")

with stats_col2:
    st.write(f"**Average Low:** ${filtered['Low'].mean():.2f}")
    st.write(f"**Average Close:** ${filtered['Close'].mean():.2f}")

# Recent Data Table
st.subheader("📋 Latest 20 Records")

st.dataframe(
    filtered.tail(20),
    use_container_width=True
)

# Download Button
csv = filtered.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name=f"{selected_stock}_stock_data.csv",
    mime="text/csv"
)