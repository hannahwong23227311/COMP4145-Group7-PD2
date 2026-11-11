import pandas as pd
import streamlit as st
import yfinance as yf

st.title("Portfolio Tracker")
st.write(
    "Enter your holdings to estimate their market value, cost basis, and "
    "unrealised gain or loss."
)
st.caption(
    "Prices come from Yahoo Finance and may be delayed or unavailable. "
    "This prototype does not execute trades."
)

with st.form("portfolio_form"):
    holdings = st.data_editor(
        pd.DataFrame(
            {
                "Ticker": pd.Series(dtype="str"),
                "Shares": pd.Series(dtype="float"),
                "Average cost ($)": pd.Series(dtype="float"),
            }
        ),
        num_rows="dynamic",
        hide_index=True,
        column_config={
            "Ticker": st.column_config.TextColumn("Ticker", required=True),
            "Shares": st.column_config.NumberColumn(
                "Shares", min_value=0.000001, step=1.0, required=True
            ),
            "Average cost ($)": st.column_config.NumberColumn(
                "Average cost ($)", min_value=0.0, step=1.0, required=True
            ),
        },
        key="portfolio_holdings",
    )
    submitted = st.form_submit_button("Calculate portfolio")

if submitted:
    if holdings.empty:
        st.warning("Add at least one holding to calculate your portfolio.")
        st.stop()

    holdings["Ticker"] = holdings["Ticker"].fillna("").astype(str).str.strip().str.upper()
    holdings["Shares"] = pd.to_numeric(holdings["Shares"], errors="coerce")
    holdings["Average cost ($)"] = pd.to_numeric(
        holdings["Average cost ($)"], errors="coerce"
    )
    invalid_rows = (
        holdings["Ticker"].eq("")
        | holdings["Shares"].isna()
        | holdings["Average cost ($)"].isna()
        | holdings["Shares"].le(0)
        | holdings["Average cost ($)"].lt(0)
    )
    if invalid_rows.any():
        st.error("Enter a ticker, positive share count, and non-negative cost for each row.")
        st.stop()

    holdings["Cost basis ($)"] = holdings["Shares"] * holdings["Average cost ($)"]
    holdings = holdings.groupby("Ticker", as_index=False).agg(
        {"Shares": "sum", "Cost basis ($)": "sum"}
    )
    holdings["Average cost ($)"] = holdings["Cost basis ($)"] / holdings["Shares"]
    if len(holdings) > 20:
        st.error("For data-provider reliability, analyze no more than 20 tickers at a time.")
        st.stop()

    tickers = holdings["Ticker"].tolist()
    try:
        prices = yf.download(
            tickers=tickers,
            period="5d",
            group_by="ticker",
            auto_adjust=False,
            progress=False,
            threads=False,
        )
    except Exception as error:
        st.error(f"Could not retrieve market prices from Yahoo Finance: {error}")
        st.stop()

    latest_prices = {}
    for ticker in tickers:
        try:
            if isinstance(prices.columns, pd.MultiIndex):
                if (ticker, "Close") in prices.columns:
                    close = prices[(ticker, "Close")]
                else:
                    close = prices[("Close", ticker)]
            else:
                close = prices["Close"]
            close = close.dropna()
            if not close.empty:
                latest_prices[ticker] = float(close.iloc[-1])
        except (KeyError, TypeError, ValueError):
            continue

    holdings["Current price ($)"] = holdings["Ticker"].map(latest_prices)
    unavailable = holdings["Current price ($)"].isna()
    if unavailable.any():
        st.warning(
            "No recent price was returned for: "
            + ", ".join(holdings.loc[unavailable, "Ticker"])
        )

    results = holdings.loc[~unavailable].copy()
    if results.empty:
        st.error("No usable prices were returned. Check the ticker symbols and try again.")
        st.stop()

    results["Market value ($)"] = results["Shares"] * results["Current price ($)"]
    results["Cost basis ($)"] = results["Shares"] * results["Average cost ($)"]
    results["Gain / loss ($)"] = results["Market value ($)"] - results["Cost basis ($)"]
    market_value = results["Market value ($)"].sum()
    cost_basis = results["Cost basis ($)"].sum()
    gain_loss = market_value - cost_basis

    value_col, cost_col, pnl_col = st.columns(3)
    value_col.metric("Market value", f"${market_value:,.2f}")
    cost_col.metric("Cost basis", f"${cost_basis:,.2f}")
    pnl_col.metric(
        "Unrealised gain / loss",
        f"${gain_loss:,.2f}",
        delta=f"{gain_loss / cost_basis:.2%}" if cost_basis else "Enter cost to calculate return",
    )

    st.subheader("Holdings")
    st.dataframe(
        results.set_index("Ticker")[
            [
                "Shares",
                "Average cost ($)",
                "Current price ($)",
                "Market value ($)",
                "Cost basis ($)",
                "Gain / loss ($)",
            ]
        ].style.format("${:,.2f}", subset=[
            "Average cost ($)",
            "Current price ($)",
            "Market value ($)",
            "Cost basis ($)",
            "Gain / loss ($)",
        ]),
        use_container_width=True,
    )

    allocation = results.set_index("Ticker")["Market value ($)"]
    st.subheader("Portfolio allocation")
    st.bar_chart(allocation / market_value)
    st.download_button(
        "Download holdings as CSV",
        data=results.to_csv(index=False),
        file_name="portfolio_holdings.csv",
        mime="text/csv",
    )
