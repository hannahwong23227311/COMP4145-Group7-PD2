# COMP4145 Project Development 2 — Idea 1

SmartInvestor AI is a Streamlit prototype for exploring historical stock data,
comparing securities, reviewing a sample portfolio, and testing a simple
moving-average strategy. It is an educational tool, not a trading system or
investment recommendation.

## Run locally

Python 3.10 or later is recommended.

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Install dependencies and start the app:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit opens the local app in a browser. Its navigation contains:

- Market dashboard and historical data export
- Stock analysis and two-stock comparison
- Portfolio value, cost basis, gain/loss, and allocation
- Moving-average crossover strategy backtest
- Optional AI financial Q&A

The AI advisor requires a valid HKBU GenAI API key entered in its password
field. The key is sent to the configured API for each request and is not stored
in the repository. Never commit API keys or secrets.

## Data and limitations

`stock_data.csv` supplies the historical data used by the dashboard,
comparison, and backtest. The stock-analysis and portfolio pages retrieve
recent prices through Yahoo Finance; availability and freshness are not
guaranteed. Portfolio price retrieval is capped at 20 tickers per calculation.
The backtest omits transaction costs, taxes, slippage, and dividends, and
historical results do not predict future performance.
