import nextcord
from nextcord import Client, Intents, Embed
from nextcord.utils import get
import asyncio
import random
import os
import main

from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions

from main import client, footer, botversion, c_em_b, c_em_e, c_em_s


class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="mute", usage="<@user> <raison>")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: nextcord.Member, *, reason="Aucune raison n'a été renseignée"):
        async def cRoleMute(ctx):
            mutedRole = await ctx.guild.create_role(name="WavysMuted",
                                                    permissions=nextcord.Permissions(
                                                        send_messages=False,
                                                        speak=False),
                                                    reason="Creation du role WavysMuted car inexistant"
                                                    )
            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, send_messages=False, speak=False)
            return mutedRole

        async def getMutedRole(ctx, guild: nextcord.Guild) -> nextcord.Role:
            role = get(guild.roles, name="WavysMuted")
            if role is not None:
                return role
            else:
                await cRoleMute(ctx)

        mutedRole = await getMutedRole(ctx, ctx.guild)
        if mutedRole not in member.roles:
            await member.add_roles(mutedRole, reason=reason)

            embed = nextcord.Embed(title="<:coche:935279475539722241> Mute",
                                  description=f"{member.mention} a perdu la voix", color=c_em_b)

            embed.add_field(name="<:ticket:935279475682328596> Raison", value=f"{reason}", inline=True)
            embed.add_field(name="<:regle:935279475778793572> Modérateur", value=ctx.author.mention, inline=False)
            embed.set_footer(text=footer)

            await ctx.send(embed=embed)
        else:
            await ctx.send("Ce membre est déjà mute")



def setup(client):
    client.add_cog(Mute(client))