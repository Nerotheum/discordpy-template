import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from pathlib import Path

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def setup_hook():
    cogs_dir = Path('./cogs')
    for cog_file in cogs_dir.rglob('*.py'):
        await bot.load_extension(f'cogs.{cog_file.stem}')
        logger.info(f"Loaded cog: {cog_file.stem}")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')

bot.run(token)