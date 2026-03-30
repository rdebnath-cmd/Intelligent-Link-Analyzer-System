def check_security(url):
    """Check if URL uses HTTPS"""
    if url.startswith("https"):
        return "Secure (HTTPS)"
    else:
        return "Not Secure (HTTP)"


def is_suspicious(url):
    """Basic suspicious check"""
    keywords = ["login", "verify", "bank", "update", "secure"]

    if len(url) > 50:
        return "Yes (Too Long)"

    for word in keywords:
        if word in url.lower():
            return f"Yes (Contains '{word}')"

    return "No"