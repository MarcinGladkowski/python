from time import sleep


def two():
    print("Starting two...")
    sleep(2)
    print("Hello two")


def four():
    print("Starting four...")
    sleep(2)
    print("Hello four")


two()
four()

"""
Expected output:
Starting two...
Hello two
Starting four...
Hello four
"""