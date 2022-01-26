import time

import nextcord
from discord import Client, Intents, Embed

import asyncio
import random
import os
import main

from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
from main import client, footer, botversion, c_em_b, c_em_e, c_em_s


class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="serverinfo", aliases=["si", "servinf"])
    async def _serverinfo(self, ctx):
        guild = ctx.guild
        roles = [role for role in guild.roles]
        emb = nextcord.Embed(colour=c_em_b, timestamp=ctx.message.created_at,
                            title="Informations sur le serveur")
        emb.set_thumbnail(url=guild.icon)
        emb.set_footer(text=f"Exécutée par {ctx.author.name}")

        emb.add_field(name="<:ticket:935279475682328596> Nom :", value=guild.name, inline=False)
        emb.add_field(name="<:id:935279475250315295> ID :", value=guild.id, inline=False)
        emb.add_field(name="<:couronne:935279475732656218> Owner :", value=f"<@{guild.owner_id}>", inline=False)
        emb.add_field(name="<:members:935604828325961760> Nombre de membres :", value=guild.member_count, inline=False)

        emb.add_field(name="<:bots:935611014718849034> Nombre de bots :", value=len(guild.bots), inline=False)

        emb.add_field(name="<:texte:935279475820744754> Nombre de salons textuels :", value=str(len(guild.text_channels)),
                      inline=False)
        emb.add_field(name="🔊 Nombre de salons vocaux :", value=str(len(guild.voice_channels)), inline=False)

        emb.add_field(name="Nombre d'émojis :", value=str(len(guild.emojis)), inline=False)

        emb.add_field(name="📆 Création du serveur :", value=guild.created_at.strftime("%d %B %Y"),
                      inline=False)

        emb.add_field(name="Roles :", value=", ".join([role.mention for role in roles[1:]]), inline=False)

        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(ServerInfo(client))
