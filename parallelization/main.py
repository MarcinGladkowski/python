"""
Examples from https://towardsdatascience.com/parallelization-in-python-the-easy-way-aa03ed04c209
"""

import pathlib
import time
import multiprocessing

# Creating generator
file_paths = (
    pathlib.Path(p)
    for p in (
    "book_about_python.txt",
    "book_about_java.txt",
    "book_about_c.txt",
    "science_fiction_book.txt",
    "lolita.txt",
    "go_there_and_return.txt",
    "statistics_for_dummies.txt",
    "data_science_part_1.txt",
    "data_science_part_2.txt",
    "data_science_part_3.txt",
)
)


def one_task():
    # print("one_task")
    time.sleep(.05)


def second_task():
    # print("second_task")
    time.sleep(.25)


def third_task():
    # print("third_task")
    time.sleep(1.)


def pipeline():
    one_task()
    second_task()
    third_task()


def evaluate_pipeline(path):
    return path, pipeline()


if __name__ == "__main__":
    # start_basic = time.perf_counter()
    # [pipeline() for path in file_paths]
    # print(f"Elapsed time - not multiprocessing: {round(time.perf_counter() - start_basic, 2)}")

    start_mp = time.perf_counter()
    with multiprocessing.Pool(4) as p:
        """
        4 - number of processes, we can use multiprocessing.cpu_count() - 1
        Example: 4 physical and 8 logical cores - it returns 8
        
        Dict evaluate the map generator
        
        Important here is we are usinf p.map() from multiprocessing handler! reduces time from 13s to 4s
        """
        dict(p.map(evaluate_pipeline, file_paths))

    print(f"Elapsed time - multiprocessing: {round(time.perf_counter() - start_mp, 2)}")
