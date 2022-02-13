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


class OnInteractionIdee(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = json.load(open('./config.json', 'r'))

    @commands.Cog.listener()
    async def on_interaction(self, interaction: nextcord.Interaction):
        messages = []
        try:
            with open(f"Data/idee/message.txt", "r") as file:
                for line in file:
                    stripped_line = line.strip()
                    messages.append(stripped_line)

            if interaction.message.channel.id == 926817386642956329:
                if str(interaction.message.id) in messages:

                    if interaction.data["custom_id"] == '1':
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
                    elif interaction.data["custom_id"] == '2':
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
                    elif interaction.data["custom_id"] == '3':
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

        except FileNotFoundError:
            return
        except IOError:
            return
        except:
            pass


def setup(client):
    client.add_cog(OnInteractionIdee(client))
