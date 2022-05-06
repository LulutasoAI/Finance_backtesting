from utilities import Baseutils
from back_testing_center import Back_Test
from matplotlib import pyplot as plt
import numpy as np
class Test:
    def __init__(self) -> None:
        pass
    def test_main(self):
        result = []
        result.append(self.Baseutils_test())
        result.append(self.Back_Test_test())
        if False in result:
            print("failed")
            return False
        else:
            print("passed")
            return True 


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
        
        backtest = Back_Test("TM")
        last = 100
        returns = backtest.make_returns()
        print(returns)
        strategy = backtest.make_random_positions()
        profit = returns.shift(1)*strategy
        plt.plot(returns[-last:])
        plt.plot(profit[-last:])
        plt.show()
        print(backtest.prices[0]*np.sum(returns),"normal")
        print(10000*np.sum(profit),"strat")
        return True

if __name__ == "__main__":
    Test().test_main()
