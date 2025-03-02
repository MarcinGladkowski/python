"""
Works from Python 3.10

Using introduced soft keywords: match, case, _

use while you want to make a decision based on the structure of the data
"""

from pathlib import Path
from urllib.request import urlretrieve

def fetch(resource):
    match resource:
        case {"protocol": "http" | "ftp", "full_url": url}:
            match urlretrieve(url): # pattern based on specific functon return value
                case file_path, _:
                    return Path(file_path).read_text("utf-8")
        case _:
            raise ValueError("Unsupported protocol")


print(fetch({'protocol': 'http', 'full_url': 'https://www.w3.org/TR/PNG/iso_8859-1.txt'}))