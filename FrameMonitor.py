from PyQt4 import QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar


def getApp(args):
    return QtGui.QApplication(args)


class FrameMonitor(QtGui.QMainWindow):
    def __init__(self, frame, function):
        super(FrameMonitor, self).__init__()
        self.widget = PandasWidget(frame, function)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Pandas Dataframe Monitor")
        self.show()


class PandasWidget(QtGui.QWidget):
    class __MatplotlibWidget(QtGui.QWidget):
        def __init__(self):
            QtGui.QWidget.__init__(self)

            self.figure = Figure((10.0, 6.0), dpi=100)
            self.canvas = FigureCanvas(self.figure)
            self.canvas.setParent(self)
            self.__toolbar = NavigationToolbar(self.canvas, self)

    class __TableWidget(QtGui.QWidget):
        def __init__(self):
            QtGui.QWidget.__init__(self)

            self.table = QtGui.QTableView()
            self.clear()

        def clear(self):
            self.__model = QtGui.QStandardItemModel()

        def append(self, items):
            x = [QtGui.QStandardItem(str(item)) for item in items]
            self.__model.appendRow(x)
            self.table.setModel(self.__model)

        def appendSeries(self, series):
            for s in series.index:
                self.append([s, series[s]])

        def selectedRow(self):
            return self.table.selectedIndexes()[0].row()

    def __init__(self, frame, function):
        QtGui.QWidget.__init__(self)

        grid = QtGui.QGridLayout()

        self.list = self.__TableWidget()
        self.table = self.__TableWidget()
        self.plot = self.__MatplotlibWidget()

        grid.addWidget(self.list.table, 1, 0, 1, 2)
        grid.addWidget(self.table.table, 2, 0, 1, 2)
        grid.addWidget(self.plot, 1, 2, 2, 8)

        self.setLayout(grid)
        self.function = function

        self.frame = frame
        self.__setKeys(frame.keys())

        QtCore.QObject.connect(self.list.table, QtCore.SIGNAL("clicked(QModelIndex)"), self.__on_list_clicked)

    def __on_list_clicked(self):
        row = self.list.selectedRow()
        key = self.__keys[row]
        self.plot.figure.clf()
        self.table.clear()
        ax1 = self.plot.figure.add_subplot(111)
        #xxx = self.function(self.frame[key])
        # print(xxx)
        (p, t) = self.function(self.frame[key])
        print(p)
        print(t)
        p.plot(ax=ax1)
        self.table.appendSeries(t)
        # self.function(self.plot.figure, self.table, self.frame[key])
        self.plot.canvas.draw()

    def __setKeys(self, keys):
        self.list.clear()

        for k in keys:
            self.list.append([k])

        self.__keys = keys
