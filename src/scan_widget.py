from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QProgressBar, QMessageBox
from PySide6.QtCore import Signal
from scanner import Scanner

class ScanWidget(QWidget):
    scan_requested = Signal(str)

    def __init__(self, settings_widget):
        super().__init__()
        self.settings_widget = settings_widget
        self.scanner = Scanner(
            scan_depth=self.settings_widget.scan_depth_spinbox.value(),
            timeout=self.settings_widget.timeout_spinbox.value(),
            include_subdomains=self.settings_widget.include_subdomains_checkbox.isChecked()
        )
        self.init_ui()
        self.scanner.scan_progress.connect(self.update_scan_output)
        self.scanner.scan_finished.connect(self.scan_complete)

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # URL Input
        url_layout = QHBoxLayout()
        url_label = QLabel("Target URL:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("e.g., https://example.com")
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        # Scan Buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Scan")
        self.stop_button = QPushButton("Stop Scan")
        self.stop_button.setEnabled(False) # Initially disabled
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Results Display
        results_label = QLabel("Scan Results:")
        layout.addWidget(results_label)
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        layout.addWidget(self.results_display)

        self.start_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.scanner.stop_scan)

    def start_scan(self):
        target_url = self.url_input.text()
        if not target_url:
            QMessageBox.warning(self, "Input Error", "Please enter a target URL.")
            return

        # Basic URL validation using regex
        import re
        url_pattern = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
            r'localhost|' # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not url_pattern.match(target_url):
            QMessageBox.warning(self, "Input Error", "Please enter a valid URL (e.g., https://example.com).")
            return

        self.results_display.clear()
        self.results_display.append(f"Starting scan for: {target_url}...")
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.url_input.setEnabled(False)
        self.scanner.start_scan(target_url)

    def update_scan_output(self, message):
        self.results_display.append(message)

    def scan_complete(self):
        self.results_display.append("Scan complete.")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.url_input.setEnabled(True)
        QMessageBox.information(self, "Scan Complete", "The scan has finished.")
