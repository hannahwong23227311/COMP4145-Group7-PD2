import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Stock Comparison",
    layout="wide"
)

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

# ----------------------------------
# Load Data
# ----------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("stock_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ----------------------------------
# Page Title
# ----------------------------------

st.title("Stock Comparison")

st.write(
    "Compare the historical performance of two stocks using market data."
)

# ----------------------------------
# Stock Selection
# ----------------------------------

stocks = sorted(df["Symbol"].unique())

col1, col2 = st.columns(2)

with col1:
    stock_1 = st.selectbox(
        "Select Stock 1",
        stocks,
        index=0
    )

with col2:
    stock_2 = st.selectbox(
        "Select Stock 2",
        stocks,
        index=1
    )

# ----------------------------------
# Filter Data
# ----------------------------------

data_1 = df[df["Symbol"] == stock_1].copy()
data_2 = df[df["Symbol"] == stock_2].copy()

# ----------------------------------
# Key Metrics
# ----------------------------------

latest_1 = data_1["Close"].iloc[-1]
latest_2 = data_2["Close"].iloc[-1]

high_1 = data_1["High"].max()
high_2 = data_2["High"].max()

low_1 = data_1["Low"].min()
low_2 = data_2["Low"].min()

avg_volume_1 = data_1["Volume"].mean()
avg_volume_2 = data_2["Volume"].mean()

st.subheader("Performance Summary")

metric_col1, metric_col2 = st.columns(2)

with metric_col1:

    st.markdown(f"### {stock_1}")

    st.metric(
        "Latest Price",
        f"${latest_1:.2f}"
    )

    st.metric(
        "Highest Price",
        f"${high_1:.2f}"
    )

    st.metric(
        "Lowest Price",
        f"${low_1:.2f}"
    )

    st.metric(
        "Average Volume",
        f"{avg_volume_1:,.0f}"
    )

with metric_col2:

    st.markdown(f"### {stock_2}")

    st.metric(
        "Latest Price",
        f"${latest_2:.2f}"
    )

    st.metric(
        "Highest Price",
        f"${high_2:.2f}"
    )

    st.metric(
        "Lowest Price",
        f"${low_2:.2f}"
    )

    st.metric(
        "Average Volume",
        f"{avg_volume_2:,.0f}"
    )

# ----------------------------------
# Price Trend Chart
# ----------------------------------

st.subheader("Historical Closing Price")

chart_data = pd.concat(
    [
        data_1[["Date", "Close"]].assign(Stock=stock_1),
        data_2[["Date", "Close"]].assign(Stock=stock_2)
    ]
)

fig = px.line(
    chart_data,
    x="Date",
    y="Close",
    color="Stock",
    title="Closing Price Comparison"
)

fig.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# Volume Comparison
# ----------------------------------

st.subheader("Average Trading Volume")

volume_df = pd.DataFrame({
    "Stock": [stock_1, stock_2],
    "Average Volume": [avg_volume_1, avg_volume_2]
})

fig2 = px.bar(
    volume_df,
    x="Stock",
    y="Average Volume",
    color="Stock",
    title="Average Trading Volume Comparison"
)

fig2.update_layout(
    template="plotly_white",
    height=450,
    showlegend=False
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ----------------------------------
# Recent Market Data
# ----------------------------------

st.subheader("Latest Records")

tab1, tab2 = st.tabs([stock_1, stock_2])

with tab1:
    st.dataframe(
        data_1.tail(10),
        use_container_width=True
    )

with tab2:
    st.dataframe(
        data_2.tail(10),
        use_container_width=True
    )