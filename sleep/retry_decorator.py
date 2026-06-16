import urllib.request
import urllib.error

from time import sleep
from functools import wraps


# Using and decorator
def retry(delay=3, max_retries=3):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            last_exec=None
            for attempt in range(1, max_retries + 1):
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    last_exec = e
                    print(
                        f"Retrying in {delay}s ...\n"
                        f"({attempt}/{max_retries})"
                    )
                    
                    if attempt >= max_retries:
                        print("Interrupt execution")
                        raise last_exec
                    
                    sleep(delay)
            raise last_exec
        return wrapper
    return decorator



@retry()
def download_file(url: str):
    try:
        response = urllib.request.urlopen(url)
        print(f"Downloaded {url} ({response.length} bytes)")
    except urllib.error.URLError as e:
        print(f"Download failed: {e.reason}")
        raise

if __name__ == "__main__":
    download_file("http://www.example.com/data.csv")