import os
import random
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = 'your bot token here'
IMAGE_FOLDER = r'image path make sure to use backslashes not forward'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="photo", description="grabs a random photo from the folder")
async def photo(interaction: discord.Interaction):
    all_files = []
    for root, dirs, files in os.walk(IMAGE_FOLDER):
        for file in files:
            if file.endswith(('.png')):
                all_files.append(os.path.join(root, file))

    if not all_files:
        await interaction.response.send_message("empty ahh folder")
        return

    random_image = random.choice(all_files)
    with open(random_image, 'rb') as f:
        picture = discord.File(f)
        await interaction.response.send_message(file=picture)

@bot.event
async def on_message(message: discord.Message):
    if "brick" in message.content.lower():
        await message.channel.send("WE JUST GOT EIGHT FREE PIZZAS")
    await bot.process_commands(message)

bot.run(TOKEN)
