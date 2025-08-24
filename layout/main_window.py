from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QWidget()  # central widget
        self.window_layout = QVBoxLayout()  # main layout
        self.widget.setLayout(self.window_layout)

        self.setCentralWidget(self.widget)  # set central widget
        self.setWindowTitle('Calculadora')  # window title

    def fixed_size(self):
        self.adjustSize()  # adjust window to fit content
        self.setFixedSize(self.width(), self.height())  # lock current size

    def add_widget(self, widget):
        self.window_layout.addWidget(widget)  # add a widget to the layout
