import nextcord

from main import footer, botversion, icon
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.category = 'moderation'

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: nextcord.User, *, reason="Aucune raison renseignée"):
        await ctx.guild.ban(user, reason=reason)

        embed = nextcord.Embed(title="<:coche:935279475539722241> Bannissement",
                              description=f"{user.mention} a été banni", color=c_em_b)

        embed.add_field(name="<:ticket:935279475682328596> Raison", value=f"{reason}", inline=True)
        embed.add_field(name="<:regle:935279475778793572> Modérateur", value=ctx.author.mention, inline=False)
        embed.set_footer(text=footer, icon_url=icon)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Ban(client))
