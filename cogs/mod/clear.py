from main import footer, botversion
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random


from main import client, c_em_b, c_em_e, c_em_s


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command(name="clear", usage="<nombre>")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number: int):

        if type(number) != int:
            await ctx.channel.send("Merci d'entrer un __nombre__ entier")

        if number >= 99:
            await ctx.channel.send("Merci d'entrer un nombre inférieur à 99")
        else:
            await ctx.channel.purge(limit=number)
            await ctx.send(f"{number} messages ont été supprimés")


def setup(client):
    client.add_cog(Clear(client))