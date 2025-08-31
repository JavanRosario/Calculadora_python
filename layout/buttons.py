from typing import TYPE_CHECKING
from layout.dysplays import Dysplay
from layout.dysplays import Infos
from PySide6.QtWidgets import QPushButton, QGridLayout
from scripts.variables import MEDIUM_FONT
from PySide6.QtCore import Slot
from scripts.utils import valid_num
from math import pow
if TYPE_CHECKING:
    from main_window import MainWindow
    from layout.dysplays import Dysplay
    from main import Infos

class Button(QPushButton):
    """
    Custom QPushButton with preset font and size.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_btn_style()

    def config_btn_style(self):
        """Apply font size, bold style, and minimum size to the button."""
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(50, 50)

class Grid(QGridLayout):
    """
    Custom QGridLayout to manage calculator buttons and logic.

    Attributes:
        dysplay (Dysplay): Display widget.
        info (Infos): Info label widget.
        window (MainWindow): Main application window for error messages.
    """
    def __init__(self, dysplay: Dysplay, info: Infos, window: "MainWindow", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.dysplay = dysplay
        self.info = info
        self.window = window
        self._calcs = ''
        self.calcs = ''
        self._left = None
        self._right = None
        self._operator = None
        self.set_grid()

    @property
    def calcs(self):
        """Update the calculation string and display it in the info label."""
        return self._calcs

    @calcs.setter
    def calcs(self, arg):
        self._calcs = arg
        self.info.setText(arg if arg else '')

    def set_grid(self):
        """
        Set up buttons on the grid and connect signals.
        """
        self.dysplay.eq_triggered.connect(self._eq)
        self.dysplay.backspace_triggered.connect(self.dysplay.backspace)
        self.dysplay.clear_triggered.connect(self.clear)
        self.dysplay.input_triggered.connect(self._insert_to_display)
        self.dysplay.operator_triggered.connect(self._config_left_operator)

        for i, line in enumerate(self.grid_mask):
            for j, column in enumerate(line):
                button = Button(column)

                if column not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self.config_special_buttons(button)

                if column == '0':
                    self.addWidget(button, i, 0, 1, 2)
                else:
                    self.addWidget(button, i, j)

                button.clicked.connect(self.create_slot(
                    self._insert_to_display, column))

    def config_special_buttons(self, button):
        """Configure the logic for special buttons like operators, clear, backspace, and equals."""
        text = button.text()

        if text == 'C':
            slot = self.create_slot(self.clear)
            button.clicked.connect(slot)

        if text in '+-/*^':
            slot = self.create_slot(self._config_left_operator, text)
            button.clicked.connect(slot)

        if text == '=':
            button.clicked.connect(self._eq)

        if text in '◀':
            button.clicked.connect(self.dysplay.backspace)

    def create_slot(self, func, *args, **kwargs):
        """Create a Qt Slot to pass arguments to a function."""
        @Slot()
        def slot():
            func(*args, **kwargs)
        return slot

    @Slot()
    def _insert_to_display(self,  text):
        """Insert numeric or dot input into the display if valid."""
        dysplay_value = self.dysplay.text() + text

        if not valid_num(dysplay_value):
            return
        self.dysplay.insert(text)

        self.dysplay.setFocus()

    # method to receive the clear from "c"
    @Slot()
    def clear(self):
        """Clear the display, info label, and reset calculator state."""
        self.dysplay.clear()
        self.calcs = ''
        self._left = None
        self._right = None
        self._operator = None
        self.info.clear()

    @Slot() 
    def _config_left_operator(self, text):
        """
        Set the left operand and operator when an operator button is pressed.
        """
        dysplay_text = self.dysplay.text()
        self.dysplay.clear()
        
        if dysplay_text == '' and self._left is None:
            self._show_error('Não digitou nada')
            return

        if self._left is None and dysplay_text != '':
            self._left = float(dysplay_text)
        elif self._left is None:
            self._show_error('Número inválido')
            return

        # Handle operator input either from button text or string
        if hasattr(text,'text'):
            self._operator = text.text()
        else:
            self._operator = text
        self.calcs = f'{self._left}{self._operator}??'

    @Slot()
    def _eq(self):
        """
        Execute the calculation when '=' is pressed.
        Handles errors like empty input, invalid numbers, division by zero, and overflow.
        """
        dysplay_text = self.dysplay.text()  

        if dysplay_text == '' and self._left is None:
            self._show_error('Não digitou nada')
            return

        if dysplay_text == '' and self._left is not None:
            self._show_error('Não digitou o segundo número')
            return

        if not valid_num(dysplay_text):
            self._show_error('Valor inválido')
            return

        self._right = float(dysplay_text)

        self.calcs = f'{self._left}{self._operator}{self._right}'
        result = 'error'

        try:
            if '^' in self.calcs and self._left is not None and self._right is not None:
                result = pow(float(self._left), float(self._right))
            else:
                result = eval(self.calcs)

            if isinstance(result, float):
                result = round(result, 3)

            if abs(result) > 1e308:
                self._show_error('Número muito grande! Overflow!')
        
        except (ZeroDivisionError, OverflowError):
            self._show_error('Não é possível dividir por zero.')
            result = 'error'

        self.dysplay.clear()
        self.info.setText(f'{self.calcs} = {result}')

        if result == 'error':
            self._left = None
        else:
            self._left = result

        self._right = None

    def _show_error(self, text):
        """Display an error message box in the main window."""
        msg_box = self.window.msg_box()
        msg_box.setText(text)
        msg_box.setWindowTitle('Erro na execução')
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.exec()
