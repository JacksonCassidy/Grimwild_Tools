import os
import asyncio
import discord
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

from reqs import *

EXPLORE_MSG = "Options:\n1:Building\n2:Settlement\n3:Sites\n4:Dangers\n5:Curiosities\n6:Barrier\n7:Factions"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='heritage', help='Responds with a random heritage from the Heritage Crucible')
async def heritage(ctx):
    response = rand_heritage()
    await ctx.send(response)

@bot.command(name='spell', help='Responds with a random spell from the Wizard\'s Spell Crucible')
async def spell(ctx):
    response = rand_spell()
    await ctx.send(response)

@bot.command(name='gm', help='Responds with a random result from the GM Crucible')
async def gm(ctx):
    response = gm_cruc()
    await ctx.send(response)

@bot.command(name='herb', help='Responds with random herbs from the Herbalism Crucible')
async def herb(ctx):
    response = rand_herb()
    await ctx.send(response)

@bot.command(name='explore', help='Responds with message prompting the user to react to choose which exploration crucible to roll on')
async def explore_msg(ctx):
    msg = await ctx.send(EXPLORE_MSG)
    for i in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]:
        await msg.add_reaction(i)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    
    if reaction.message.content != EXPLORE_MSG:
        return

    match reaction.emoji:
        case "1️⃣":
            response = explore(1)
            name = "*Building:*\n"
        case "2️⃣":
            response = explore(2)
            name = "*Settlement:*\n"
        case "3️⃣":
            response = explore(3)
            name = "*Site:*\n"
        case "4️⃣":
            response = explore(4)
            name = "*Danger*:\n"
        case "5️⃣":
            response = explore(5)
            name = "*Curiosity:*\n"
        case "6️⃣":
            response = explore(6)
            name = "*Barrier:*\n"
        case "7️⃣":
            response = explore(7)
            name = "*Faction:*\n"
        case _:
            return

    await reaction.message.channel.send(name + response)

bot.run(TOKEN)