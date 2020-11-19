from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class MyWindow(QtWidgets.QMainWindow):
    """Auto-closing window"""
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        QtCore.QTimer.singleShot(3000, self.close)

def test_main():
    app = QtWidgets.QApplication(sys.argv)
    my_win = MyWindow()
    my_win.show()
    sys.exit(app.exec_())
