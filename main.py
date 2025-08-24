from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from scripts.variables import ICON_DIR
from dysplays import Dysplay, Calculations
from styles.styles import setup_theme
import ctypes
import sys

if __name__ == '__main__':
    # fix icon bug on windows
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        myappid)  # Windows app ID for taskbar icon fix

    app = QApplication(sys.argv)  # main app instance
    window = MainWindow()  # main window
    # applying dark theme
    setup_theme(app)

    calculations = Calculations('2+4')  # create label with text
    window.add_widget(calculations)  # add label to the window

    dysplay = Dysplay()  # custom widget
    window.add_widget(dysplay)  # add widget to window layout

    icon = QIcon(str(ICON_DIR))  # load app icon
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    window.fixed_size()  # fix window size
    window.show()  # display window
    app.exec()  # run application loop
