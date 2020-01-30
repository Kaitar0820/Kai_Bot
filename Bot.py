import discord
import json
import random

from discord.ext import commands

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)



bot = commands.Bot(command_prefix='!')


@bot.command()
async def 傻眼(ctx):
    random_pic = random.choice(jdata["pic"])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@bot.command()
async def 尬(ctx):
    random_pic = random.choice(jdata["url_pic"])
    await ctx.send(random_pic)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome']))
    await channel.send(f"{member} join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave']))
    await channel.send(f"{member} leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")


bot.run('NjcyMDAzODEzNzk1NjkyNTU0.XjIwTQ.Reggba0_RyYioJVCiyW3EvKTuxU')