from attr import dataclass

from models.channel import Channel


@dataclass
class Job:
    channel: Channel = None
    topic: str = None
