from PyQt4 import QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar


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

    def __init__(self, function):
        QtGui.QWidget.__init__(self)

        grid = QtGui.QGridLayout()
        self.__list = self.__TableWidget()
        self.table = self.__TableWidget()
        self.plot = self.__MatplotlibWidget()

        grid.addWidget(self.__list.table, 1, 0, 1, 2)
        grid.addWidget(self.table.table, 2, 0, 1, 2)
        grid.addWidget(self.plot, 1, 2, 2, 8)

        self.setLayout(grid)
        self.function = function

        QtCore.QObject.connect(self.__list.table, QtCore.SIGNAL("clicked(QModelIndex)"), self.__on_list_clicked)

    def __on_list_clicked(self):
        row = self.__list.selectedRow()
        key = self.__keys[row]
        self.plot.figure.clf()
        self.table.clear()
        self.function(key)
        self.plot.canvas.draw()

    def setKeys(self, keys):
        self.__list.clear()

        for k in keys:
            self.__list.append([k])

        self.__keys = keys