from discord.ext import commands
from discord.ext import tasks
import discord_self_embed
import discord
import asyncio
import base64
import random
import config
import os

os.system('cls')
print("""


  _           _       
 | |         | |      
 | |     ___ | | __ _ 
 | |    / _ \| |/ _` |
 | |___| (_) | | (_| |
 |______\___/|_|\__,_|
                      
                      
""")

prefix = config.prefix
token = config.token

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f"""
    -------------------------
    logged in as
    User: {bot.user.name}#{bot.user.discriminator}
    ID: {bot.user.id}
    Token: {token}
    Prefix: {prefix}
    -------------------------
    """)



@bot.command()
async def whois(ctx, user: discord.User):
    embed = discord_self_embed.Embed(f'Who Is {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}',
    colour='36393f',
    )
    embed.set_image(user.avatar_url)
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.message.delete()
    await ctx.send(url)

    
@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

@bot.command()
async def presence(ctx, pres):
    game = discord.Game(str(pres))
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.dnd, activity=game)

@bot.command()
async def cmds(ctx):
    await ctx.message.delete()
    await ctx.send("""
        Ping - test commnad
    Whois - Ping someone to grab information on them
    Presence - Change your discord activity
    Idle - Changes your status to Idle
    dnd - Changes your status to Do Not Disturb
    Online - Changes your status to Online
    rr - Rick roll
    Status - Changes your status
    rng - Ranom Number
    Kick - Kick
    Ban - Ban
    Trash - Random Trash Talk
    """)

@bot.command()
async def idle(ctx):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.idle)

@bot.command()
async def online(ctx):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.online)

@bot.command()
async def dnd(ctx):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.dnd)

@bot.command()
async def rr(ctx):
    await ctx.message.delete()
    await ctx.send("""
    We’re no strangers to love,
You know the rules and so do I.
A full commitment’s what I’m thinking of,
You wouldnt get this from any other guy.

I just wanna tell you how I’m feeling,
Gotta make you understand…

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.

We’ve known each other for so long
Your heart’s been aching
But you’re too shy to say it.
Inside we both know what’s been going on,
We know the game and we’re gonna play it.

Annnnnd if you ask me how I’m feeling,
Don’t tell me you’re too blind to see…

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.

Give you up. give you up.
Give you up, give you up.
Never gonna give
Never gonna give, give you up.
Never gonna give
Never gonna give, give you up.

We’ve known each other for so long
Your heart’s been aching
But you’re too shy to say it.
Inside we both know what’s been going on,
We know the game and we’re gonna play it.

I just wanna tell you how I’m feeling,
Gotta make you understand…

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.

Never gonna give you up,
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye,
Never gonna tell a lie and hurt you.
    """)

@bot.command()
async def status(ctx, stat):
    await ctx.message.delete()

    if stat == 'dnd':
        await bot.change_presence(status=discord.Status.dnd)

    if stat == 'idle':
        await bot.change_presence(status=discord.Status.idle)

    if stat == 'online':
        await bot.change_presence(status=discord.Status.online)
    
@bot.command()
async def rng(ctx, min, max):
    rand = random.randint(int(min), int(max))

    await ctx.message.delete()
    await ctx.send(f"Your random number is {rand}")

  
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    if message.author == bot.user:
        return
    
    elif message.content.lower() == "whydidyoutypethis":
        await message.channel.send("woah")

    elif "https://discord.gift/" in message.content.lower():
        print("Nitro link found!")


@bot.command()
async def ban(ctx, user: discord.User, *, reason=None):
    await ctx.guild.ban(user, reason=reason)
    embed = discord_self_embed.Embed(f'Banned {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}\nReason: {reason}',
    colour='ce0100',
    )
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.send(url)
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command()
async def kick(ctx, user: discord.User, *, reason=None):
    await ctx.guild.kick(user, reason=reason)
    embed = discord_self_embed.Embed(f'Kicked {user.name}',
    description=f'Username: {user.name}#{user.discriminator}\nID: {user.id}\nReason: {reason}',
    colour='ce0100',
    )
    url = embed.generate_url(hide_url=True, shorten_url=False)
    await ctx.send(url)
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command()
async def trash(ctx):
    strings = ["L", "Trash", "Ratio"]
    await ctx.send(f"{random.choice(strings)}")

bot.run(token)
