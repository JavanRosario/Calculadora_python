from PySide6.QtWidgets import QApplication
from layout.main_window import MainWindow
from PySide6.QtGui import QIcon
from scripts.variables import ICON_DIR
from layout.dysplays import Dysplay, Infos
from layout.buttons import Grid
from layout.styles import setup_theme
import ctypes
import sys

if __name__ == '__main__':
    # fix Windows taskbar icon
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        myappid)

    # create main application
    app = QApplication(sys.argv)
    window = MainWindow()

    # applying dark theme
    setup_theme(app)

    # create label widget
    info = Infos('Sua conta')
    window.add_widget(info)

    # create input widget
    dysplay = Dysplay()
    window.add_widget(dysplay)

    # add grid layout
    grid = Grid(dysplay, info, window)
    window.window_layout.addLayout(grid)

    # set app icon
    icon = QIcon(str(ICON_DIR))  # load app icon
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    window.fixed_size()  # fix window size
    window.show()  # display window
    app.exec()  # run application loop
