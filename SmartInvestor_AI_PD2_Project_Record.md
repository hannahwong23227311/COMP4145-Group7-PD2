# SmartInvestor AI
## Project Record & Delivery Update
**COMP4145 Project Development 2 — Idea 1 | Group 7**
**Status date:** 11 November 2026
**Draft note:** Actual week dates, historical team assignments, and deployment status were not provided. Scrum-board snapshots below are reconstructed from the repository, not contemporaneous records.

## Project purpose

Build an accessible stock-analysis prototype for non-professional investors. SmartInvestor AI brings historical market exploration, company comparison, portfolio calculations, a simple strategy backtest, and optional AI explanations into one Streamlit interface. It supports learning and decision support; it does not place trades or provide personalized financial advice.

## Initial project update — Week 1 (reconstructed)

The supplied repository already contained a Streamlit dashboard, stock analysis, comparison, a basic one-share portfolio view, an AI chat page, and a 12,540-row historical CSV covering 10 symbols. The exact Week 1 accomplishments and dates are unknown.

This baseline provided a usable prototype, but the portfolio did not account for user quantities or cost basis, the AI page had a placeholder Authorization header, and mixed time zones could break comparison data loading. Yahoo Finance availability and API credentials were identified as risks.

## Chosen enhancements

| Enhancement | User value and rationale |
|---|---|
| Portfolio analytics | Enter holdings and cost; calculate market value, cost basis, unrealized gain/loss, and allocation. Bulk price lookup is capped at 20 tickers. |
| Moving-average backtest | Compare a simple long-only crossover with buy-and-hold; show return, drawdown, and latest signal. Uses the supplied historical CSV. |
| Working AI advisor | Use the HKBU endpoint with Bearer authentication, response/error handling, a password key field, and a financial-advice disclaimer. |

**System at a glance:** Investor → Streamlit multipage UI → historical CSV (dashboard, comparison, backtest) + Yahoo Finance (recent prices) + optional HKBU GenAI API (chat). The sources are separate; external data can be delayed, rate-limited, or unavailable.

## Scrum board snapshots

**Important:** Actual historical board exports and dates were unavailable. These snapshots are reconstructed from the supplied repository baseline; they are not verified historical activity.

### Before Week 1 — proposed starting board

| Backlog / To do | Starting evidence |
|---|---|
| Agree user needs and acceptance criteria; inspect dataset and API constraints; plan UI and data flow. | A Streamlit app shell and sample historical CSV were present; file history was not verified. |
| Plan portfolio quantities/cost basis, comparison, AI integration, tests, and deployment. | Basic dashboard, analysis, comparison, portfolio, and AI-advisor page files existed. |

### End of Week 1 — reconstructed from baseline

| Observed as present | Open / not verified at that point |
|---|---|
| Dashboard and CSV charts; single-stock analysis; two-stock comparison; basic portfolio page; AI chat UI. | Reliable portfolio valuation; working API authentication; strategy backtest; robust timezone parsing; user testing; public deployment. |
| Dataset: 12,540 rows and 10 symbols (validated during this work). | Actual Week 1 completion dates, owners, estimates, blockers, and team acceptance were not supplied. |

### Team communication and ownership

The brief describes a ten-person group spanning business and technical roles, but names and actual assignments were not provided. Suggested communication: weekly CEO/CTO summary of scope, risks, and decisions; a shared sprint board with one accountable owner per story; technical/business review of data assumptions; and a demo plus acceptance check at sprint end. The role allocation below is proposed, not confirmed.

| Stakeholder / proposed role | Primary project concern |
|---|---|
| CEO / sponsor; CTO / technical approver | Business value, scope, architecture, risk, and release decision. |
| Product owner; business analyst; finance/market SME | Investor needs, acceptance criteria, trading assumptions, and disclaimers. |
| UX designer; app developer; data engineer | Clarity/accessibility, Streamlit implementation, data integrity, and source limits. |
| QA tester; release/documentation owner | Regression checks, usability feedback, deployment, and project record. |

## Final project update — current local build

As of 11 November 2026, app dependencies were installed into the ignored project-local `.venv`. The local implementation has six core modules (market dashboard, stock analysis, comparison, portfolio, AI advisor, and strategy backtest) plus a home landing page. Changes were made and smoke-checked in this session; historical team delivery dates remain unknown.

- **Portfolio:** Editable ticker/share/cost inputs; weighted cost basis for duplicate ticker rows; market value, unrealized gain/loss, and allocation; missing prices reported; 20-ticker limit.
- **Strategy:** Long-only moving-average crossover; signals use the prior day for daily returns to reduce look-ahead bias; comparison with buy-and-hold and maximum drawdown shown.
- **AI advisor:** HKBU endpoint/model, Bearer key header, 45-second timeout, API status/response validation, and clear errors. A live key/API call was not tested.
- **Reliability and documentation:** Stock symbol validation and missing-data handling; mixed-timezone CSV parsing corrected in comparison; README updated with setup, data, and limitations.

### End of Week 2 — reconstructed delivery board

| Done / verified locally | Pending / blocked for release |
|---|---|
| Implemented three enhancements; Python compilation passed; Streamlit AppTest passed for home, AI, portfolio, comparison, and strategy pages; local Streamlit health endpoint returned “ok”. | Public deployment URL and hosting status are unverified. Cloud publish and a working public link remain required for submission. |
| CSV integrity check passed: 12,540 rows, 10 symbols, populated closing-price values. README includes local run instructions. | Yahoo Finance live requests, HKBU API with a valid key, and end-user acceptance testing were not performed. |

### Remaining risks and actions

| Risk | Next action |
|---|---|
| Yahoo Finance throttling/staleness; HKBU key and service availability. | Keep the 20-ticker cap, show source/freshness, test unavailable responses, and use secrets management on hosting. |
| Backtest simplifications and AI errors. | State assumptions; add transaction costs/dividends, test strategy edge cases, and require human review of AI output. |
| Submission link and historic project record. | Deploy and verify the public app; replace reconstructed boards with dated board records if available. |

**Access link:** Public URL pending — deployment status could not be confirmed. Local-only access after launch is `http://localhost:8501`; this is not a public submission link.

## Discussion and reflection: vibe coding

The team-reported vibe-coding time is approximately **1 hour**, using **GitHub Copilot** (under the assignment limit of 3 hours). This is a reported estimate, not a measured time log. No comparison with other AI tools was provided, so this report does not claim one tool outperformed another.

### What worked well

- Copilot accelerated routine Streamlit scaffolding and implementation of portfolio metrics, strategy visualization, and API error handling.
- The existing multipage app and included CSV made it possible to extend a working prototype instead of building a UI and dataset from scratch.
- A short validation loop found a real mixed-timezone parsing failure; compile checks, Streamlit AppTest, and a local health check provided useful evidence beyond code generation.

### Weaknesses and learning

- Generated code is not automatically correct: the original AI page contained a placeholder authorization value, and the stock-comparison parser failed on mixed UTC offsets. Review and execution surfaced these defects.
- Yahoo Finance and LLM responses are external dependencies; local smoke tests do not prove live data, credentials, rate limits, or model output are reliable.
- Backtests can look persuasive while omitting transaction costs, taxes, slippage, dividends, and data-quality concerns. Results must remain educational, not a buy/sell promise.

### Recommendations

Keep vibe coding time-boxed; write acceptance criteria first; ask the assistant for small, reviewable changes; inspect every API/security-sensitive line; test normal, missing-data, and error paths; and record the time/tool used. Before submission, publish the app, verify the live link without exposing keys, perform a business-team usability review, capture dated scrum-board evidence, and update this draft with actual owners, milestones, blockers, and user feedback.

## Submission status

| Item | Status |
|---|---|
| Idea 1 product implementation | Local prototype and documented enhancements ready for review. |
| Vibe coding limit | Reported 1 hour with Copilot; under the 3-hour limit. |
| Historical Week 1 / team details | Unknown; boards and ten-role map are clearly labeled reconstructed/proposed. |
| Public Streamlit/cloud URL | Not confirmed; add verified public URL after deployment. |
