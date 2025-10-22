from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextBrowser
from PySide6.QtCore import Qt

class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel("<h2>Help & Information</h2>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        help_content = """
        <h3>About This Tool</h3>
        <p>This Web Security Scanner is designed to help identify common vulnerabilities in web applications. It performs various checks, including:</p>
        <ul>
            <li><b>URL Discovery:</b> Crawls the target website to find accessible links and resources.</li>
            <li><b>XSS (Cross-Site Scripting) Detection:</b> Attempts to inject malicious scripts to test for XSS vulnerabilities.</li>
            <li><b>SQL Injection Detection:</b> Tries to inject SQL commands to test for database vulnerabilities.</li>
            <li><b>Broken Link Checker:</b> Identifies broken or inaccessible links.</li>
            <li><b>Header Analysis:</b> Checks for security-related HTTP headers.</li>
        </ul>

        <h3>How to Use</h3>
        <ol>
            <li>Go to the 'Scan' tab.</li>
            <li>Enter the target URL (e.g., <code>https://example.com</code>) in the input field.</li>
            <li>(Optional) Adjust scan settings in the 'Settings' tab (e.g., scan depth, timeout).</li>
            <li>Click 'Start Scan' to begin the process.</li>
            <li>Monitor the progress and review the results in the 'Scan Results' area.</li>
        </ol>

        <h3>Web Security Basics</h3>
        <p>Web security is crucial for protecting websites and web applications from various cyber threats. Common attack types include:</p>
        <ul>
            <li><b>Cross-Site Scripting (XSS):</b> Attackers inject client-side scripts into web pages viewed by other users.</li>
            <li><b>SQL Injection (SQLi):</b> Attackers manipulate database queries to gain unauthorized access or control.</li>
            <li><b>Cross-Site Request Forgery (CSRF):</b> Attackers trick users into performing actions they didn't intend.</li>
            <li><b>Broken Authentication:</b> Weak authentication mechanisms allow attackers to compromise user accounts.</li>
            <li><b>Security Misconfiguration:</b> Improperly configured servers or applications expose vulnerabilities.</li>
        </ul>
        <p>Always ensure your web applications are up-to-date, use strong authentication, validate all user input, and implement proper security headers.</p>
        """

        self.help_browser = QTextBrowser()
        self.help_browser.setHtml(help_content)
        layout.addWidget(self.help_browser)
