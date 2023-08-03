from collections import deque
from threading import Lock, Thread
from queue import Queue

my_queue = Queue()


def consumer():
    print('Consumer waiting...')
    work = my_queue.get()
    print('Consumer working')

    print('Consumer finished')
    my_queue.task_done()


thread = Thread(target=consumer)
thread.start()

print('Producer set data')
my_queue.put(object())
print('Producer waiting')
my_queue.join()
print('Producer finished')
thread.join()


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def download(item):
    return item


def resize(item):
    return item


def upload(item):
    return item


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())


download_queue.close()


download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(f'{done_queue.qsize()} elements were processed')


for thread in threads:
    thread.join()