from PyQt5.QtWidgets import *
def test_main():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec_()
