import discord.ext.test as dpytest
import pytest


@pytest.mark.asyncio
async def test_throw_error_channel_does_not_exist(bot):
    await dpytest.message(
        content="!document_with_LLM 123453 test_keyword",
        channel=dpytest.get_config().channels[0],
        member=dpytest.get_config().members[0],
    )
    res = dpytest.get_message().content
    assert res == "Channel does not exist."


@pytest.mark.asyncio
async def test_new_job_added_to_queue_when_discord_command_triggered(bot):
    _channel = dpytest.get_config().channels[0]

    await dpytest.message(
        content="hello", channel=_channel, member=dpytest.get_config().members[0]
    )
    await dpytest.message(
        content="test", channel=_channel, member=dpytest.get_config().members[1]
    )

    await dpytest.message("!document_with_LLM %d test_keyword" % (_channel.id))

    job = pytest.mock_job_queue.get()

    assert job is not None
    pytest.mock_job_queue.task_done()


@pytest.mark.asyncio
async def test_get_channel_messages_successfully(bot):
    _channel = dpytest.get_config().channels[0]

    first_msg = await dpytest.message(
        content="hello", channel=_channel, member=dpytest.get_config().members[0]
    )
    second_msg = await dpytest.message(
        content="test", channel=_channel, member=dpytest.get_config().members[1]
    )

    command_trigger = await dpytest.message(
        "!document_with_LLM %d test_keyword" % (_channel.id)
    )

    job = pytest.mock_job_queue.get()
    job_content = job.channel.get_messages()

    assert job_content == [first_msg, second_msg, command_trigger]
    pytest.mock_job_queue.task_done()
