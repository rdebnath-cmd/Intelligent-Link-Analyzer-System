from urllib.parse import urlparse

def is_valid_url(url):
    """Check if URL format is valid"""
    parsed = urlparse(url)
    return all([parsed.scheme in ["http", "https"], parsed.netloc])
