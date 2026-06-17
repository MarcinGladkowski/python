import threading
import logging

WORKER_INTERVAL = 1
MAIN_INTERVAL = 0.75

def worker(event, worker_time_interval):
    while not event.is_set():
        logging.debug(f"Worker thread check in {worker_time_interval}")
        event.wait(worker_time_interval)
        

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="{relativeCreated:>6,.0f} ms | {threadName:<18} | {message}",
        style="{",
    )
    
    event = threading.Event()
    
    thread_one = threading.Thread(target=worker, args=(event, 2))
    thread_two = threading.Thread(target=worker, args=(event, 4))
    
    thread_one.start()
    thread_two.start()
    
    while not event.is_set():
        try:
            logging.debug("Main thread checking in")
            event.wait(MAIN_INTERVAL)
        except KeyboardInterrupt:
            event.set()
            break
        
        
if __name__ == '__main__':
    main()