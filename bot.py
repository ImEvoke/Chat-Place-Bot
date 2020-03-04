import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix='.')
client.remove_command('help')
id = client.get_guild(647917650579554314)



@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Use .help to view commands!'))
  print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def bruh(ctx):
  await ctx.send('Bruh')

@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f'{ctx.author} says: {message}')

@client.command()
async def serbia(ctx):
    embed = discord.Embed(title=' ', description=' ')
    embed.set_image(url='https://media.discordapp.net/attachments/647917650579554318/684169962515988718/image0.jpg?width=589&height=613')
    await ctx.send(embed=embed)

@client.command()
async def secks(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=' ', description=' ')
    embed.set_image(url='https://media.discordapp.net/attachments/684169620038484016/684215817210036224/X8vQxhF.jpg')
    await ctx.send(embed=embed)

@client.command()
async def relationshipadvice(ctx):
    await ctx.message.delete()
    await ctx.send('https://media.discordapp.net/attachments/647917650579554318/684563526169264172/video0.mp4')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name='Prefix', value='.', inline=False)
    embed.add_field(name='.help', value='Sends this message in a DM.', inline=False)
    embed.add_field(name='.ping', value='Returns Pong!', inline=False)
    embed.add_field(name='.say', value='Send a message from you as the bot.', inline=False)
    embed.add_field(name='.serbia', value='Serbia.', inline=False)
    embed.add_field(name='.secks', value='Secks.', inline=False)

    await author.send(embed=embed)

























keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
