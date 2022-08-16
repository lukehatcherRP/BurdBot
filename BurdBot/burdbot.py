import discord
from discord.ext import commands

TOKEN = 'ODcxMTc1MzYyMjg4MTc3MTUy.Guj9Z5.X019d4u7XflxJ8YnDz6auRldF7f0xLD5o7dFwQ'

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
async def dunst(ctx, sentance):
    """Dunstifies a sentance"""

    def dunst (sent):  
        res = ""    
        for idx in range(len(sent)):
            if not idx % 2 :
                res = res + sent[idx].upper()
            else:
                res = res + sent[idx].lower()
        return(res)
    # printing result
    print("The alternate case string is : " + dunst(sentance))


    await ctx.send(sentance)

bot.run(TOKEN)
