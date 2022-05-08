import pandas as pd 
import numpy as np
from back_testing_center import Back_Test 

class SMA_related:
    """
    
    """
    def __init__(self) -> None:
        pass 
    
    def process_prices(self,price_data:pd.Series,sma_setting_1:int,sma_setting_2:int) -> pd.DataFrame:
        """
        high level.
        """
        data = self.add_sma(price_data,sma_setting_1,sma_setting_2)
        data = self.add_decisions(data)
        return data

    def add_sma(self,data:pd.Series,sma_setting_1:int,sma_setting_2:int) -> pd.DataFrame:
        if sma_setting_1 <= sma_setting_2:
            temporal = sma_setting_2 
            sma_setting_2 = sma_setting_1
            sma_setting_1 = temporal
            del temporal #w/e
        result = pd.DataFrame()
        result["price"] = data
        result["SMA_1".format(sma_setting_1)] = data.rolling(sma_setting_1).mean()
        result["SMA_2".format(sma_setting_2)] = data.rolling(sma_setting_2).mean()
        return result 
    
    def add_decisions(self,data:pd.DataFrame) -> pd.DataFrame:
        data["position"] = np.where(data["SMA_1"] > data["SMA_2"],1,-1)
        return data

    def back_test_main(self,symbol):
        backtest = Back_Test(symbol)
        data = self.process_prices(backtest.prices,14,233)
        data["returns"] = backtest.make_returns()
        backtest.make_result(data)


