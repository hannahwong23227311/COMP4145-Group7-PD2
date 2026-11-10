import streamlit as st
import pandas as pd
from utils.sidebar import render_sidebar

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="SmartInvestor AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("stock_data.csv")

df = load_data()

total_stocks = df["Symbol"].nunique()
total_records = len(df)

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.main {
    background-color: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
}

/* Metric Cards */
div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}

/* Feature Cards */
.feature-card {
    background-color: white;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

/* Titles */
h1 {
    color: #0F172A;
}

h2, h3 {
    color: #1E293B;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.markdown("## SmartInvestor AI")

    st.caption(
        "Investment Analytics Platform"
    )

    st.divider()

    st.caption("COMP4145 Project Development 2")
    st.caption("Group 7")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("SmartInvestor AI")

st.markdown("""
### Transforming Stock Market Data into Actionable Insights

SmartInvestor AI is an interactive platform designed to help users analyse
historical stock performance, compare companies, monitor portfolio trends,
and support investment decision-making through data analytics and artificial intelligence.
""")

st.info(
    "Select a module from the sidebar to begin analysing market data."
)

# --------------------------------------------------
# Overview Metrics
# --------------------------------------------------

st.markdown("## Platform Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Stocks Covered",
        total_stocks
    )

with col2:
    st.metric(
        "Records",
        f"{total_records:,}"
    )

with col3:
    st.metric(
        "Core Features",
        "5"
    )

with col4:
    st.metric(
        "AI Status",
        "Ready"
    )

# --------------------------------------------------
# Market Snapshot
# --------------------------------------------------

st.markdown("## Market Snapshot")

latest_prices = (
    df.groupby("Symbol")["Close"]
    .last()
    .sort_values(ascending=False)
)

st.bar_chart(latest_prices)

# --------------------------------------------------
# Features
# --------------------------------------------------

st.markdown("## Platform Features")

left_col, right_col = st.columns(2)

with left_col:

    st.markdown("""
    <div class="feature-card">
    <h3>Stock Analysis</h3>
    Analyse historical stock prices, identify trends,
    and review company performance over time.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
    <h3>Portfolio Tracker</h3>
    Monitor multiple stocks and assess portfolio value
    through a single dashboard.
    </div>
    """, unsafe_allow_html=True)

with right_col:

    st.markdown("""
    <div class="feature-card">
    <h3>Stock Comparison</h3>
    Compare historical performance and market behaviour
    across different companies.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
    <h3>AI Financial Advisor</h3>
    Generate insights and receive explanations of stock
    market trends through AI-assisted analytics.
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Project Objective
# --------------------------------------------------

st.markdown("## Project Objective")

st.write("""
The objective of SmartInvestor AI is to provide an accessible and user-friendly
investment analytics platform. Through data visualisation, portfolio management,
and AI-powered support, the system enables users to better understand market
behaviour and make more informed investment decisions.
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "SmartInvestor AI | COMP4145 Project Development 2 | Group 7"
)
