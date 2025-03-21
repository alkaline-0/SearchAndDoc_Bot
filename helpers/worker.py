import queue

from services.trigger_search import TriggerSearchService

job_queue = queue.Queue()


def worker() -> None:
    while True:
        # Get the job from the queue and execute it
        job = job_queue.get()
        try:
            res = TriggerSearchService.instance().trigger_search(job)
            print(len(res))
        finally:
            job_queue.task_done()
