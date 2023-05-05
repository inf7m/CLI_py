import socket
from urllib.parse import urlparse
import urllib.request
import urllib.error


def is_valid_url(url_input: str) -> bool:
    try:
        result = urlparse(url_input)
        print(f"urlparse.schema: {result.scheme}")
        return all(result)
    except ValueError:
        return False


def is_network_available() -> bool:
    try:
        urllib.request.urlopen('https://www.google.com')
        return True
    except urllib.error.HTTPError:
        print("Internet not stable or failure")
        return False
    except socket.error:
        print("SockerError: ", socket.error)
        return False
