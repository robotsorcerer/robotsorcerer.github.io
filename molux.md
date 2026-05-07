I had eight months of experimenting with various aspects of Ito's stochastic calculus, Black-Scholes models, and modern diffusion schemes with various neural network architectures to improve market odds for a family-owned hedge-fund portfolio management system (more below).


- Built a production-grade analytics and execution stack integrating:
  - real-time market data ingestion (yfinance, NASDAQ APIs)  
  - portfolio P&L attribution and tax-lot tracking  
  - automated options roll and dynamic risk adjustment workflows  

- Designed and operated an automated quantitative trading and portfolio monitoring system, including:
  - real-time intraday alert system driven by implied volatility and options market signals  
  - systematic options strategy execution (covered calls, credit/debit spreads, iron condors, convex structures)  
  - rolling risk exposure tracking (delta, theta, vega) at 5-minute resolution  (on a cron reporting pipeline)
 - trading and portfolio allocation strategies grounded in probabilistic modeling and uncertainty quantification

- Developed probabilistic forecasting models for automated trading on high-frequency contracts in binary prediction markets (e.g., Kalshi). Achieved ~**60% directional accuracy** across structured contracts.

- Incorporated Hamilton–Jacobi reachability–based safety filters into diffusion-driven policies to enforce risk-aware position sizing and maintain safe operating envelopes under high-delta and deep ITM LEAP exposure.

- Implemented cron-based reporting and decision pipelines delivering automated daily summaries across equity, options, and cash positions, enabling disciplined and reproducible trading operations.
