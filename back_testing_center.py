import pandas as pd 
import numpy as np
from utilities import Baseutils
import random
from typing import List, Tuple
from matplotlib import pyplot as plt

class Back_Test:
    def __init__(self, symbol):
        self.baseutils = Baseutils() #if you want to specify start and end date put them here.
        self.dataframe:pd.DataFrame = self.baseutils.fetch_DataFrame(symbol)
        self.prices : pd.DataFrame = self.dataframe["Close"]
    
    def make_returns(self) -> pd.DataFrame:
        prices :pd.Series = self.prices
        Returns : pd.Series  = np.log(prices/prices.shift(1))
        return Returns

    def make_random_positions(self) -> List[int]:
        """
        Replace this with a real model
        """
        strategy = [] 
        for i in range(len(self.prices)):
            strategy.append(random.randint(-1,1))
        return np.array(strategy)
    
    
    def make_result(self,data:pd.DataFrame):
        last = 100
        data["profit"] = data["returns"].shift(1)*data["position"]
        plt.plot(data["returns"][-last:])
        plt.plot(data["profit"][-last:])
        plt.show()
        original_capital = 10000 
        result_profit = original_capital * np.exp(np.sum(data["profit"]))
        hold_profit = original_capital * np.exp(np.sum(data["returns"]))
        print(int(result_profit-original_capital),"result_profit with strat")
        print(int(hold_profit-original_capital),"theoretical profit when holding until the last day in data.")
