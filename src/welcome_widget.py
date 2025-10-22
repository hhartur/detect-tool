from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        welcome_label = QLabel("<h1>Welcome to the Web Security Scanner!</h1>")
        welcome_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcome_label)

        info_label = QLabel("This tool helps you scan websites for common security vulnerabilities.\n\nNavigate through the tabs to start a scan, configure settings, or get help.")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setWordWrap(True)
        layout.addWidget(info_label)

