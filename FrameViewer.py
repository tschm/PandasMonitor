import sys
import pandas
import numpy

import PandasWidget


# define the reaction. fig is the central figure, table is the table in the lower left corner of the screen
# ts is the timeseries
def func(fig, table, ts):
    ax1 = fig.add_subplot(111)
    ts.cumsum().plot(ax=ax1)
    table.appendSeries(ts.describe())


def random_frame():
    index = pandas.DatetimeIndex(freq="D", start="2010/01/01", periods=1000)
    data = numpy.random.randn(1000, 5)
    return pandas.DataFrame(data=data, index=index, columns=["A", "B", "C", "D", "E"])

if __name__ == "__main__":
    app = PandasWidget.getApp(sys.argv)

    # ex seems to be important
    ex = PandasWidget.FrameMonitor(random_frame(), func)

    # wait with the exit until the app has stopped
    sys.exit(app.exec_())
