from PySide6.QtWidgets import QPushButton, QGridLayout
from scripts.variables import MEDIUM_FONT


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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # define grid button layout
        self.grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
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
