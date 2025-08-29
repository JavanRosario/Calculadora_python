from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox


# main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # central widget and layout
        self.widget = QWidget()
        self.window_layout = QVBoxLayout()
        self.widget.setLayout(self.window_layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle('Calculadora')

    # lock window size after adjusting
    def fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # add widget to main layout
    def add_widget(self, widget: QWidget):
        self.window_layout.addWidget(widget)

    def msg_box(self):
        return QMessageBox(self)
