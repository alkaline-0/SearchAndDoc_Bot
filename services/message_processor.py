import datetime
from collections.abc import Iterator
from dataclasses import dataclass

import discord
import spacy

nlp = spacy.load("en_core_web_trf")


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
            cluster = MessageCluster(
                message.id, message.author, message.created_at, message.content
            )
        else:
            cluster.content += message.content

    # last cluster
    if cluster != None:
        yield cluster


def test_spacy_setup():
    # Example messages
    message_1 = (
        "I am looking for the best machine learning algorithms for text classification."
    )
    message_2 = "What are the top methods for classifying text in machine learning?"

    # Process the messages
    doc1 = nlp(message_1)
    doc2 = nlp(message_2)

    # Calculate similarity
    similarity_score = doc1.similarity(doc2)
    return similarity_score
