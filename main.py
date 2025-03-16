import asyncio
import os
import threading

import discord
from discord.ext import commands
from dotenv import load_dotenv
from fastapi import FastAPI

import helpers.commands
from views.discord_bot.bot import client, run

app = FastAPI()
load_dotenv()
job_queue = helpers.commands.job_queue

def worker():
    while True:
        # Get the job from the queue and execute it
        job = job_queue.get()
        try:
            for msg in job:
              print (msg.content)
        finally:
            job_queue.task_done()

threading.Thread(target=worker, daemon=True).start()
            
async def main():
  task = asyncio.create_task(run(bot=client, token=os.getenv("DISCORD_BOT_TOKEN")))
  await task

asyncio.create_task(main())