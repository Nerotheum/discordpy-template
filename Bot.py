import os
from dotenv import load_dotenv
import discord

load_dotenv()

token = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

bot.run(token)