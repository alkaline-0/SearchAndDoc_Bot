import discord

from helpers.worker import job_queue
from helpers.worker_task import WorkerTask
from models.channel import Channel
from views.discord_bot.bot import client as bot


@bot.command(name="document_with_LLM")
async def trigger_search(
    ctx,
    channel_name: str,
    topic: str,
) -> any:
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    if not channel:
        await ctx.channel.send("Channel does not exist.")
        return None
    channel_obj = Channel(channel=channel)
    await channel_obj.get_channel_messages()

    job_queue.put(WorkerTask(channel=channel_obj, topic=topic))
