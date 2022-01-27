from main import footer, botversion
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx):

        channel = ctx.channel
        guild_name = ctx.guild.name
        name = channel.name
        position = channel.position
        nsfw = channel.nsfw
        topic = channel.topic

        await channel.clone()
        await channel.delete()

        new_channel = nextcord.utils.get(client.get_all_channels(), guild__name=str(guild_name), name=str(name))

        if topic is None:

            await new_channel.edit(
                position=position,
                nsfw=nsfw

            )

        else:
            await new_channel.edit(
                position=position,
                nsfw=nsfw,
                topic=topic
            )

        await new_channel.send('Channel Clear')


def setup(client):
    client.add_cog(Purge(client))
