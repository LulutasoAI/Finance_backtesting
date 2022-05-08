from utilities import Baseutils
from back_testing_center import Back_Test
from SMA import SMA_related
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

class Test:
    def __init__(self) -> None:
        pass
    def test_main(self):
        result = []
        result.append(self.Baseutils_test())
        result.append(self.Back_Test_test())
        result.append(self.SMA_related_test())
        if False in result:
            print("failed")
            return False
        else:
            print("passed")
            return True 

    def SMA_related_test(self):
        try:
            sma_related = SMA_related()
            
            sma_related.back_test_main("NEE")
            return True
        except Exception as e:
            print(e)
            return False

    def Baseutils_test(self):
        baseutil = Baseutils()
        try:
            dataframe = baseutil.fetch_DataFrame("TM")
            print(dataframe)
            return True
        except Exception as e:
            print(e)
            return False

    def Back_Test_test(self):
        
        backtest = Back_Test("NEE")
        last = 30
        returns = backtest.make_returns()
        print(returns)
        strategy = backtest.make_random_positions()
        profit = returns.shift(1)*strategy
        data = pd.DataFrame()
        #data["prices"] = backtest.prices[-last:]
        ##data["returns"] = returns[-last:]
        ##data["profit"] = profit[-last:]
        #data["position"] = strategy[-last:]
        #plt.plot(returns[-last:])
        #plt.plot(profit[-last:])
        
        #plt.plot(strategy[-last:])
        #plt.show()
        #ax = data.plot(secondary_y="Position",figsize=(10,6))
        #ax.get_legend().set_bbox_to_anchor((0.25,0.85))
        #ax.figure.show()
        
        theoretical_latest = backtest.prices[0]*np.exp(np.sum(returns))
        the_latest = backtest.prices[-1]
        print(backtest.prices[0],"first price")
        print(theoretical_latest,"hold")
        print(the_latest,"the latest price")
        print(10000*np.exp(np.sum(profit)),"strat")
        print(type(backtest.prices))
        if round(theoretical_latest,2) == round(the_latest,2):
            print("logged return test ok")
            return True
        else:
            return False

if __name__ == "__main__":
    Test().test_main()
