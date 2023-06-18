import sys
from PyQt6.QtWidgets import *
import pyqtgraph as pg


class BarChart(QMainWindow):
    def __init__(self, value, title):
        super().__init__()
        self.value = value
        self.title = title
        self.setWindowTitle("PyQtGraph")
        self.setGeometry(100, 100, 600, 500)
        self.UiComponents()

        self.show()

    def set_value(self, value):
        self.value = value

    def UiComponents(self):
        widget = QWidget()
        plot = pg.plot()
        plot.setBackground("white")
        # y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2, 0, 20]
        y1 = self.value
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        layout = QGridLayout()
        months = ["   ", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                  "Oct", "Nov", "Dec"]

        bargraph = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='orange')
        plot.addItem(bargraph)

        for i, month in enumerate(months):
            label = QLabel(month)
            layout.addWidget(label, 1, i)

        layout.addWidget(plot, 0, 0, 1, len(months))
        widget.setLayout(layout)
        self.setWindowTitle(self.title)
        self.setFixedSize(600, 500)
        self.setCentralWidget(widget)
