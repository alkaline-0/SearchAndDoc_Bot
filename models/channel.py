import discord


class Channel:
    channel: discord.channel
    messages: any

    def __init__(self, channel: discord.channel):
        self.channel = channel
        self.messages = []

    async def get_channel_messages(
        self,
    ) -> any:
        async for message in self.channel.history(limit=None):
            self.messages.append(message)

    def get_messages(self) -> any:
        return self.messages


# Squence diagram with different Actors // Use mermaid with the code
# Documentation of the discord when it blocks/not blocks/return
