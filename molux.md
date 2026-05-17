- Production-grade analytics and execution stack single UI:
  - real-time market data ingestion (yfinance, NASDAQ APIs)  
  - portfolio P&L attribution and tax-lot tracking  
  - automated options close/roll-(out/up) for dynamic risk adjustment workflows  

- Automated quantitative trading and portfolio monitoring system, including:
  - real-time intraday alert system driven by IV and options Greeks  
  - systematic options strategy execution including (poor man's) covered calls, credit/debit vertical and diagonal spreads, iron condors, convex structures  
  - rolling risk exposure tracking (delta, theta, vega) all rolled into a cron reporting pipeline
  - trading and portfolio allocation strategies grounded in probabilistic modeling, stochastic optimal control, and uncertainty quantification

- Probabilistic forecasting models for automated trading on high-frequency contracts in binary prediction markets (e.g., Kalshi). 
  - Incorporated Hamilton–Jacobi reachability–based safety filters for risk-aware position sizing and for maintaining safe operating envelopes under dynamically changing thetas, deltas, gammas with deep ITM LEAP exposure.

- Automated reporting and decision-making pipelines delivering automated daily summaries across equity, options, and cash positions --- informing disciplined and reproducible trading operations.
