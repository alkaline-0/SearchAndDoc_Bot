import discord.ext.test as dpytest
import pytest

from models.channel import Channel
from services.message_processor import MessageCluster, get_message_clusters

@pytest.mark.asyncio
async def test_message_clusters(bot):
    _channel = dpytest.get_config().channels[0]
    _member1 = dpytest.get_config().members[0]
    _member2 = dpytest.get_config().members[1]

    _cluster1 = ["Hello, ", "World", "!"]
    _cluster2 = ["Some Random", "Stuff"]
    _cluster3 = ["New Text"]

    # cluster 1
    message1 = await dpytest.message(
        content=_cluster1[0], channel=_channel, member=_member1
    )
    await dpytest.message(content=_cluster1[1], channel=_channel, member=_member1)
    await dpytest.message(content=_cluster1[2], channel=_channel, member=_member1)

    # cluster 2
    message2 = await dpytest.message(
        content=_cluster2[0], channel=_channel, member=_member2
    )
    await dpytest.message(content=_cluster2[1], channel=_channel, member=_member2)

    # cluster 3
    message3 = await dpytest.message(
        content=_cluster3[0], channel=_channel, member=_member1
    )

    channel_obj = Channel(channel=_channel)
    await channel_obj.get_channel_messages()

    clusters = list(get_message_clusters(channel_obj.messages))
    cluster1: MessageCluster = clusters[0]
    cluster2: MessageCluster = clusters[1]
    cluster3: MessageCluster = clusters[2]

    assert (
        cluster1.author == _member1
        and cluster1.channel_id == _channel.id
        and cluster1.created_at == message1.created_at
        and cluster1.content == f"{_cluster1[0]}{_cluster1[1]}{_cluster1[2]}"
    )
    assert (
        cluster2.author == _member2
        and cluster2.channel_id == _channel.id
        and cluster2.created_at == message2.created_at
        and cluster2.content == f"{_cluster2[0]}{_cluster2[1]}"
    )
    assert (
        cluster3.author == _member1
        and cluster2.channel_id == _channel.id
        and cluster3.created_at == message3.created_at
        and cluster3.content == f"{_cluster3[0]}"
    )