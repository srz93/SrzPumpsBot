import os
import telebot
import time
import ccxt

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
exchange = ccxt.binance()

TOP_COINS = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT', 'XRP/USDT']
ALERTED = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to SrzPumpsBot! Use /watch to start signal monitoring.")

@bot.message_handler(commands=['watch'])
def start_watching(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "🔍 Watching top coins for pump signals...")
    
    def monitor():
        while True:
            for symbol in TOP_COINS:
                try:
                    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=3)
                    if len(ohlcv) < 3:
                        continue

                    prev = ohlcv[-2][4]  # Close of previous candle
                    last = ohlcv[-1][4]  # Close of current candle
                    change_pct = ((last - prev) / prev) * 100

                    if abs(change_pct) > 0.5 and symbol not in ALERTED:
                        direction = "🚀 Pump" if change_pct > 0 else "🔻 Dump"
                        msg = f"{direction} Alert on {symbol}:\nPrice moved {change_pct:.2f}% in 1 min!"
                        bot.send_message(chat_id, msg)
                        ALERTED.add(symbol)

                except Exception as e:
                    print(f"Error checking {symbol}: {e}")
            time.sleep(15)

    import threading
    thread = threading.Thread(target=monitor)
    thread.start()

bot.polling()
