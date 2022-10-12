import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

class Window (QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Магістерська дисертація")
        self.setGeometry(300, 300, 800, 500)

        self.new_text = QtWidgets.QLabel(self)

        self_text = QtWidgets.QLabel(self)
        self_text.setText("Базовий надпис")
        self_text.move(100, 100)
        self_text.adjustSize()

        self = QtWidgets.QPushButton(self)
        self.move(70, 150)
        self.setText("Buttun")
        self.setFixedWidth(200)
        self.clicked.connect(add_label)


def add_label(self):
    self.new_text.setText("HADPUC")
    self.new_text.move(100, 50)
    self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

