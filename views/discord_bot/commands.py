import queue

import discord.ext.commands as commands

from background_tasks.job import Job
from models.channel import Channel


class DiscordCommands(commands.Cog):
    _client: any

    def __init__(self, client, job_queue: queue.Queue):
        self._client = client
        self._job_queue = job_queue

    @commands.command(name="document_with_LLM")
    async def trigger_search(
        self,
        ctx,
        channel_id: int,
        topic: str,
    ) -> any:

        channel = self._client.get_channel(channel_id)
        if not channel:
            await ctx.channel.send("Channel does not exist.")
            return None
        channel_obj = Channel(channel=channel)
        await channel_obj.get_channel_messages()

        self._job_queue.put(Job(channel=channel_obj, topic=topic))
