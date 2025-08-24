from PySide6.QtWidgets import QPushButton, QGridLayout
from layout.dysplays import Dysplay
from scripts.variables import MEDIUM_FONT
from PySide6.QtCore import Slot
from scripts.utils import valid_num


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
    def __init__(self, dysplay: Dysplay, *args, **kwargs):
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
        self.set_grid()

    # setting grid buttons

    def set_grid(self):
        for i, line in enumerate(self.grid_mask):
            for j, colum in enumerate(line):
                button = Button(colum)

                # mark special buttons
                if colum not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')

                # make '0' span two columns
                if colum == '0':
                    self.addWidget(button, i, 0, 1, 2)
                else:
                    self.addWidget(button, i, j)

                # Custom connection for button click
                button.clicked.connect(self.dysplay_conection(
                    self.insert_text_in_layout, button))

    # Create slot for signal with arguments
    def dysplay_conection(self, func, *args, **kwargs):
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
