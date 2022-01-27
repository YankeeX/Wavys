import os

import nextcord
from nextcord.ext import commands
from main import client, footer, c_em_b, icon


class HelpButton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url="https://cafedesdevs.fr/",
                                         label="Site"))

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="help", description="Permet d'afficher la page d'aide")
    async def _help(self, ctx):

        mod = []
        util = []

        for filename in os.listdir('cogs/mod'):
            if filename.endswith('.py'):
                mod.append(filename[:-3])

        for filename in os.listdir('cogs/utils'):
            if filename.endswith('.py'):
                util.append(filename[:-3])

        mod.sort()
        util.sort()

        embedVar = nextcord.Embed(title="Page d'aide du client", color=c_em_b)

        embedVar.add_field(name="<:mod:936336421332086784> Modération",
                           value=', '.join(f'`{filename}`' for filename in mod),
                           inline=False)
        embedVar.add_field(name="<:util:936338215856656404> Utilitaire",
                           value=', '.join(f'`{filename}`' for filename in util),
                           inline=False)
        embedVar.set_footer(text=footer,
                            icon_url=icon)
        view = HelpButton()
        await ctx.send(embed=embedVar, view=view)


def setup(client):
    client.add_cog(Help(client))
