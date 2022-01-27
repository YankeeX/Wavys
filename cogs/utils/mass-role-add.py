import main

from main import footer, botversion, icon
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s


class MassRoleAdd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="massrole-add", aliases=["mr-add"])
    @commands.has_permissions(administrator=True)
    async def massrole(self, ctx, role: nextcord.Role):
        guild = ctx.guild

        for member in ctx.guild.members:
            await member.add_roles(role)

        embedVar = nextcord.Embed(
            description=f"✅ **Le role {role.mention} a été ajouté à tous les membres du serveur",
            color=c_em_s)
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(MassRoleAdd(client))
