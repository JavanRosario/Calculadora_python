from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from scripts.variables import BIG_FONT, DEFAUT_MARGIN, MINIUM_WIDTH, SMALL_FONT
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt,Signal
from scripts.utils import is_empty,is_num_or_dot

class Dysplay(QLineEdit):
    # Custom signals for specific calculator events
    eq_triggered = Signal()
    backspace_triggered = Signal()
    clear_triggered = Signal()
    input_triggered = Signal(str)
    operator_triggered = Signal(str)

    def __init__(self):
        super().__init__()
        self.config_style()  # set initial appearance

    def config_style(self):
        """Configure font, alignment, margins, and minimum size of the display."""
        margins = [DEFAUT_MARGIN for margin in range(4)]
        self.setStyleSheet(f'font-size:{BIG_FONT}px')
        self.setMinimumHeight(BIG_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        self.setMinimumWidth(MINIUM_WIDTH)

    def keyPressEvent(self, ev: QKeyEvent) -> None:
        """
        Override key press event to capture specific inputs.
        Emits custom signals based on key type.
        """
        text = ev.text().strip()
        key = ev.key()
        KEYS = Qt.Key

        # Identify key types
        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        is_backspace = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_esc = key in [KEYS.Key_Escape]
        is_operator = key in [KEYS.Key_AsciiCircum,KEYS.Key_Plus,KEYS.Key_Minus,
                              KEYS.Key_Slash,KEYS.Key_Asterisk,KEYS.Key_P]

        # Emit corresponding signals for key presses
        if is_enter:
            self.eq_triggered.emit()
            return ev.ignore()
        
        if is_backspace:
            self.backspace_triggered.emit()
            return ev.ignore()
        
        if is_esc:
            self.clear_triggered.emit()
            return ev.ignore()
        
        if is_operator:
            # Convert 'p' to '^' for exponentiation
            if text.lower() == 'p':
                text = '^'
            self.operator_triggered.emit(text)
            return ev.ignore()
        
        if is_empty(text):
            return ev.ignore()
        
        if is_num_or_dot(text):
            self.input_triggered.emit(text)
            return ev.ignore()

class Infos(QLabel):
    """Label to display intermediate calculation information on the calculator."""
    def __init__(self, text):
        super().__init__(text)
        self.config_calc_style()  # apply style

    def config_calc_style(self):
        """Configure appearance of the information label."""
        self.setStyleSheet(f'font-size:{SMALL_FONT}px')  # set font size
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # align text right

    