# SrzPumpsBot

A Telegram bot that scans top cryptocurrencies (BTC, ETH, BNB, SOL, XRP) for 1-minute pump/dump signals based on volume and price movement.

## Commands

- `/start` – Get a welcome message
- `/watch` – Start real-time monitoring

## Deployment (Render)

1. Create a new **Web Service** on [Render](https://render.com/)
2. Add your environment variable:
   - `TELEGRAM_TOKEN=your_bot_token`
3. Use these commands:
   - **Build**: `pip install -r requirements.txt`
   - **Start**: `python bot.py`
