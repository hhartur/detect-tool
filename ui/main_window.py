import sys
import json
import os
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QStackedWidget, QFrame, QSplitter, QListWidget,
    QMessageBox, QTabWidget, QListWidgetItem, QCheckBox
)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFontDatabase

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.vulnerability_scanner import VulnerabilityScanner

class ScanWorker(QThread):
    scan_log = Signal(str, str)
    scan_finished = Signal(dict)
    scan_update = Signal(str)

    def __init__(self, scanner, target_url, enable_browser_scan):
        super().__init__()
        self.scanner = scanner
        self.target_url = target_url
        self.enable_browser_scan = enable_browser_scan

    def run(self):
        results = self.scanner.run_full_scan(
            self.target_url,
            log_callback=self.scan_log.emit,
            update_callback=self.scan_update.emit,
            enable_browser_scan=self.enable_browser_scan
        )
        self.scan_finished.emit(results)

class MainWindow(QMainWindow):
    HISTORY_FILE = "history.json"

    def __init__(self):
        super().__init__()
        self.scanner = VulnerabilityScanner()
        self.scan_history = self.load_history()
        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        self.setWindowTitle("Attack Surface Orchestrator")
        self.setGeometry(100, 100, 1600, 900)
        self.setMinimumSize(1200, 700)
        QFontDatabase.addApplicationFont("/:/fonts/FiraCode-Regular.ttf")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        self.stacked_widget = QStackedWidget()
        scan_page = self.create_scan_page()
        history_page = self.create_history_page()
        self.stacked_widget.addWidget(scan_page)
        self.stacked_widget.addWidget(history_page)
        main_layout.addWidget(self.stacked_widget)

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)
        sidebar_layout = QVBoxLayout(sidebar)
        title = QLabel("ORCHESTRATOR")
        title.setObjectName("sidebarTitle")
        sidebar_layout.addWidget(title)
        self.scan_btn = QPushButton(" Nova Varredura")
        self.scan_btn.setCheckable(True)
        self.scan_btn.setChecked(True)
        self.scan_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        sidebar_layout.addWidget(self.scan_btn)
        self.history_btn = QPushButton(" Histórico")
        self.history_btn.setCheckable(True)
        self.history_btn.clicked.connect(self.display_history_page)
        sidebar_layout.addWidget(self.history_btn)
        self.nav_buttons = [self.scan_btn, self.history_btn]
        for btn in self.nav_buttons:
            btn.clicked.connect(self.update_nav_selection)
        sidebar_layout.addStretch()
        return sidebar

    def create_scan_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # URL Input and Scan Button
        url_bar = QFrame()
        url_bar_layout = QHBoxLayout(url_bar)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://alvo.com")
        self.url_input.setObjectName("urlInput")
        url_bar_layout.addWidget(self.url_input)
        self.scan_button = QPushButton("INICIAR VARREDURA")
        self.scan_button.setObjectName("scanButton")
        self.scan_button.clicked.connect(self.start_scan)
        url_bar_layout.addWidget(self.scan_button)
        layout.addWidget(url_bar)

        # New: Browser-based Scan Checkbox
        self.browser_scan_checkbox = QCheckBox("Habilitar Varredura Baseada em Navegador (Playwright)")
        self.browser_scan_checkbox.setChecked(True) # Default to enabled
        self.browser_scan_checkbox.setObjectName("browserScanCheckbox")
        layout.addWidget(self.browser_scan_checkbox)
        
        self.status_frame = QFrame()
        self.status_frame.setFixedHeight(30)
        self.status_frame.setVisible(False)
        status_layout = QHBoxLayout(self.status_frame)
        status_layout.setContentsMargins(0, 5, 0, 5)
        self.status_label = QLabel("Iniciando varredura...")
        self.status_label.setObjectName("statusLabel")
        status_layout.addWidget(self.status_label)
        layout.addWidget(self.status_frame)
        self.results_tabs = QTabWidget()
        self.results_tabs.setVisible(False)
        self.setup_results_tabs()
        layout.addWidget(self.results_tabs)
        return page
        
    def setup_results_tabs(self):
        self.tabs_map = {
            "Sumário de Risco": "summary_results",
            "Descoberta de Superfície": "discovery_results",
        }
        for tab_name, attr_name in self.tabs_map.items():
            tab_widget = QTextEdit()
            tab_widget.setReadOnly(True)
            tab_widget.setObjectName("resultsText")
            setattr(self, attr_name, tab_widget)
            self.results_tabs.addTab(tab_widget, tab_name)

    def create_history_page(self):
        page = QWidget()
        page_layout = QVBoxLayout(page)
        title = QLabel("Histórico de Varreduras")
        title.setObjectName("pageTitle")
        page_layout.addWidget(title)
        splitter = QSplitter(Qt.Horizontal)
        self.history_list_widget = QListWidget()
        self.history_list_widget.itemClicked.connect(self.display_history_item)
        splitter.addWidget(self.history_list_widget)
        self.history_detail_widget = QTextEdit()
        self.history_detail_widget.setReadOnly(True)
        self.history_detail_widget.setObjectName("resultsText")
        splitter.addWidget(self.history_detail_widget)
        splitter.setSizes([300, 700])
        page_layout.addWidget(splitter)
        return page

    def update_nav_selection(self):
        sender = self.sender()
        for btn in self.nav_buttons:
            btn.setChecked(btn == sender)

    def check_prerequisites(self):
        # get_missing_tools now returns an empty list, so this check will always pass
        missing = self.scanner.get_missing_tools()
        if missing:
            QMessageBox.critical(self, "Ferramentas Ausentes", 
                                 f"As seguintes ferramentas não foram encontradas:\n\n{', '.join(missing)}\n\n"
                                 "Por favor, instale-as e garanta que estejam no PATH do sistema.")
            return False
        return True

    def start_scan(self):
        if not self.check_prerequisites():
            return
        url = self.url_input.text().strip()
        if not url.startswith("http"):
            QMessageBox.warning(self, "URL Inválida", "A URL deve iniciar com http:// ou https://.")
            return
        self.scan_button.setEnabled(False)
        self.scan_button.setText("...")
        self.status_frame.setVisible(True)
        self.results_tabs.setVisible(True)
        for attr_name in self.tabs_map.values():
            getattr(self, attr_name).clear()
        
        enable_browser_scan = self.browser_scan_checkbox.isChecked() # Get checkbox state
        self.scan_worker = ScanWorker(self.scanner, url, enable_browser_scan) # Pass to ScanWorker
        self.scan_worker.scan_log.connect(self.update_log_display)
        self.scan_worker.scan_update.connect(lambda msg: self.status_label.setText(f"Atividade: {msg}"))
        self.scan_worker.scan_finished.connect(self.on_scan_finished)
        self.scan_worker.start()
        
    def update_log_display(self, tab_key, log_line):
        tab_attr = self.tabs_map.get(tab_key)
        if tab_attr:
            getattr(self, tab_attr).append(log_line)

    def on_scan_finished(self, result):
        self.scan_button.setEnabled(True)
        self.scan_button.setText("INICIAR VARREDURA")
        self.status_frame.setVisible(False)
        self.display_scan_results(result)
        self.scan_history.insert(0, result)
        self.save_history()

    def display_scan_results(self, result):
        for key, attr_name in self.tabs_map.items():
            report_key = attr_name.replace('_results', '_report')
            getattr(self, attr_name).setText(result.get(report_key, "Nenhum resultado para esta categoria."))
        
    def display_history_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.history_list_widget.clear()
        self.history_detail_widget.clear()
        for scan in self.scan_history:
            item = QListWidgetItem(f"{scan.get('target', 'N/A')}\n{scan.get('timestamp', 'N/A')}")
            item.setData(Qt.UserRole, scan)
            self.history_list_widget.addItem(item)
    
    def display_history_item(self, item):
        scan_data = item.data(Qt.UserRole)
        formatted_history = ""
        # Updated key_order to reflect removed reports
        key_order = ["summary_report", "discovery_report"]
        for key in key_order:
            if key in scan_data:
                title = key.replace('_report', '').replace('_', ' ').upper()
                formatted_history += f"--- {title} ---\n\n{scan_data[key]}\n\n"
        self.history_detail_widget.setText(formatted_history)

    def load_history(self):
        if not os.path.exists(self.HISTORY_FILE): return []
        try:
            with open(self.HISTORY_FILE, "r") as f: return json.load(f)
        except (json.JSONDecodeError, IOError): return []

    def save_history(self):
        try:
            with open(self.HISTORY_FILE, "w") as f: json.dump(self.scan_history, f, indent=4)
        except IOError as e:
            QMessageBox.critical(self, "Erro de Histórico", f"Não foi possível salvar o histórico: {e}")
            
    def apply_theme(self):
        self.setStyleSheet(
            """
            QWidget { background-color: #1c1c1c; color: #e0e0e0; font-family: 'Segoe UI', 'sans-serif'; font-size: 14px; }
            #sidebar { background-color: #161616; border-right: 1px solid #333; }
            #sidebarTitle { color: #00aaff; font-size: 18px; font-weight: bold; padding: 15px; text-align: center; }
            #sidebar QPushButton { background-color: transparent; border: none; color: #a0a0a0; padding: 12px 20px; text-align: left; font-weight: bold; }
            #sidebar QPushButton:hover { background-color: #2a2a2a; color: #ffffff; }
            #sidebar QPushButton:checked { background-color: #252525; color: #00aaff; border-left: 3px solid #00aaff; }
            #urlInput { background-color: #2a2a2a; border: 1px solid #333; padding: 12px; font-size: 16px; color: #e0e0e0; }
            #scanButton { background-color: #007acc; color: white; font-weight: bold; padding: 12px 25px; border: none; }
            #scanButton:hover { background-color: #005a_e; }
            #scanButton:disabled { background-color: #555; }
            #statusLabel { color: #888; }
            #pageTitle { font-size: 20px; font-weight: bold; color: #e0e0e0; }
            QTabWidget::pane { border: 1px solid #333; }
            QTabBar::tab { background: #1c1c1c; color: #aaa; padding: 10px 25px; border: 1px solid #333; border-bottom: none; }
            QTabBar::tab:selected { background: #2a2a2a; color: #fff; }
            QTextEdit, QListWidget { background-color: #212121; border: 1px solid #333; font-family: 'Fira Code', 'monospace'; font-size: 13px; }
            QListWidget::item { padding: 10px; border-bottom: 1px solid #333; }
            QListWidget::item:selected, QListWidget::item:hover { background-color: #2a2a2a; }
            QSplitter::handle { background-color: #333; }
            QSplitter::handle:horizontal { width: 1px; }
            """)