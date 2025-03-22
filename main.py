import asyncio
import os
import threading

from dotenv import load_dotenv
from fastapi import FastAPI

import views.discord_bot.commands
import helpers.worker
from views.discord_bot.bot import client, run

threading.Thread(target=helpers.worker.worker, daemon=True).start()

app = FastAPI()
load_dotenv()


async def main() -> None:
    task = asyncio.create_task(run(bot=client, token=os.getenv("DISCORD_BOT_TOKEN")))
    await task


asyncio.create_task(main())
