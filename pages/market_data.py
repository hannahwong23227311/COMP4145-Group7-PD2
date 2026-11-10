import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Configuration
# ----------------------------------
with st.sidebar:

    st.markdown("## SmartInvestor AI")

    st.caption(
        "Investment Analytics Platform"
    )

    st.divider()

    st.caption(
        "COMP4145 Project Development 2"
    )

    st.caption(
        "Group 7"
    )

st.set_page_config(
    page_title="Market Dashboard",
    layout="wide"
)

# ----------------------------------
# Load Dataset
# ----------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("stock_data.csv")
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    return df

df = load_data()

# ----------------------------------
# Page Title
# ----------------------------------

st.title("Market Dashboard")

st.write(
    """
    Explore historical stock market performance using
    interactive visualisations and key market indicators.
    """
)

# ----------------------------------
# Stock Selection
# ----------------------------------

stocks = sorted(df["Symbol"].unique())

selected_stock = st.selectbox(
    "Select a Stock",
    stocks
)

filtered = df[df["Symbol"] == selected_stock].copy()

# ----------------------------------
# Key Metrics
# ----------------------------------

latest_price = filtered["Close"].iloc[-1]
highest_price = filtered["High"].max()
lowest_price = filtered["Low"].min()
average_volume = filtered["Volume"].mean()

st.subheader("Performance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Latest Price",
        f"${latest_price:.2f}"
    )

with col2:
    st.metric(
        "Highest Price",
        f"${highest_price:.2f}"
    )

with col3:
    st.metric(
        "Lowest Price",
        f"${lowest_price:.2f}"
    )

with col4:
    st.metric(
        "Average Volume",
        f"{average_volume:,.0f}"
    )

# ----------------------------------
# Create Charts
# ----------------------------------

price_fig = px.line(
    filtered,
    x="Date",
    y="Close",
    title=f"{selected_stock} Closing Price Trend"
)

price_fig.update_layout(
    template="plotly_white",
    height=500
)

volume_fig = px.bar(
    filtered,
    x="Date",
    y="Volume",
    title=f"{selected_stock} Trading Volume"
)

volume_fig.update_layout(
    template="plotly_white",
    height=500
)

# ----------------------------------
# Tabs
# ----------------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "Price Trend",
        "Volume Analysis",
        "Market Data"
    ]
)

with tab1:
    st.plotly_chart(
        price_fig,
        use_container_width=True
    )

with tab2:
    st.plotly_chart(
        volume_fig,
        use_container_width=True
    )

with tab3:
    st.dataframe(
        filtered.sort_values(
            by="Date",
            ascending=False
        ),
        use_container_width=True
    )

# ----------------------------------
# Recent Records
# ----------------------------------

st.subheader("Latest Records")

st.dataframe(
    filtered.tail(10),
    use_container_width=True
)

# ----------------------------------
# Download Dataset
# ----------------------------------

csv_file = filtered.to_csv(index=False)

st.download_button(
    label="Download Filtered Dataset",
    data=csv_file,
    file_name=f"{selected_stock}_data.csv",
    mime="text/csv"
)