import nextcord
from nextcord import Client, Intents, Embed
from nextcord.utils import get
import asyncio
import random
import os
import main

from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions

from main import client, footer, botversion, c_em_b, c_em_e, c_em_s, icon


class RemRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="role-remove")
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, role: nextcord.Role, member: nextcord.Member = None):

        if member is None:
            member = ctx.author

        if role not in member.roles:
            failem4 = nextcord.Embed(title="Erreur",
                                     description=f"❌ - Ce membre possède pas le rôle mentionné",
                                     color=c_em_e)
            failem4.set_footer(text=footer, icon_url=icon)
            await ctx.send(embed=failem4)
        else:
            await member.remove_roles(role)
            embed = nextcord.Embed(title="Role remove",
                                   description=f"Le rôle {role.mention} a bien été retiré à {member.mention}",
                                   color=c_em_b)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(RemRole(client))
