import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Strategy Backtest", layout="wide")
st.title("Moving-Average Strategy Backtest")
st.write(
    "Explore a simple long-only moving-average crossover on the included "
    "historical dataset. The backtest is educational and does not predict future results."
)

@st.cache_data
def load_data():
    data = pd.read_csv("stock_data.csv")
    data["Date"] = pd.to_datetime(data["Date"], utc=True)
    return data


try:
    df = load_data()
except (OSError, ValueError, KeyError) as error:
    st.error(f"Could not load the historical stock dataset: {error}")
    st.stop()

stocks = sorted(df["Symbol"].dropna().unique())
if not stocks:
    st.error("The dataset does not contain any stock symbols.")
    st.stop()

controls = st.columns(3)
with controls[0]:
    ticker = st.selectbox("Stock", stocks)

history = (
    df.loc[df["Symbol"] == ticker, ["Date", "Close"]]
    .dropna()
    .sort_values("Date")
    .drop_duplicates("Date", keep="last")
    .set_index("Date")
)
if len(history) < 3:
    st.error("There is not enough historical data for a moving-average backtest.")
    st.stop()

with controls[1]:
    short_window = st.number_input(
        "Short moving average (days)",
        min_value=2,
        max_value=len(history) - 1,
        value=min(20, len(history) - 1),
    )
with controls[2]:
    long_window = st.number_input(
        "Long moving average (days)",
        min_value=2,
        max_value=len(history),
        value=min(50, len(history)),
    )

if short_window >= long_window:
    st.error("The short moving-average window must be smaller than the long window.")
    st.stop()

history["Short MA"] = history["Close"].rolling(int(short_window)).mean()
history["Long MA"] = history["Close"].rolling(int(long_window)).mean()
history["Daily return"] = history["Close"].pct_change().fillna(0)
history["Position"] = (
    (history["Short MA"] > history["Long MA"]).shift(1).fillna(False).astype(int)
)
history["Strategy equity"] = (1 + history["Daily return"] * history["Position"]).cumprod()
history["Buy-and-hold equity"] = (1 + history["Daily return"]).cumprod()
history["Strategy drawdown"] = (
    history["Strategy equity"] / history["Strategy equity"].cummax() - 1
)

strategy_return = history["Strategy equity"].iloc[-1] - 1
buy_hold_return = history["Buy-and-hold equity"].iloc[-1] - 1
max_drawdown = history["Strategy drawdown"].min()
latest_signal = (
    "Long (short MA above long MA)"
    if history["Short MA"].iloc[-1] > history["Long MA"].iloc[-1]
    else "Cash (short MA at/below long MA)"
)

st.caption(
    f"Data period: {history.index.min().date()} to {history.index.max().date()} · "
    "No transaction costs, taxes, slippage, or dividends are modeled."
)

metric_cols = st.columns(4)
metric_cols[0].metric("Strategy return", f"{strategy_return:.1%}")
metric_cols[1].metric("Buy-and-hold return", f"{buy_hold_return:.1%}")
metric_cols[2].metric("Strategy max drawdown", f"{max_drawdown:.1%}")
metric_cols[3].metric("Latest signal", latest_signal)

equity_chart = history[["Strategy equity", "Buy-and-hold equity"]].rename(
    columns={
        "Strategy equity": "Moving-average strategy",
        "Buy-and-hold equity": "Buy and hold",
    }
)
fig = px.line(
    equity_chart,
    title=f"{ticker} — cumulative growth of $1",
    labels={"value": "Portfolio value ($)", "Date": "Date", "variable": "Strategy"},
)
fig.update_layout(template="plotly_white", height=480)
st.plotly_chart(fig, use_container_width=True)

st.info(
    "Signals use the previous trading day's moving-average relationship when "
    "calculating each day's strategy return, reducing look-ahead bias. "
    "Historical performance is not a forecast or investment recommendation."
)
