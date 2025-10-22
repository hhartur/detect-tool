import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from PySide6.QtCore import QObject, Signal
import security_modules.xss_scanner as XSSScanner

class Scanner(QObject):
    scan_progress = Signal(str)
    scan_finished = Signal()

    def __init__(self, scan_depth=3, timeout=10, include_subdomains=False):
        super().__init__()
        self.scan_depth = scan_depth
        self.timeout = timeout
        self.include_subdomains = include_subdomains
        self.visited_urls = set()
        self.found_vulnerabilities = []
        self._running = False

    def start_scan(self, target_url):
        self._running = True
        self.found_vulnerabilities = []
        self.visited_urls = set()
        self.base_url = target_url # Set base_url here
        self._crawl(self.base_url, 0)
        self.scan_finished.emit()

    def _crawl(self, url, depth):
        if not self._running or depth > self.scan_depth or url in self.visited_urls:
            return

        self.visited_urls.add(url)
        self.scan_progress.emit(f"Crawling: {url} (Depth: {depth})")

        try:
            response = requests.get(url, timeout=self.timeout)
            if response.status_code == 200 and 'text/html' in response.headers.get('Content-Type', ''):
                soup = BeautifulSoup(response.text, 'html.parser')
                self._find_links(soup, url, depth)
                self._find_forms(soup, url, depth) # Call _find_forms here
                # self._find_js_event_listeners(soup, url) # To be implemented
                self._run_security_checks(url, response)

        except requests.exceptions.RequestException as e:
            self.scan_progress.emit(f"Error crawling {url}: {e}")

    def _find_links(self, soup, current_url, depth):
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            absolute_link = urljoin(current_url, link)
            parsed_link = urlparse(absolute_link)
            parsed_base = urlparse(self.base_url)

            # Only follow links within the same domain or subdomain if allowed
            if parsed_link.netloc == parsed_base.netloc or \
               (self.include_subdomains and parsed_link.netloc.endswith(f'.{parsed_base.netloc}')):
                self._crawl(absolute_link, depth + 1)

    def _find_forms(self, soup, current_url, depth):
        for form in soup.find_all('form'):
            action = form.get('action')
            method = form.get('method', 'get').lower()
            form_url = urljoin(current_url, action)

            inputs = {}
            for input_tag in form.find_all(['input', 'textarea']):
                input_name = input_tag.get('name')
                input_type = input_tag.get('type', 'text')
                input_value = input_tag.get('value', '')

                if input_name:
                    inputs[input_name] = input_value

            self.scan_progress.emit(f"Found form: {method.upper()} {form_url} with fields: {list(inputs.keys())}")

            # Test each input field with various payloads
            for input_name in inputs.keys():
                self._test_form_input(form_url, method, inputs, input_name)

    def _test_form_input(self, form_url, method, base_inputs, test_input_name):
        self.scan_progress.emit(f"Testing input '{test_input_name}' in form {form_url} ({method.upper()})")

        for payload in XSSScanner.XSS_PAYLOADS:
            test_inputs = base_inputs.copy()
            test_inputs[test_input_name] = payload

            try:
                if method == 'post':
                    response = requests.post(form_url, data=test_inputs, timeout=self.timeout)
                else: # Assume GET for now, though forms can specify other methods
                    response = requests.get(form_url, params=test_inputs, timeout=self.timeout)

                # Pass the response to security checks
                self._run_security_checks(form_url, response) # Re-use existing security checks

            except requests.exceptions.RequestException as e:
                self.scan_progress.emit(f"Error submitting form {form_url} with payload '{payload}' in {test_input_name}: {e}")

    def _find_js_event_listeners(self, soup, url):
        # This is a complex task that often requires a headless browser (e.g., Selenium)
        # For a basic implementation, we might look for common JS event attributes (onclick, etc.)
        # or parse <script> tags, but a full solution is beyond a simple BeautifulSoup approach.
        pass

    def _run_security_checks(self, url, response):
        # Run XSS scan
        xss_vulnerabilities = XSSScanner.XSSScanner.scan(url, response)
        if xss_vulnerabilities:
            self.found_vulnerabilities.extend(xss_vulnerabilities)
            for vul in xss_vulnerabilities:
                self.scan_progress.emit(f"Vulnerability Found: {vul['type']} - {vul['description']} at {vul['url']}")

    def stop_scan(self):
        self._running = False
