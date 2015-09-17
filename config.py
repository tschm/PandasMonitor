import pandas as pd
import numpy as np


def random_frame():
    index = pd.DatetimeIndex(freq="D", start="2010/01/01", periods=1000)
    data = np.random.randn(1000, 5)
    return pd.DataFrame(data=data, index=index, columns=["A", "B", "C", "D", "E"])


# define the reaction. fig is the central figure, table is the table in the lower left corner of the screen
# ts is the timeseries
def func(ts):
    series = ts.cumsum()
    table = ts.describe()
    return (series, table)


# need to define two variables

# FRAME defines the pandas dataframe used in the display
FRAME = random_frame()

# FUNC defines the function that returns the tuple (x, y) where x is the time series we plot and y is table we print
FUNC = func


