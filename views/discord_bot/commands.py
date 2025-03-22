from background_tasks.job import Job
from background_tasks.thread_worker import job_queue
from models.channel import Channel
from views.discord_bot.bot import client


@client.command(name="document_with_LLM")
async def trigger_search(
    ctx,
    channel_id: int,
    topic: str,
) -> any:

    channel = client.get_channel(channel_id)
    if not channel:
        await ctx.channel.send("Channel does not exist.")
        return None
    channel_obj = Channel(channel=channel)
    await channel_obj.get_channel_messages()

    job_queue.put(Job(channel=channel_obj, topic=topic))
