import discord


class Channel:
    channel: discord.channel

    def __init__(self, channel: discord.channel):
        self.channel = channel

    async def get_channel_messages(self) -> list[discord.Message]:
        messages = []
        async for message in self.channel.history(limit=None):
            messages.append(message)

        return messages


# Squence diagram with different Actors // Use mermaid with the code
# Documentation of the discord when it blocks/not blocks/return
