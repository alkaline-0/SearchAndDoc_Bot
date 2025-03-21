import threading

from helpers.worker_task import WorkerTask


class TriggerSearchService:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls) -> any:
        with cls._lock:
            if cls._instance is None:
                print("Creating new instance")
                cls._instance = cls.__new__(cls)
                # Put any initialization here.
            return cls._instance

    def trigger_search(self, worker_task: WorkerTask) -> None:
        # clean up messages
        return worker_task.channel.get_messages()
