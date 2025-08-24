from PySide6.QtWidgets import QLineEdit
from scripts.variables import BIG_FONT, DEFAUT_MARGIN, MINIUM_WIDTH, SMALL_FONT
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class Dysplay(QLineEdit):
    def __init__(self):
        super().__init__()
        self.config_style()  # set initial appearance

    def config_style(self):
        # set font, alignment, size and margins
        margins = [DEFAUT_MARGIN for margin in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONT}px')
        self.setMinimumHeight(BIG_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setMinimumWidth(MINIUM_WIDTH)


class Calculations(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.config_calc_style()  # apply style

    def config_calc_style(self):
        self.setStyleSheet(f'font-size:{SMALL_FONT}px')  # set font size
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # align text right
