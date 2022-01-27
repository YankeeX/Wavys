from main import footer, botversion, icon
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s


class MassRoleRem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="massrole-remove", aliases=["mr-remove"], usage="<@role>")
    @commands.has_permissions(administrator=True)
    async def massrolerem(self, ctx, role: nextcord.Role):
        for member in ctx.guild.members:
            await member.remove_roles(role)

        embedVar = nextcord.Embed(
            description=f"✅ Le role {role.mention} a été retiré à tous les membres du serveur",
            color=c_em_s)
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(MassRoleRem(client))
