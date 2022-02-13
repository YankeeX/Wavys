import main
from main import footer, botversion, icon
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions, guild_only
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s, prefix

filtered_words = ["pd", "fdp", "enculé", "enculer", "connard", "con", "ntm", "ntr", "tg", "salop"]
starting_links = ["discord.gg/", "https://discord.gg/"]


class Badwords(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_message(self, msg: nextcord.Message):

        if isinstance(msg.channel, nextcord.DMChannel):
            pass

        else:
            if msg.author.id != 841942462774640650:

                guild = msg.guild

                member = guild.get_member(msg.author.id)

                role_staff = [846393202012717117, 936261214907015218, 802192508423110666, 847066743934287932,
                              846790827011604500, 936243464352448544, 936243468253163571, 936243467200385074,
                              936243755785277521]
                try:
                    if member.top_role.id in role_staff:
                        pass
                    else:

                        for word in filtered_words:
                            if msg.content.startswith(word):
                                await msg.delete()
                                response = await msg.channel.send(
                                    f"<:mod:936336421332086784> {msg.author.mention} il est strictement interdit d'envoyer des insultes !")
                                await asyncio.sleep(5)
                                await response.delete()

                        for starts in starting_links:
                            if starts in msg.content:
                                await msg.delete()
                                response = await msg.channel.send(
                                    f"<:mod:936336421332086784> {msg.author.mention} les liens sont interdits !")
                                await asyncio.sleep(5)
                                await response.delete()
                except:
                    pass
            else:
                pass


def setup(client):
    client.add_cog(Badwords(client))
