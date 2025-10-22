from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from welcome_widget import WelcomeWidget
from scan_widget import ScanWidget
from settings_widget import SettingsWidget
from help_widget import HelpWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Security Scanner")
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.welcome_tab = WelcomeWidget()
        self.settings_tab = SettingsWidget()
        self.scan_tab = ScanWidget(self.settings_tab)
        self.help_tab = HelpWidget()

        self.tab_widget.addTab(self.welcome_tab, "Welcome")
        self.tab_widget.addTab(self.scan_tab, "Scan")
        self.tab_widget.addTab(self.settings_tab, "Settings")
        self.tab_widget.addTab(self.help_tab, "Help")
