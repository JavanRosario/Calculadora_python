from PySide6.QtWidgets import QPushButton
from scripts.variables import MEDIUM_FONT


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_btn_style()

    def config_btn_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(50, 50)
        self.setProperty('cssClass', 'specialButton')
