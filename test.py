import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QScrollArea

class ScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QScrollArea Example')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        # Create a widget to hold the elements inside the scroll area
        self.scrollWidget = QWidget()
        self.scrollArea.setWidget(self.scrollWidget)

        self.scrollLayout = QVBoxLayout(self.scrollWidget)

        # Add some example elements to the scroll area
        for i in range(20):
            self.scrollLayout.addWidget(QTextEdit(f"Text {i+1}"))

        self.clearButton = QPushButton('Clear ScrollArea')
        self.clearButton.clicked.connect(self.clearScrollArea)

        layout.addWidget(self.scrollArea)
        layout.addWidget(self.clearButton)

        self.setLayout(layout)

    def clearScrollArea(self):
        # Clear all elements inside the scroll area
        for i in reversed(range(self.scrollLayout.count())):
            widgetToRemove = self.scrollLayout.itemAt(i).widget()
            self.scrollLayout.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScrollAreaExample()
    ex.show()
    sys.exit(app.exec_())
