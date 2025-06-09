from dunce import duncey
import discord
from discord.ext import commands

# Remove Token before commiting 
TOKEN = os.getenv("TOKEN")

description = '''ninjaBot in Python'''

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.reactions = True  # Required to handle reactions

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

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
    
    # Check if the message contains trash keywords (case-insensitive)
    trash_keywords = ['trash', 'garbage']
    if any(keyword in message.content.lower() for keyword in trash_keywords):
        try:
            await message.add_reaction('🗑️')
        except Exception as e:
            print(f"Error adding trash reaction: {e}")
    
    # Process commands after checking for trash
    await bot.process_commands(message)

@bot.event
async def on_reaction_add(reaction, user):
    # Don't respond to our own reactions
    if user == bot.user:
        return
    
    # Check if the reaction is the mockingspongebob emote
    # This could be a custom emoji named "mockingspongebob" or a Unicode emoji
    emote_name = None
    if hasattr(reaction.emoji, 'name'):
        emote_name = reaction.emoji.name
    else:
        emote_name = str(reaction.emoji)
    
    # Check for mockingspongebob emote (could be custom emoji or Unicode)
    if emote_name == 'mockingspongebob' or emote_name == '🤡':
        try:
            # Apply duncey to the reacted message content
            if reaction.message.content:  # Only process if message has content
                dunced_content = duncey(reaction.message.content)
                await reaction.message.reply(dunced_content)
        except Exception as e:
            print(f"Error processing dunce reaction: {e}")


@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def dunce(ctx):
    """DuNcEsTiFiEs the PrEvIoUs MeSsAgE"""
    # Get the message history, excluding the current command message
    messages = []
    async for message in ctx.channel.history(limit=2):
        messages.append(message)
    
    # The first message is the current command, the second is the previous message
    if len(messages) < 2:
        await ctx.send("No previous message found to dunce!")
        return
    
    previous_message = messages[1]
    
    # Apply duncey to the previous message content
    dunced_content = duncey(previous_message.content)
    
    # Reply to the previous message
    await previous_message.reply(dunced_content)

bot.run(TOKEN)
