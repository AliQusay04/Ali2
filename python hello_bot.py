import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    if message.content.lower() == 'hello':
        await message.channel.send('Hello!')

bot.run('MTE0NzQxODEyNzk3MDMzNjgyOA.GZIomZ.UFmlJW6dIaKk2DFXxvWyqLxh5YK31JvspxhGew')
