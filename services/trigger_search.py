from background_tasks.worker_task import WorkerTask


def create_search_request(worker_task: WorkerTask) -> None:
    # clean up messages
    return worker_task.channel.get_messages()
