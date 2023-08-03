"""
E.g. Martin => MMaarrttinn
"""


def double(name: str) -> str:
    return ''.join([x * 2 for x in name])


if __name__ == '__main__':
    print(double('Martin'))
