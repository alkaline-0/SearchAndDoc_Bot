from dataclasses import dataclass
import datetime
from typing import Iterator
import discord

@dataclass
class MessageCluster:
    id: int
    author: discord.Member
    created_at: datetime
    content: str

    def __repr__(self):
        return f"[{self.created_at}] {self.author}: {self.content}"

def get_message_clusters(messages: list[discord.Message]) -> Iterator[MessageCluster]:
    cluster = None
    for message in messages:
        if cluster == None or message.author != cluster.author:
            # finish off cluster
            if cluster != None:
                yield cluster

            # begin new cluster
            cluster = MessageCluster(message.id, message.author, message.created_at, message.content)
        else:
            cluster.content += message.content

    # last cluster
    if cluster != None:
        yield cluster