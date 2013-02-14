from PyQt4 import QtGui
import sys
import PandasWidget
import pandas, numpy

class StoreMonitor(QtGui.QMainWindow):
    def __init__(self, frame):
        super(StoreMonitor, self).__init__()
        self.__widget = PandasWidget.PandasWidget(self.react)
        self.__widget.setKeys(frame.keys())
        self.frame = frame
        self.setCentralWidget(self.__widget)
        self.setWindowTitle("Pandas Dataframe Monitor")
        self.show()

    def react(self, key):
        ts = self.frame[key]
        ts = ts.dropna()
        ax1 = self.__widget.plot.figure.add_subplot(111)

        ts.plot(ax = ax1)
        ax1.set_title(key)

        x = ts.describe()

        self.__widget.table.clear()
        for s in x.index:
            self.__widget.table.append([s,x[s]])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    index = pandas.DatetimeIndex(freq = "D", start="2010/01/01",periods=1000)
    data  = numpy.random.randn(1000,5)

    A = pandas.DataFrame(data = data, index = index, columns = ["A","B","C","D","E"])
    ex = StoreMonitor(A)

    sys.exit(app.exec_())
