from attr import dataclass

from models.channel import Channel


@dataclass
class WorkerTask:
    channel: Channel = None
    topic: str = None
