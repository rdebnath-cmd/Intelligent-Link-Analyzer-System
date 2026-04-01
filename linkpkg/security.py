import re

def check_security(url):
    """Check if URL uses HTTPS"""
    if url.startswith("https://"):
        return "Secure (HTTPS)"
    else:
        return "Not Secure (HTTP)"


def is_suspicious(url):
    """Enhanced suspicious check"""
    keywords = ["login", "verify", "bank", "update", "secure", "password", "account"]
    suspicious_reasons = []

    if len(url) > 100:
        suspicious_reasons.append("Too Long")

    for word in keywords:
        if word in url.lower():
            suspicious_reasons.append(f"Contains '{word}'")

    # Check for IP-based URLs
    if re.match(r"^https?://\d+\.\d+\.\d+\.\d+", url):
        suspicious_reasons.append("IP Address in URL")

    # Check for uncommon TLDs
    uncommon_tlds = [".xyz", ".top", ".club", ".info"]
    if any(url.endswith(tld) for tld in uncommon_tlds):
        suspicious_reasons.append("Uncommon TLD")

    return "Yes (" + ", ".join(suspicious_reasons) + ")" if suspicious_reasons else "No"
