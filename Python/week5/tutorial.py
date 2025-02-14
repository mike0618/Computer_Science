import threading
import queue
from time import time, sleep


class ThreadExample:
    def __init__(self) -> None:
        # thread Lock prevents threads running into each othre
        self.thread_lock = threading.Lock()
        self.NUMBER_OF_THREADS = 5
        self.NUMBER_OF_JOBS = 10
        # create thread queue to keep thack of the threads
        self.q = queue.Queue(maxsize=self.NUMBER_OF_JOBS)
        for _ in range(self.NUMBER_OF_THREADS):
            # set the thread target
            thread = threading.Thread(target=self.worker)
            # all threads end when main program ends for cleaner shutdown
            thread.daemon = True
            # start/spawn the thread
            thread.start()
        # start timer
        start_time = time()
        print("Creating a task request for each item in the given range\n")
        # put all task requests into the queue
        for item in range(self.NUMBER_OF_JOBS):
            self.q.put(item)
        # block until all worker tasks are complete in the queue
        self.q.join()
        # calculate elapsed time
        elapsed_time = time() - start_time
        print(f"All workers completed their tasks after {elapsed_time:.2f} seconds")

    def worker(self):
        while True:
            # get the next item in the queue
            item = self.q.get()
            # hard work here
            sleep(1)
            # output: thread_lock preventsd the threads from running into each other
            with self.thread_lock:
                print(f"Working on {item}")
                print(f"Finished {item}")
            # remove task from queue
            self.q.task_done()


if __name__ == "__main__":
    thread_example = ThreadExample()
