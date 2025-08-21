from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from scripts.path import ICON_DIR
import ctypes
import sys

if __name__ == '__main__':
    # fix icon bug on windows
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    icon = QIcon(str(ICON_DIR))
    app.setWindowIcon(icon)
    window = MainWindow()
    # window.fixed_size()
    window.setWindowIcon(icon)

    window.show()
    app.exec()
