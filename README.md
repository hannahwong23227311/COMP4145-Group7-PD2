# COMP4145 Project Development 2 — Idea 1

SmartInvestor AI is a Streamlit prototype for exploring historical stock data,
comparing securities, reviewing a sample portfolio, and testing a simple
moving-average strategy. It is an educational tool, not a trading system or
investment recommendation.

## Access and deployment status

This project was verified locally, but a public hosted deployment link has not
been confirmed at the time of writing. The local app was successfully launched
with Streamlit at http://localhost:8501 during verification.

> Localhost access is for development and testing only and does not count as a
> public submission link.

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

## Quick validation

A basic smoke test for the app includes:

- Starting Streamlit successfully
- Loading the home dashboard without errors
- Opening the stock analysis, comparison, portfolio, and strategy pages
- Entering a valid HKBU GenAI key and sending a sample question
- Verifying that missing or invalid keys show a warning or error instead of
  crashing the app

## Data and limitations

`stock_data.csv` supplies the historical data used by the dashboard,
comparison, and backtest. The stock-analysis and portfolio pages retrieve
recent prices through Yahoo Finance; availability and freshness are not
guaranteed. Portfolio price retrieval is capped at 20 tickers per calculation.
The backtest omits transaction costs, taxes, slippage, and dividends, and
historical results do not predict future performance.

The AI feature is also dependent on an external HKBU GenAI service and a valid
API key. A local app launch does not prove that live external services are
available or that the API is permanently functional.

## Notes for submission

- Local verification was completed successfully.
- Public hosting and a verified public URL are still required for final
  submission if the assignment expects a live hosted link.
- This prototype is designed for educational and learning use, not for live
  financial trading advice or automated investment decisions.
