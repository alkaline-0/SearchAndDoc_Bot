import queue

from services.trigger_search import create_search_request

job_queue = queue.Queue()


def run_thread_worker() -> None:
    while True:
        # Get the job from the queue and execute it
        job = job_queue.get()
        try:
            res = create_search_request(job)
            print(len(res))
        finally:
            job_queue.task_done()
