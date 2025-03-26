import queue
import threading

from services.message_processor import test_spacy_setup
from services.trigger_search import create_search_request


class Worker(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        self._job_queue = queue.Queue()
        super().__init__(*args, **kwargs)

    def run(self) -> None:
        while True:
            # Get the job from the queue and execute it
            job = self._job_queue.get()
            try:
                res = create_search_request(job)
                print(test_spacy_setup())
                print(len(res))
            finally:
                self._job_queue.task_done()

    def get_queue(self) -> queue.Queue:
        return self._job_queue
