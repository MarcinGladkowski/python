"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string
"""
import zlib

compressed = zlib.compress(b"hello world!hello world!hello world!hello world!")

zlib.decompress(compressed)