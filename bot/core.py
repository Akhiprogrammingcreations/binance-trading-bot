from binance.client import Client
from binance.enums import *
import logging
import json

class BasicBot:
    def __init__(self, config_path="config/config.json"):
        with open(config_path) as f:
            config = json.load(f)

        self.client = Client(config["API_KEY"], config["API_SECRET"], testnet=True)
        self.client.FUTURES_URL = config["BASE_URL"] + "/fapi"
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger("BinanceBot")
        handler = logging.FileHandler("logs/bot.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.upper() == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.logger.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing market order: {e}")
            return None

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            self.logger.info(f"Account balance: {balance}")
            return balance
        except Exception as e:
            self.logger.error(f"Error getting balance: {e}")
            return None

    def get_price(self, symbol):
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            self.logger.info(f"Price for {symbol}: {price}")
            return price
        except Exception as e:
            self.logger.error(f"Error getting price: {e}")
            return None
