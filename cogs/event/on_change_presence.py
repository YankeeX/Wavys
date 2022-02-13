import main
from main import footer, botversion, icon
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions, guild_only
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s, prefix


class ChangePresence(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_presence_update(self, before: nextcord.Member, after: nextcord.Member):

        try:
            if before.activity is not None:
                if before.id == 784103512589205534:
                    if before.activity.name == "discord.gg/cafedesdevs":
                        guild = client.get_guild(802070964287963177)
                        role_partner = after.guild.get_role(937060719386558464)
                        if role_partner in before.roles:
                            await before.remove_roles(role_partner)
                        else:
                            pass

            if after.activity is not None:
                if after.id == 784103512589205534:
                    if after.activity.name == "discord.gg/cafedesdevs":
                        guild = client.get_guild(802070964287963177)
                        role_partner = after.guild.get_role(937060719386558464)
                        if role_partner not in after.roles:
                            await after.add_roles(role_partner)
                        else:
                            pass
                    else:
                        pass
        except:
            pass

def setup(client):
    client.add_cog(ChangePresence(client))
