import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(671347507351257118)
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(671347507351257118)
    await channel.send(f"{member} leave")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")
 
   

bot.run('NjcyMDAzODEzNzk1NjkyNTU0.XjFKqQ.IESoEzq4OQWY7G9iyaPvpQo6p1o')