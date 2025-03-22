import asyncio
import os
import threading

from dotenv import load_dotenv
from fastapi import FastAPI

import background_tasks.thread_worker

# flake8: noqa
import views.discord_bot.commands  # pylint: disable=unused-import
from views.discord_bot.bot import client, run

threading.Thread(
    target=background_tasks.thread_worker.run_thread_worker, daemon=True
).start()

app = FastAPI()
load_dotenv()


async def main() -> None:
    task = asyncio.create_task(run(bot=client, token=os.getenv("DISCORD_BOT_TOKEN")))
    await task


asyncio.create_task(main())
