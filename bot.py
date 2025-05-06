import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}') 

@bot.event
async def on_ready():
    print(f' Hola corazoncito, vamos a escuchar musica ♡⸜(˃ ᵕ ˂ )⸝: {bot.user.name}')
    await load_cogs()  

bot.run(TOKEN)