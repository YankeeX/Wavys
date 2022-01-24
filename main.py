import nextcord
from nextcord.ext import commands
import os
import asyncio
import random
from Tools.utils import getLanguage, getConfig
import json

with open("config.json", "r") as config:
        config = json.load(config)



client = commands.Bot(command_prefix='!')
client.remove_command("help")


@client.event
async def on_ready():
    number_of_guild = len(client.guilds)
    count = 0
    for guild in client.guilds:
        for member in guild.members:
            count = count + 1

    print("Actuellement en ligne")


async def ch_pr():
    global count
    await client.wait_until_ready()
    number_of_guild = len(client.guilds)
    count = 0
    for guild in client.guilds:
        for member in guild.members:
            count = count + 1

    while not client.is_closed():
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name=f"regarder son écran"))

        await asyncio.sleep(30)


client.loop.create_task(ch_pr())

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('cogs/Membre'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.Membre.{filename[:-3]}')

client.run(config["token"])