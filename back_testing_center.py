import pandas as pd 
import numpy as np
from utilities import Baseutils
import random
from typing import List, Tuple
class Back_Test:
    def __init__(self, symbol):
        self.baseutils = Baseutils() #if you want to specify start and end date put here.
        self.dataframe:pd.DataFrame = self.baseutils.fetch_DataFrame(symbol)
        self.prices : pd.DataFrame = self.dataframe["Close"]
    
    def make_returns(self) -> pd.DataFrame:
        prices :pd.DataFrame = self.prices
        Returns : pd.DataFrame  = np.log(prices/prices.shift(1))
        return Returns

    def make_random_positions(self) -> List[int]:
        """
        Replace this with a real model
        """
        strategy = [] 
        for i in range(len(self.prices)):
            strategy.append(random.randint(-1,1))
        return np.array(strategy)
            

