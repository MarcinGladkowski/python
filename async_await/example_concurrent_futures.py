"""
Built in module mutiprocessing
- open child processes using many cores
- theirs GIL are independent
- commands come from main process
- useful in heavy calculations
- GIL doesn't allow to use multiple CORES!
"""

"""
Navier-Stokes
"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    assert False, 'Unavailable'


NUMBERS = [
    (1234569, 2343449), (1234519, 2343469),
    (1234569, 2343449), (1234519, 2343469),
    (1234569, 2343449), (1234519, 2343469),
    (1234569, 2343449), (1234519, 2343469),
    (1234569, 2343449), (1234519, 2343469),
    (1234569, 2343449), (1234529, 2343499),
]


def main():
    start = time.time()
    results = list(map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Operation took {delta:.3f} seconds \n')


"""
Solution by using multiple cores
- longer bc of starting threads, communication with...
"""


def main_concurrent():
    start = time.time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Operation took {delta:.3f} seconds\n')


"""
Fastest implementation!
"""


def main_concurrent_from_future():
    start = time.time()
    pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, NUMBERS))
    end = time.time()
    delta = end - start
    print(f'Operation took {delta:.3f} seconds\n')


if __name__ == '__main__':
    main()
    main_concurrent()
    main_concurrent_from_future()
