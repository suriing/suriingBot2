import os
import random
import asyncio

from keep_alive import keep_alive
import discord
from discord import app_commands
from discord import ui
from image2ascii import image_to_ascii, text_to_img


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


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")


# This context menu command only works on messages
@client.tree.context_menu(name="Image to ASCII [jpg/png → txt]")
async def context_image_to_ascii(
    interaction: discord.Interaction, message: discord.Message
):
    "이미지(jpg/png)를 아스키 아트(txt)로 변환."
    await interaction.response.defer()
    attach = message.attachments[0]
    attach_ext = os.path.splitext(attach.filename)[1].lower()
    if not (attach_ext == ".jpg" or attach_ext == ".png"):
        await interaction.followup.send("attachment is not 'jpg' or 'png' format")
        return
    await attach.save(attach.filename)
    ### UI for asking resize size
    ascii_text = None
    button_px50 = ui.Button(label="px50", style=discord.ButtonStyle.secondary)
    button_px100 = ui.Button(label="px100", style=discord.ButtonStyle.primary)
    button_px200 = ui.Button(label="px200", style=discord.ButtonStyle.secondary)
    button_px300 = ui.Button(label="px300", style=discord.ButtonStyle.secondary)
    resize_view = ui.View()
    resize_view.add_item(button_px50)
    resize_view.add_item(button_px100)
    resize_view.add_item(button_px200)
    resize_view.add_item(button_px300)

    async def txt_px50(interaction: discord.Interaction):
        nonlocal ascii_text
        px = 50
        await interaction.response.edit_message(
            content=f"max {px}x{px} resized image will be transformed to ascii art!",
            view=None,
        )
        ascii_text = image_to_ascii(attach.filename, max_width=px, max_height=px)

    async def txt_px100(interaction: discord.Interaction):
        nonlocal ascii_text
        px = 100
        await interaction.response.edit_message(
            content=f"max {px}x{px} resized image will be transformed to ascii art!",
            view=None,
        )
        ascii_text = image_to_ascii(attach.filename, max_width=px, max_height=px)

    async def txt_px200(interaction: discord.Interaction):
        nonlocal ascii_text
        px = 200
        await interaction.response.edit_message(
            content=f"max {px}x{px} resized image will be transformed to ascii art!",
            view=None,
        )
        ascii_text = image_to_ascii(attach.filename, max_width=px, max_height=px)

    async def txt_px300(interaction: discord.Interaction):
        nonlocal ascii_text
        px = 300
        await interaction.response.edit_message(
            content=f"max {px}x{px} resized image will be transformed to ascii art!",
            view=None,
        )
        ascii_text = image_to_ascii(attach.filename, max_width=px, max_height=px)

    button_px50.callback = txt_px50
    button_px100.callback = txt_px100
    button_px200.callback = txt_px200
    button_px300.callback = txt_px300

    await interaction.followup.send("Please select max size.", view=resize_view)
    ### UI end

    tempfp = "ascii-" + str(random.randint(1, 999)) + ".txt"
    while ascii_text is None:
        await asyncio.sleep(1)
    with open(tempfp, "w") as file:
        for line in ascii_text:
            file.write(line)
            file.write("\n")
        file.close()
    with open(tempfp, "rb") as f:
        txt_file = discord.File(f)
        await interaction.followup.send(file=txt_file)
    os.unlink(attach.filename)
    os.unlink(tempfp)


# This context menu command only works on messages
@client.tree.context_menu(name="ASCII to PNG [txt → png]")
async def context_ascii_to_image(
    interaction: discord.Interaction, message: discord.Message
):
    "아스키 아트(txt)를 이미지(png)로 변환."
    await interaction.response.defer()
    attach = message.attachments[0]
    attach_ext = os.path.splitext(attach.filename)[1].lower()
    if not attach_ext == ".txt":
        await interaction.followup.send("attachment is not 'txt' format")
        return
    await attach.save(attach.filename)
    ### UI for asking color theme
    ascii_img = None
    button_light = ui.Button(
        label="light", style=discord.ButtonStyle.primary, custom_id="light_theme"
    )
    button_dark = ui.Button(
        label="dark", style=discord.ButtonStyle.secondary, custom_id="dark_theme"
    )
    color_view = ui.View()
    color_view.add_item(button_light)
    color_view.add_item(button_dark)

    async def dark_png(interaction: discord.Interaction):
        nonlocal ascii_img
        await interaction.response.edit_message(
            content="dark theme image will be replied!", view=None
        )
        ascii_img = text_to_img(attach.filename, colortheme="dark")

    async def light_png(interaction: discord.Interaction):
        nonlocal ascii_img
        await interaction.response.edit_message(
            content="light theme image will be replied!", view=None
        )
        ascii_img = text_to_img(attach.filename)

    button_dark.callback = dark_png
    button_light.callback = light_png

    await interaction.followup.send("Please select color theme", view=color_view)
    ### UI end
    tempfp = "ascii-" + str(random.randint(1, 999)) + ".png"
    while ascii_img is None:
        await asyncio.sleep(1)
    ascii_img.save(tempfp, optimize=True)
    with open(tempfp, "rb") as f:
        picture = discord.File(f)
        await interaction.followup.send(file=picture)
    os.unlink(attach.filename)
    os.unlink(tempfp)


keep_alive()  # Starts a webserver to be pinged.

token = os.getenv("token")
client.run(token)  # Starts the bot
