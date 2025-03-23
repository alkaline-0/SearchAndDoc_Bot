import queue
import threading

from services.trigger_search import create_search_request


class Worker(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        self.job_queue = queue.Queue()
        super().__init__(*args, **kwargs)

    def run(self) -> None:
        while True:
            # Get the job from the queue and execute it
            job = self.job_queue.get()
            try:
                res = create_search_request(job)
                print(len(res))
            finally:
                self.job_queue.task_done()

    def get_queue(self) -> queue.Queue:
        return self.job_queue
