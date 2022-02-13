import main
from main import footer, botversion, icon
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions, guild_only
import asyncio
import random
from nextcord.utils import get

from main import client, c_em_b, c_em_e, c_em_s, prefix


class OnJoin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guilds = self.client.get_guild(802070964287963177)

        if member.guild.id != guilds.id:
            pass
        else:
            try:
                channel = guilds.get_channel(941715017596796998)
                role = guilds.get_role(802197117946560543)
                roles = guilds.get_role(846393942827466802)

                await channel.send(f"<:cdd:936959132886519818> - Bienvenue {member.mention} sur le **Café Des Devs** !")
                await member.add_roles(role)
                await member.add_roles(roles)
            except:
                pass


def setup(client):
    client.add_cog(OnJoin(client))
