import os

from discord.ext import commands
from discord import ButtonStyle as bs
from discord import Intents, ui
from dotenv import load_dotenv

from reqs import *

EXPLORE_MSG = "Options:\n1: Building\n2: Settlement\n3: Sites\n4: Dangers\n5: Curiosities\n6: Barrier\n7: Factions"

SEASON_MSG = "Options:\n1: Spring\n2: Summer\n3: Fall\n4: Winter"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Currently unused
'''
class RemView(ui.View): # currently un
    @ui.button(label="Remove", style=bs.gray)
    async def remove(self, interaction, button):
        await interaction.message.delete()
'''
class ExploreView(ui.View):
    @ui.button(label="1", style=bs.gray)
    async def opt1(self, interaction, button):
        await interaction.response.send_message("*Building:*\n" + explore(1))
    
    @ui.button(label="2", style=bs.gray)
    async def opt2(self, interaction, button):
        await interaction.response.send_message("*Settlement:*\n" + explore(2))

    @ui.button(label="3", style=bs.gray)
    async def opt3(self, interaction, button):
        await interaction.response.send_message("*Site:*\n" + explore(3))
    
    @ui.button(label="4", style=bs.gray)
    async def opt4(self, interaction, button):
        await interaction.response.send_message("*Danger:*\n" + explore(4))

    @ui.button(label="5", row=1, style=bs.gray)
    async def opt5(self, interaction, button):
        await interaction.response.send_message("*Curiosity:*\n" + explore(5))

    @ui.button(label="6", row=1, style=bs.gray)
    async def opt6(self, interaction, button):
        await interaction.response.send_message("*Barrier:*\n" + explore(6))

    @ui.button(label="7", row=1, style=bs.gray)
    async def opt7(self, interaction, button):
        await interaction.response.send_message("*Faction:*\n" + explore(7))
    
    @ui.button(label="Remove", row=1, style=bs.red)
    async def remove(self, interaction, button):
        await interaction.message.delete()

class SeasonView(ui.View):
    @ui.button(label="1", style=bs.gray)
    async def opt1(self, interaction, button):
        await interaction.response.send_message("*Spring:*\n" + month_name(1))
    
    @ui.button(label="2", style=bs.gray)
    async def opt2(self, interaction, button):
        await interaction.response.send_message("*Summer:*\n" + month_name(2))

    @ui.button(label="3", style=bs.gray)
    async def opt3(self, interaction, button):
        await interaction.response.send_message("*Fall:*\n" + month_name(3))
    
    @ui.button(label="4", style=bs.gray)
    async def opt4(self, interaction, button):
        await interaction.response.send_message("*Winter:*\n" + month_name(4))
    
    @ui.button(label="Remove", style=bs.red)
    async def remove(self, interaction, button):
        await interaction.message.delete()
    

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

@bot.command(name='patron', help='Responds with random results from the Patron Crucible')
async def patron(ctx):
    response = rand_patron()
    await ctx.send(response)

@bot.command(name='surge', help='Responds with random results from the Wild Surge Crucible')
async def surge(ctx):
    response = wild_surge()
    await ctx.send(response)

@bot.command(name='traps', help='Responds with 3 random results from the Favourite Traps Crucible')
async def traps(ctx):
    response = trap_names()
    await ctx.send(response)

@bot.command(name='tenet', help='Responds with random results from the Tenet Builder')
async def tenet(ctx):
    response = rand_tenet()
    await ctx.send(response)

@bot.command(name='explore', help='Responds with message prompting the user to react to choose which exploration crucible to roll on')
async def explore_msg(ctx):
    await ctx.send(EXPLORE_MSG, view=ExploreView())

@bot.command(name='season', help='Responds with message prompting the user to react to choose which season to generate a month name for')
async def season_msg(ctx):
    await ctx.send(SEASON_MSG, view=SeasonView())

bot.run(TOKEN)