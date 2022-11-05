import os
from keep_alive import keep_alive
import discord
from discord import app_commands
from discord import ui


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)
        # In this basic example, we just synchronize the app commands to one guild.
        # Instead of specifying a guild to every command, we copy over our global commands instead.
        # By doing so, we don't have to wait up to an hour until they are shown to the end-user.

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        # self.tree.copy_global_to()
        await self.tree.sync()


intents = discord.Intents.all()
client = MyClient(intents=intents)


@client.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(client.user)  # Prints the bot's username and identifier


keep_alive()  # Starts a webserver to be pinged.

token = os.getenv("token")
client.run(token)  # Starts the bot
