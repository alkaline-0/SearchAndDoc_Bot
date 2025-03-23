from background_tasks.job import Job


def create_search_request(job_obj: Job) -> None:
    # clean up messages
    return job_obj.channel.get_messages()
