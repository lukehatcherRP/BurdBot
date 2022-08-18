from dunce import duncey
import discord
from discord.ext import commands

# Remove Token before commiting 
TOKEN = 'ODcxMTc1MzYyMjg4MTc3MTUy.GYWkFb.OxmNDXe5I756-vC_vsassnbrnDrQCJL_Ng1A_s'

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def dunce(ctx, *, sentance):
    """DuNcEsTiFiEs a SeNtAnCe"""
    await ctx.send(duncey(sentance))

bot.run(TOKEN)
