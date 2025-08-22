from PySide6.QtWidgets import QLineEdit
from scripts.variables import BIG_FONT, DEFAUT_MARGIN, MINIUM_WIDTH
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
