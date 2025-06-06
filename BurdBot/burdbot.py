from dunce import duncey
import discord
from discord.ext import commands
import requests
import random
import json

# Remove Token before commiting 
TOKEN = 'ODcxMTc1MzYyMjg4MTc3MTUy.GYWkFb.OxmNDXe5I756-vC_vsassnbrnDrQCJL_Ng1A_s'

description = '''ninjaBot in Python'''

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

async def get_random_trash_gif():
    """Fetch a random trash GIF from Tenor API"""
    try:
        # Using Tenor API v2 - you should set TENOR_API_KEY environment variable
        # For now, fallback to a list of static GIFs
        static_trash_gifs = [
            "https://media.tenor.com/2LzaKODtKT0AAAAC/trash-garbage.gif",
            "https://media.tenor.com/XpBLleSzxcYAAAAC/garbage-trash.gif",
            "https://media.tenor.com/5q9VUSSjJsEAAAAC/garbage-trash.gif",
            "https://media.tenor.com/iHG_R4H3HXMAAAAC/trash-garbage.gif"
        ]
        
        # Try to use Tenor API if available
        tenor_api_key = "AIzaSyCyouca1_KOqP2XtokhGb7gF2BgAqwF_N4"  # Demo key
        if tenor_api_key and tenor_api_key != "YOUR_TENOR_API_KEY_HERE":
            url = "https://tenor.googleapis.com/v2/search"
            params = {
                "q": "trash garbage",
                "key": tenor_api_key,
                "limit": 20,
                "contentfilter": "medium"
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('results'):
                    # Select a random GIF from the results
                    gif = random.choice(data['results'])
                    return gif['media_formats']['gif']['url']
        
        # Fallback to random static GIF
        return random.choice(static_trash_gifs)
    except Exception as e:
        print(f"Error fetching GIF: {e}")
        # Return a random static fallback GIF
        static_trash_gifs = [
            "https://media.tenor.com/2LzaKODtKT0AAAAC/trash-garbage.gif",
            "https://media.tenor.com/XpBLleSzxcYAAAAC/garbage-trash.gif",
            "https://media.tenor.com/5q9VUSSjJsEAAAAC/trash-garbage.gif",
            "https://media.tenor.com/iHG_R4H3HXMAAAAC/trash-garbage.gif"
        ]
        return random.choice(static_trash_gifs)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    # Don't respond to our own messages
    if message.author == bot.user:
        return
    
    # Check if the message contains "trash" (case-insensitive)
    if 'trash' in message.content.lower():
        try:
            gif_url = await get_random_trash_gif()
            await message.reply(gif_url)
        except Exception as e:
            print(f"Error sending trash GIF: {e}")
    
    # Process commands after checking for trash
    await bot.process_commands(message)


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
