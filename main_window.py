from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.window_layout = QVBoxLayout()
        self.widget.setLayout(self.window_layout)

        self.setCentralWidget(self.widget)
        self.setWindowTitle('Calculadora')

    def fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
