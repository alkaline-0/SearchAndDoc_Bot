import datetime
from collections.abc import Iterator
from dataclasses import dataclass

import discord


@dataclass
class MessageCluster:
    id: int
    channel_id: int
    author: discord.Member
    created_at: datetime
    content: str

    def __repr__(self):
        return f"[{self.created_at}] {self.author}: {self.content}"


def process_content(
    message: discord.Message, clean_content: bool, remove_markdown: bool
):
    text = message.content

    if clean_content:
        text = message.clean_content

    if remove_markdown:
        text = discord.utils.remove_markdown(text)

    return text


def get_message_clusters(
    messages: list[discord.Message], clean_content: bool, remove_markdown: bool
) -> Iterator[MessageCluster]:
    cluster = None
    for message in messages:
        if (
            cluster == None
            or message.author != cluster.author
            or message.channel.id != cluster.channel_id
        ):
            # finish off cluster
            if cluster != None:
                yield cluster

            # begin new cluster
            cluster = MessageCluster(
                message.id,
                message.channel.id,
                message.author,
                message.created_at,
                message.content,
            )
        else:
            cluster.content += (
                f" {process_content(message, clean_content, remove_markdown)}"
            )

    # last cluster
    if cluster != None:
        yield cluster
