from bot.core import BasicBot

if __name__ == "__main__":
    bot = BasicBot()

    print("✅ Binance Bot Started")
    print("🔹 BTCUSDT Price:", bot.get_price("BTCUSDT"))
    print("🔹 Account Balance:", bot.get_balance())
