import os
import discord
import asyncio
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta

# Bot Intents & Defining Bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command('help')    

# Loading Cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            
async def main():
    await load()
    await bot.start("TOKEN")

# Startup Event
@bot.listen()
async def on_ready():
    await print(f"---------------------------------------- \n| Logged in as {bot.user} | \n| ID: {bot.user.id}              |\n----------------------------------------")


asyncio.run(main())
