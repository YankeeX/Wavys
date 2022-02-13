import datetime
import math
import os

import main
from main import footer, botversion, icon
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions, guild_only
import asyncio
import random

from main import client, c_em_b, c_em_e, c_em_s, prefix


class Pour(nextcord.ui.Button):
    def __init__(self):
        super().__init__(style=nextcord.ButtonStyle.secondary, emoji="<:Valide:942079286133796934>", custom_id="1")

    async def callback(self, interaction: nextcord.Interaction):
        users = []
        try:
            with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    users.append(stripped_line)

            if str(interaction.user.id) not in users:
                await interaction.send("Vous avez voté **pour** à cette idée", ephemeral=True)
                a = interaction.user.id
                with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "a") as file:
                    file.write(f"{str(a)}\n")

                with open("Data/idee/idee.json", "r") as f:
                    keys = json.load(f)

                num = keys[str(interaction.message.id)]["pour"]

                num_update = num + 1

                def updateKeyNum(data):
                    with open("Data/idee/idee.json", "r") as config:
                        config = json.load(config)
                    config[str(interaction.message.id)]["pour"] = data
                    newdata = json.dumps(config, indent=4, ensure_ascii=False)
                    with open("Data/idee/idee.json", "w") as config:
                        config.write(newdata)

                updateKeyNum(num_update)

                with open("Data/idee/idee.json", "r") as f:
                    keys = json.load(f)

                contre = int(keys[str(interaction.message.id)]["contre"])
                pour = int(keys[str(interaction.message.id)]["pour"])
                timestamp = keys[str(interaction.message.id)]["timestamp"]
                image = keys[str(interaction.message.id)]["url_image"]

                users.clear()

                with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "r") as file:
                    for line in file:
                        stripped_line = line.strip()
                        users.append(stripped_line)

                user_name = keys[str(interaction.message.id)]["user_name"]
                content = keys[str(interaction.message.id)]["content"]
                user = client.get_user(int(keys[str(interaction.message.id)]["author_id"]))
                new_embed = nextcord.Embed(title="Nouvelle Idée",
                                           description=f"{content}\n\n<:Valide:942079286133796934>-**Pour**: `{pour}`\n"
                                                       f"<:cross:942079286217699328>-**Contre**: `{contre}`",
                                           color=c_em_b)
                new_embed.set_author(name=str(user_name), icon_url=user.avatar.url)
                if str(image) != "None":
                    new_embed.set_image(url=str(image))
                new_embed.set_footer(text=timestamp)
                await interaction.message.edit(embed=new_embed)

            else:
                await interaction.send("Vous avez déjà voté !", ephemeral=True)
        except FileNotFoundError:
            return
        except IOError:
            return



class Contre(nextcord.ui.Button):
    def __init__(self):
        super().__init__(style=nextcord.ButtonStyle.secondary, emoji="<:cross:942079286217699328>", custom_id="2")

    async def callback(self, interaction: nextcord.Interaction):
        users = []
        try:
            with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    users.append(stripped_line)

            if str(interaction.user.id) not in users:
                await interaction.send("Vous avez voté **contre** à cette idée", ephemeral=True)
                a = interaction.user.id
                with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "a") as file:
                    file.write(f"{str(a)}\n")

                with open("Data/idee/idee.json", "r") as f:
                    keys = json.load(f)

                num = keys[str(interaction.message.id)]["contre"]

                num_update = num + 1

                def updateKeyNum(data):
                    with open("Data/idee/idee.json", "r") as config:
                        config = json.load(config)
                    config[str(interaction.message.id)]["contre"] = data
                    newdata = json.dumps(config, indent=4, ensure_ascii=False)
                    with open("Data/idee/idee.json", "w") as config:
                        config.write(newdata)

                updateKeyNum(num_update)
                with open("Data/idee/idee.json", "r") as f:
                    keys = json.load(f)

                contre = int(keys[str(interaction.message.id)]["contre"])
                pour = int(keys[str(interaction.message.id)]["pour"])
                timestamp = keys[str(interaction.message.id)]["timestamp"]
                image = keys[str(interaction.message.id)]["url_image"]

                users.clear()

                with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "r") as file:
                    for line in file:
                        stripped_line = line.strip()
                        users.append(stripped_line)

                user_name = keys[str(interaction.message.id)]["user_name"]
                content = keys[str(interaction.message.id)]["content"]
                user = client.get_user(int(keys[str(interaction.message.id)]["author_id"]))
                new_embed = nextcord.Embed(title="Nouvelle Idée",
                                           description=f"{content}\n\n<:Valide:942079286133796934>-**Pour**: `{pour}`\n"
                                                       f"<:cross:942079286217699328>-**Contre**: `{contre}`",
                                           color=c_em_b)
                new_embed.set_author(name=str(user_name), icon_url=user.avatar.url)
                if str(image) != "None":
                    new_embed.set_image(url=str(image))
                new_embed.set_footer(text=timestamp)
                await interaction.message.edit(embed=new_embed)

            else:
                await interaction.send("Vous avez déjà voté !", ephemeral=True)
        except FileNotFoundError:
            return
        except IOError:
            return



class Select_Staff(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Valider l'idée", emoji="<:Valide:942079286133796934>"),
            nextcord.SelectOption(label="Refuser l'idée", emoji="<:cross:942079286217699328>"),
            nextcord.SelectOption(label="Supprimer l'idée", emoji="🗑"),
        ]
        super().__init__(placeholder="Staff Only", min_values=1, max_values=1, options=options, custom_id="3")

    async def callback(self, interaction: nextcord.Interaction):
        messages = []
        with open(f"Data/idee/message.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                messages.append(stripped_line)

        messages.remove(str(interaction.message.id))

        with open(f"Data/idee/message.txt", "w") as file:
            for id in messages:
                file.writelines(f"{id}\n")

        users = []
        with open("Data/idee/idee.json", "r") as f:
            keys = json.load(f)

        contre = int(keys[str(interaction.message.id)]["contre"])
        pour = int(keys[str(interaction.message.id)]["pour"])
        timestamp = keys[str(interaction.message.id)]["timestamp"]

        users.clear()

        with open(f"Data/idee/users/{str(interaction.message.id)}.txt", "r") as file:
            for line in file:
                stripped_line = line.strip()
                users.append(stripped_line)

        user_name = keys[str(interaction.message.id)]["user_name"]
        content = keys[str(interaction.message.id)]["content"]
        user = client.get_user(int(keys[str(interaction.message.id)]["author_id"]))
        image = keys[str(interaction.message.id)]["url_image"]

        guild = interaction.guild
        role_equipe_admin = guild.get_role(926817291193176125)

        if role_equipe_admin in interaction.user.roles:

            if interaction.data["values"] == ["Valider l'idée"]:
                try:
                    await interaction.send(
                        f"{user.mention}, votre idée a été **validée** par l'équipe du **Café Des Devs**.")
                    del keys[str(interaction.message.id)]
                    with open("Data/idee/idee.json", "w") as f:
                        json.dump(keys, f, indent=4)
                    os.remove(f"Data/idee/users/{str(interaction.message.id)}.txt")
                    new_embed = nextcord.Embed(title="Nouvelle Idée",
                                               description=f"{content}\n\n<:Valide:942079286133796934>-**Pour**: `{pour}`\n"
                                                           f"<:cross:942079286217699328>-**Contre**: `{contre}`",
                                               color=0x92EA73)
                    new_embed.set_author(name=str(user_name), icon_url=user.avatar.url)
                    if str(image) != "None":
                        new_embed.set_image(url=str(image))
                    new_embed.set_footer(text=timestamp)
                    await interaction.message.edit(embed=new_embed, view=None)
                except:
                    pass
            elif interaction.data["values"] == ["Refuser l'idée"]:
                try:
                    del keys[str(interaction.message.id)]
                    with open("Data/idee/idee.json", "w") as f:
                        json.dump(keys, f, indent=4)
                    os.remove(f"Data/idee/users/{str(interaction.message.id)}.txt")
                    await interaction.send(
                        f"{user.mention}, votre idée a été **refusée** par l'équipe du **Café Des Devs**.")
                    new_embed = nextcord.Embed(title="Nouvelle Idée",
                                               description=f"{content}\n\n<:Valide:942079286133796934>-**Pour**: `{pour}`\n"
                                                           f"<:cross:942079286217699328>-**Contre**: `{contre}`",
                                               color=0xDF5656)
                    new_embed.set_author(name=str(user_name), icon_url=user.avatar.url)
                    if str(image) != "None":
                        new_embed.set_image(url=str(image))
                    new_embed.set_footer(text=timestamp)
                    await interaction.message.edit(embed=new_embed, view=None)
                except:
                    pass

            elif interaction.data["values"] == ["Supprimer l'idée"]:
                try:
                    del keys[str(interaction.message.id)]
                    with open("Data/idee/idee.json", "w") as f:
                        json.dump(keys, f, indent=4)
                    os.remove(f"Data/idee/users/{str(interaction.message.id)}.txt")

                    await interaction.send("Idée supprimée", ephemeral=True)
                    await interaction.message.delete()
                except:
                    pass
        else:
            await interaction.send("Vous n'avez pas la permission pour faire ça", ephemeral=True)


class ButtonView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Pour())
        self.add_item(Contre())
        self.add_item(Select_Staff())


class OnIdee(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.guild:
            guild = message.guild
            idee_chan = client.get_channel(926817386642956329)
            channel = message.channel

            if channel.id == idee_chan.id:
                if message.author.id != 841942462774640650:
                    content = message.content


                    author_name = message.author.name
                    author_discriminator = message.author.discriminator
                    user_name = f"{author_name}#{author_discriminator}"

                    view = ButtonView()
                    await message.delete()
                    embed = nextcord.Embed(title="Nouvelle idée",
                                           description=f"{content}\n\n<:Valide:942079286133796934>-**Pour**: `1`\n<:cross:942079286217699328>-**Contre**: `0`",
                                           color=c_em_b)
                    embed.set_author(name=str(user_name), icon_url=message.author.avatar.url)
                    if message.attachments:
                        attachments = message.attachments
                        embed.set_image(url=str(attachments[0].url))
                    embed.set_footer(text=message.created_at.strftime("%a, %#d %B %Y, %H:%M"))
                    new_message = await message.channel.send(embed=embed, view=view)

                    self.custom_id = random.randint(0, 1000)
                    attachments = message.attachments
                    with open("Data/idee/idee.json", "r") as f:
                        idee = json.load(f)

                        data = {
                            "author_id": message.author.id,
                            "message_id": new_message.id,
                            "content": str(content),
                            "user_name": str(user_name),
                            "pour": 1,
                            "contre": 0,
                            "channel_id": channel.id,
                            "timestamp": str(message.created_at.strftime("%a, %#d %B %Y, %H:%M")),
                            "custom_id": self.custom_id,
                            "url_image": str(attachments[0].url) if message.attachments else "None"
                        }
                        idee[str(new_message.id)] = data

                    with open("Data/idee/idee.json", "w") as f:
                        json.dump(idee, f, indent=4)

                    with open(f"Data/idee/users/{new_message.id}.txt", "a") as file:
                        a = message.author.id
                        file.write(f"{str(a)}\n")

                    with open(f"Data/idee/message.txt", "a") as file:
                        a = new_message.id
                        file.write(f"{str(a)}\n")

            else:
                return
        else:
            return


def setup(client):
    client.add_cog(OnIdee(client))
