import asyncio
import json
import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands import MissingPermissions, has_permissions

from main import client, footer, botversion, icon, c_em_b, c_em_e


class YesNo(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label='✅', style=nextcord.ButtonStyle.success)
    async def yes(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = True
        self.stop()

    @nextcord.ui.button(label='❌', style=nextcord.ButtonStyle.danger)
    async def no(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = False
        self.stop()


class embed(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.command(name="embed", description='Permet de créer une embed')
    async def embed(self, ctx):

        guild = ctx.guild

        init = await ctx.send(embed=nextcord.Embed(
            title="Création d'un embed",
            description="Merci de répondre aux questions suivantes pour finaliser la création de votre embed.",
            color=c_em_b)
                              .set_footer(icon_url=icon, text=self.client.user.name))

        questions = [
            "Quel est le titre de l'embed ?",
            "Quel est le texte de l'embed ?",
            "Dans quel salon sera l'embed ? (mentionnez le salon)",
            "Quelle sera la couleur de l'embed (Merci d'entrer une couleur hexadecimale)",
            "Souhaitez vous ajouter une image ?",
            "Quelle sera l'image ? (Merci de mettre le lien de l'image)"
        ]

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        index = 1
        answers = []
        question_message = None
        for question in questions:
            embed = nextcord.Embed(
                title="Configuration de l'embed",
                description=question,
                color=c_em_b
            ).set_footer(icon_url=icon, text="Wavys | tapez cancel pour annuler la commande")
            if index == 1:
                question_message = await ctx.send(embed=embed)
            else:
                if index == 5:
                    image = False
                    view = YesNo()
                    await question_message.edit(embed=embed, view=view)
                    await view.wait()
                    if view.value is None:
                        return
                    elif view.value:
                        await question_message.edit(embed=embed)
                        image = True
                    else:
                        break
                else:
                    await question_message.edit(embed=embed)

            try:
                if index == 5:
                    pass
                else:
                    user_response = await self.client.wait_for("message", timeout=120, check=check)
                    if str(user_response.content) == "cancel" or str(user_response.content) == "Cancel":
                        embedVar = nextcord.Embed(
                            description=f"``❌`` Commande annulée", color=c_em_e)
                        message_error = await ctx.send(embed=embedVar)
                        await init.delete()
                        await question_message.delete()
                        await asyncio.sleep(1)
                        await user_response.delete()
                        await message_error.delete()
                        break
                    else:
                        await user_response.delete()
            except asyncio.TimeoutError:
                await ctx.send(embed=nextcord.Embed(
                    title="Error",
                    color=c_em_e,
                    description="Vous avez pris trop de temps pour répondre à la question."
                ))
                return
            else:
                index += 1
                try:
                    answers.append(user_response.content)
                except:
                    return

        try:
            channel_id = int(answers[2][2:-1])
        except ValueError:
            await ctx.send(
                "Vous n'avez pas mentionnez le salon comme il faut, faite comme ça ? {}.".format(
                    ctx.channel.mention))
            return

        color = answers[3]

        try:
            sixteenIntegerHex = int(color.replace("#", ""), 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
        except ValueError:
            embedVar = nextcord.Embed(
                description=f"``❌`` La couleur n'est pas valide veuillez réitérer la commande", color=c_em_e)
            message_error = await ctx.send(embed=embedVar)

        text = str(answers[1])
        title = str(answers[0])
        channel = self.client.get_channel(channel_id)

        embed_em = nextcord.Embed(title=title, description=text, color=readableHex)
        if image:
            image_content = str(answers[5])
            embed_em.set_image(url=image_content)
        embed_em.set_footer(text=footer, icon_url=icon)

        await channel.send(embed=embed_em)

        await init.delete()
        await question_message.delete()


def setup(client):
    client.add_cog(embed(client))
