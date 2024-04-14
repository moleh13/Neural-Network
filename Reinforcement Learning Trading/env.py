import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

price_data = pd.read_csv('BTC-USD.csv')

class TradingEnvironment:
    def __init__(self, data_path, initial_cash):
        self.data = pd.read_csv(data_path)
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.position = None
        self.pnl = 0
        self.asset = 0
        self.day = 0
        self.position_day = 0

    def long_position(self):
        if self.position:
            print("You already have a position.")
            return
        else:
            self.position = 'long'
            self.asset = self.cash / self.data['Close'].iloc[self.day]
            self.position_day = self.day

    def close_position(self):
        if not self.position:
            print("You don't have any position to close.")
            return
        else:
            if self.position == 'long':
                self.pnl = self.asset * self.data['Close'].iloc[self.day] - self.data['Close'].iloc[self.position_day] * self.asset
            self.cash += self.pnl
            self.position = None
            self.asset = 0
            print("Position closed. PnL:", self.pnl)
            print("Updated cash balance:", self.cash)

    def step(self, action):
        current_price = self.data['Close'].iloc[self.day]
        unrealized_pnl = self.asset * current_price - self.asset * self.data['Close'].iloc[self.position_day]


        print("Current day:", self.day)
        print("Current price of the asset:", current_price)
        print("Current Asset:", self.asset)
        print("Unrealized PnL:", unrealized_pnl)
        
        if action == 'long':
            self.long_position()
        elif action == 'close':
            self.close_position()
        elif action == 'wait':
            print("Current price of the asset:", current_price)
            pass
        else:
            print("Invalid action.")
        
        print("Current Asset:", self.asset)
        print("Current position:", self.position)
        print("Current cash balance:", self.cash)
        print("***********************************************")
        self.day += 1