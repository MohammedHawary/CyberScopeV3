from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chart = QChart()
        self.chart.setObjectName('test')
        self.chart_view = QChartView(self.chart)

        self.button = QPushButton("Change Color")
        self.button.clicked.connect(self.change_chart_background)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def change_chart_background(self):
        self.chart.setBackgroundBrush(QColor("red"))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
