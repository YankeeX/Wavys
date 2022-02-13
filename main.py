import nextcord
from nextcord.ext import commands
import os
import asyncio
import random
from nextcord import Intents
import json

with open("config.json", "r") as config:
    config = json.load(config)

prefix = config['prefix']

intents = nextcord.Intents().default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.voice_states = True
intents.presences = True
intents.reactions = True
intents.guild_reactions = True

client = commands.Bot(command_prefix=prefix, intents=intents)
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
        await client.change_presence(
            activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"son écran"))

        await asyncio.sleep(30)


client.loop.create_task(ch_pr())

botversion = "beta"
footer = f"Wavys {botversion}"
icon = "https://cdn.discordapp.com/attachments/576032647806058503/935612382414245918/Frame_1889.png"
owners = ['597680465025040425', '638730315950587914']
c_em_b = 0xEAB38D  # couleur d'embed basique
c_em_e = 0xb51f18  # couleur d'embed error
c_em_s = 0x31ba18  # couleur d'embed success



@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./cogs/utils'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.utils.{filename[:-3]}')

for filename in os.listdir('./cogs/mod'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.mod.{filename[:-3]}')

for filename in os.listdir('./cogs/event'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.event.{filename[:-3]}')

client.run(config["token"])
