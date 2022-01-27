import main
from main import footer, icon
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
import asyncio
import random
from main import client, c_em_b, c_em_e, c_em_s, prefix


class OnCommandError(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        failem1 = nextcord.Embed(title="Erreur",
                                description="`❌` - Je suis désolé mais vous ne possèdez pas la permission requise pour "
                                            "effectuer cette commande",
                                color=c_em_e)
        failem1.set_footer(text=footer, icon_url=icon)
        failem2 = nextcord.Embed(title="Erreur",
                                description="`❌` - Nous somme désolé, mais le bot a rencontré une erreur lors de l'execution "
                                            "de la commande",
                                color=c_em_e)
        failem2.set_footer(text=footer, icon_url=icon)
        failem3 = nextcord.Embed(title="Erreur",
                                description="`❌` - Cette commande n'existe pas",
                                color=c_em_e)
        failem3.set_footer(text=footer, icon_url=icon)

        failem4 = nextcord.Embed(title="Erreur",
                                description="`❌` - Le n'a pas la permissions pour effectuer cette action."
                                            "\nMerci de le placer plus haut dans liste des roles",
                                color=c_em_e)
        failem4.set_footer(text=footer, icon_url=icon)

        failem_Forbidden = nextcord.Embed(title="Erreur",
                                         description="`❌` - Interdit !"
                                                     "\nMerci de le placer plus haut dans liste des roles",
                                         color=c_em_e)
        failem4.set_footer(text=footer, icon_url=icon)

        if isinstance(error, commands.MissingPermissions):
            try:
                await ctx.reply(embed=failem1)
            except:
                return

        elif isinstance(error, commands.BotMissingPermissions):
            try:

                await ctx.reply(embed=failem4)

            except:
                return
        elif isinstance(error, commands.CheckFailure):
            try:
                await ctx.reply(embed=failem2)
            except:
                return

        elif isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                failem5 = nextcord.Embed(title="Erreur",
                                        description=f"`❌` - Il manque un/plusieurs argument(s)",
                                        color=c_em_e)
                failem5.set_footer(text=footer, icon_url=icon)
                failem5.add_field(name="Commande: ", value=f"``{main.prefix}{ctx.command.name} {ctx.command.usage}``")

                await ctx.reply(embed=failem5)
            except:
                return

        elif isinstance(error, nextcord.errors.Forbidden):
            try:
                await ctx.reply(embed=failem_Forbidden)
            except:
                return


def setup(client):
    client.add_cog(OnCommandError(client))
