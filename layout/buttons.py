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
        self.calcs = ''
        self._left = None
        self._right = None
        self._operator = None
        self.set_grid()

    @property
    def calcs(self):
        return self._calcs

    @calcs.setter
    def calcs(self, arg):
        self._calcs = arg
        self.info.setText(arg if arg else '')

    # setting grid buttons
    def set_grid(self):
        for i, line in enumerate(self.grid_mask):
            for j, column in enumerate(line):
                button = Button(column)

                # mark special buttons
                if column not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self.config_special_buttons(button)

                # make '0' span two columns
                if column == '0':
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

        if text in '+-/*':
            slot = self.create_slot(self._operator_clicked, button)
            button.clicked.connect(slot)

        if text in '=':
            button.clicked.connect(self._eq)

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
        self.calcs = ''
        self._left = None
        self._right = None
        self._operator = None
        self.info.clear()

    # logic for calculation information
    def _operator_clicked(self, button):
        text = button.text()
        dysplay_text = self.dysplay.text()
        self.dysplay.clear()

        # if display is not a valid number and no left operand exists, do nothing
        if not valid_num(dysplay_text) and self._left is None:
            return

        # assign left operand only if it's not already set and display is not empty
        if self._left is None and dysplay_text != '':
            # left gets a new display text value
            self._left = int(dysplay_text)

        # store the selected operator
        self._operator = text
        # update calculation string with left operand and operator
        self.calcs = f'{self._left}{self._operator}??'

    def _eq(self):
        dysplay_text = self.dysplay.text()  # get current display text

        # if display is not a valid number, stop execution
        if not valid_num(dysplay_text):
            return

        # assign right operand
        self._right = int(dysplay_text)
        # build the calculation expression as a string
        self.calcs = f'{self._left}{self._operator}{self._right}'

        try:
            # evaluate the expression
            result = eval(self.calcs)
        except ZeroDivisionError:
            # handle division by zero
            result = ''

        # clear display and show result in info label
        self.dysplay.clear()
        self.info.setText(f'{self.calcs} = {result}')
        # prepare for next calculation: store result as new left operand
        self._left = result
        self._right = None
