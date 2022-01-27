import main
from main import footer, botversion, icon
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions, guild_only
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s, prefix


class OnMessage(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_message(self, message):

        if len(message.mentions) != 0:
            str_mention_id = f"@<@{str(message.mentions[0].id)}>"
        else:
            return
        try:
            if not message.author.bot:
                if message.mentions[0].id == 784103512589205534 and len(message.content) == len(str_mention_id):

                    em = nextcord.Embed(description="Mon prefix est ``" + prefix + "``",
                                        color=c_em_b)
                    await message.reply(embed=em)

                else:
                    return
            else:
                return
        except:
            return


def setup(client):
    client.add_cog(OnMessage(client))
