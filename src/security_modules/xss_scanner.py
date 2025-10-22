class XSSScanner:
    XSS_PAYLOADS = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg/onload=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<iframe src=javascript:alert('XSS')></iframe>",
        "<p onmouseover=alert('XSS')>Hover over me</p>",
        "'';!--\"<XSS>=&{()}",
        "<script>confirm('XSS')</script>",
        "<script>prompt('XSS')</script>",
        "<marquee><img src=x onerror=alert('XSS')></marquee>",
        "<div style=\"width:100px;height:100px;background:url(javascript:alert('XSS'))\"></div>"
    ]

    @staticmethod
    def scan(url, response):
        vulnerabilities = []
        response_text = response.text

        for payload in XSSScanner.XSS_PAYLOADS:
            # Check for direct reflection of the payload
            if payload in response_text:
                vulnerabilities.append({
                    "type": "XSS",
                    "url": url,
                    "severity": "High",
                    "description": f"Reflected XSS vulnerability detected with payload: {payload}"
                })
            # Check for reflection after common HTML encoding (e.g., < becomes &lt;)
            elif payload.replace('<', '&lt;').replace('>', '&gt;') in response_text:
                vulnerabilities.append({
                    "type": "XSS",
                    "url": url,
                    "severity": "Medium",
                    "description": f"Potential XSS vulnerability (encoded reflection) with payload: {payload}"
                })
        return vulnerabilities
