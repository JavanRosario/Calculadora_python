from typing import TYPE_CHECKING
from layout.dysplays import Dysplay
from layout.dysplays import Infos
from PySide6.QtWidgets import QPushButton, QGridLayout
from scripts.variables import MEDIUM_FONT
from PySide6.QtCore import Slot
from scripts.utils import valid_num

if TYPE_CHECKING:
    from layout.dysplays import Dysplay
    from main import Infos


# custom button class
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
        # self.setProperty('cssClass', 'specialButton')


# custom grid layout class
class Grid(QGridLayout):
    def __init__(self, dysplay: Dysplay, info: Infos, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # define grid button layout
        self.grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.dysplay = dysplay
        self.info = info
        self._calcs = ''
        self.calcs = 'teste'
        self.set_grid()

    @property
    def calcs(self):
        return self._calcs

    @calcs.setter
    def calcs(self, arg):
        self._calcs = arg

    # setting grid buttons
    def set_grid(self):
        for i, line in enumerate(self.grid_mask):
            for j, colum in enumerate(line):
                button = Button(colum)

                # mark special buttons
                if colum not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self.config_special_buttons(button)

                # make '0' span two columns
                if colum == '0':
                    self.addWidget(button, i, 0, 1, 2)
                else:
                    self.addWidget(button, i, j)

                # Custom connection for button click
                button.clicked.connect(self.create_slot(
                    self.insert_text_in_layout, button))

    # special button logic
    def config_special_buttons(self, button):
        text = button.text()

        if text == 'C':
            slot = self.create_slot(self.clear)
            button.clicked.connect(slot)

    # Create slot for signal with arguments
    def create_slot(self, func, *args, **kwargs):
        @Slot()
        def slot():
            func(*args, **kwargs)
        return slot

    # Insert button text into display
    def insert_text_in_layout(self,  button):
        button_text = button.text()
        dysplay_value = self.dysplay.text() + button_text

        if not valid_num(dysplay_value):
            return
        self.dysplay.insert(button_text)

    # method to receive the clear from "c"
    def clear(self):
        self.dysplay.clear()
