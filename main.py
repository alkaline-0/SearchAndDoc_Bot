import asyncio
import os
import threading

from dotenv import load_dotenv
from fastapi import FastAPI

import background_tasks.thread_worker
from views.discord_bot.bot import client, run
from views.discord_bot.commands import DiscordCommands

worker = background_tasks.thread_worker.Worker()
threading.Thread(target=worker.run, daemon=True).start()

app = FastAPI()
load_dotenv()


async def main() -> None:
    await client.add_cog(DiscordCommands(client=client, job_queue=worker.job_queue))
    task = asyncio.create_task(run(bot=client, token=os.getenv("DISCORD_BOT_TOKEN")))
    await task


asyncio.create_task(main())
