from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.fixed_size()
    window.show()
    app.exec()
