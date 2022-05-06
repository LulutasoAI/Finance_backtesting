from ast import Return
import pandas as pd 
import numpy as np
from utilities import Baseutils
class Back_Test:
    def __init__(self, symbol):
        self.baseutils = Baseutils() #if you want to specify start and end date put here.
        self.dataframe:pd.DataFrame = self.baseutils.fetch_DataFrame(symbol)
    
    def make_returns(self) -> pd.DataFrame:
        prices : pd.DataFrame = self.dataframe["Close"]
        Returns : pd.DataFrame  = np.log(prices/prices.shift(1))
        return Returns

