from main import footer, botversion, icon
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random


from main import client, c_em_b, c_em_e, c_em_s


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="kick", usage="<@user> <raison>")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: nextcord.User, *, reason="Aucune raison renseignée"):
        await ctx.guild.kick(user=user, reason=reason)

        embed = nextcord.Embed(title="<:coche:935279475539722241> Expulsion",
                               description=f"{user.mention} a été expulsé du serveur", color=c_em_b)

        embed.add_field(name="<:ticket:935279475682328596> Raison", value=f"{reason}", inline=True)
        embed.add_field(name="<:regle:935279475778793572> Modérateur", value=ctx.author.mention, inline=False)
        embed.set_footer(text=footer, icon_url=icon)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Kick(client))
