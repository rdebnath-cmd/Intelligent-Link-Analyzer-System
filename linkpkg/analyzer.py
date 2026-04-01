import urllib.request
import urllib.error

def check_status(url):
    """Check if URL is working or broken"""
    try:
        response = urllib.request.urlopen(url, timeout=5)
        if response.status == 200:
            return "Working"
        else:
            return f"Error Code: {response.status}"
    except urllib.error.HTTPError as e:
        return f"HTTP Error: {e.code}"
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Unexpected Error: {e}"
