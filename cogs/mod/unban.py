from main import footer, botversion, icon
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='unban', description='Permet de débannir la personne visée')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user, *, reason="Aucune raison renseignée"):

        userName, userId = user.split("#")
        bannedUser = await ctx.guild.bans()
        for i in bannedUser:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(user=i.user, reason=reason)
                embed = nextcord.Embed(title="<:coche:935279475539722241> Expulsion",
                                       description=f"{user} a été débanni de ce serveur", color=c_em_b)

                embed.add_field(name="<:ticket:935279475682328596> Raison", value=f"{reason}", inline=True)
                embed.add_field(name="<:regle:935279475778793572> Modérateur", value=ctx.author.mention, inline=False)
                embed.set_footer(text=footer, icon_url=icon)
                return

        failem4 = nextcord.Embed(title="Erreur",
                                description=f"❌ - L'utilistateur {user} n'est pas dans la liste des bannis",
                                color=c_em_e)
        failem4.set_footer(text=footer, icon_url=icon)
        await ctx.send(embed=failem4)


def setup(client):
    client.add_cog(Unban(client))
