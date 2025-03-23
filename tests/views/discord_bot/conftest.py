import glob
import os
import queue

import discord
import discord.ext.test as dpytest
import pytest
import pytest_asyncio

from views.discord_bot.commands import DiscordCommands


@pytest_asyncio.fixture
async def bot():
    # Setup
    _intents = discord.Intents.default()
    _intents.typing = False
    _intents.presences = False
    _intents.message_content = True
    _intents.members = True

    client = discord.ext.commands.Bot(intents=_intents, command_prefix="!")
    pytest.mock_job_queue = queue.Queue()
    await client._async_setup_hook()
    await client.add_cog(
        DiscordCommands(client=client, job_queue=pytest.mock_job_queue)
    )
    dpytest.configure(client=client, text_channels=["test", "general"], members=3)

    yield client

    # Teardown
    await dpytest.empty_queue()


def pytest_sessionfinish(session, exitstatus):
    """Code to execute after all tests."""

    # dat files are created when using attachements
    print("\n-------------------------\nClean dpytest_*.dat files")
    fileList = glob.glob("./dpytest_*.dat")
    for filePath in fileList:
        try:
            os.remove(filePath)
        except Exception:
            print("Error while deleting file : ", filePath)
