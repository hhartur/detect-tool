from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QHBoxLayout, QCheckBox

class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel("<h2>Scan Settings</h2>")
        layout.addWidget(title_label)

        # Scan Depth
        depth_layout = QHBoxLayout()
        depth_label = QLabel("Scan Depth (links to follow):")
        self.scan_depth_spinbox = QSpinBox()
        self.scan_depth_spinbox.setMinimum(1)
        self.scan_depth_spinbox.setMaximum(10)
        self.scan_depth_spinbox.setValue(3) # Default depth
        depth_layout.addWidget(depth_label)
        depth_layout.addWidget(self.scan_depth_spinbox)
        layout.addLayout(depth_layout)

        # Timeout
        timeout_layout = QHBoxLayout()
        timeout_label = QLabel("Request Timeout (seconds):")
        self.timeout_spinbox = QSpinBox()
        self.timeout_spinbox.setMinimum(5)
        self.timeout_spinbox.setMaximum(60)
        self.timeout_spinbox.setValue(10) # Default timeout
        timeout_layout.addWidget(timeout_label)
        timeout_layout.addWidget(self.timeout_spinbox)
        layout.addLayout(timeout_layout)

        # Include Subdomains
        self.include_subdomains_checkbox = QCheckBox("Include Subdomains in Scan")
        self.include_subdomains_checkbox.setChecked(False)
        layout.addWidget(self.include_subdomains_checkbox)

        layout.addStretch() # Push content to the top
