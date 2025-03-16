import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from fastapi import FastAPI

from views.discord_bot.bot import client, run
import helpers.commands

app = FastAPI()
load_dotenv()


async def main():
  task = asyncio.create_task(run(bot=client, token=os.getenv("DISCORD_BOT_TOKEN")))
  await task

asyncio.create_task(main())