import urllib.request


def check_status(url):
    """Check if URL is working or broken"""
    try:
        response = urllib.request.urlopen(url, timeout=5)
        if response.status == 200:
            return "Working"
        else:
            return f"Error Code: {response.status}"
    except:
        return "Broken"
