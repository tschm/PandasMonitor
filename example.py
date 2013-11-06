import sys
import pandas as pd
import numpy as np
import FrameMonitor


# define the reaction. fig is the central figure, table is the table in the lower left corner of the screen
# ts is the timeseries
def func(fig, table, ts):
    ax1 = fig.add_subplot(111)
    ts.cumsum().plot(ax=ax1)
    table.appendSeries(ts.describe())


def random_frame():
    index = pd.DatetimeIndex(freq="D", start="2010/01/01", periods=1000)
    data = np.random.randn(1000, 5)
    return pd.DataFrame(data=data, index=index, columns=["A", "B", "C", "D", "E"])

if __name__ == "__main__":
    app = FrameMonitor.getApp(sys.argv)

    # ex seems to be important
    ex = FrameMonitor.FrameMonitor(random_frame(), func)

    # wait with the exit until the app has stopped
    sys.exit(app.exec_())
