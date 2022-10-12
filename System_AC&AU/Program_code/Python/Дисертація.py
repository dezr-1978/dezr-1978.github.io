import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

def add_label():
    print("add")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
      
    window.setWindowTitle("Магістерська дисертація")
    window.setGeometry(300,300,800,500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Базовий надпис")
    main_text.move(100, 100)
    main_text.adjustSize()
    
    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Buttun")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)
    
    window.show()
    sys.exit(app.exec_())

if  __name__  ==  "__main__":
    application()
