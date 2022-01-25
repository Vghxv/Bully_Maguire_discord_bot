import json
import discord
from discord.ext import commands

with open(".\config.json","r",encoding="UTF8") as config:
    conf=json.load(config)

with open(".\settings","r",encoding="UTF8") as settings:
    st=json.load(settings)


intents=discord.Intents.all()


bot = commands.Bot(command_prefix="M ",intents=intents)



@bot.event
async def on_ready():
    channel = bot.get_channel(934773565084033094)
    await channel.send("hey guys")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(934773565084033094)
    await channel.send(f"you trash, {member}")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(934793872712810536)
    await channel.send(f"bye, {member}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")

@bot.command()
async def dance(ctx):
    gif=discord.File(st["bully-maguire-dance"])
    await ctx.send(file=gif)

@bot.command()
async def pizza(ctx):
    gif=discord.File(st["pizza"])
    await ctx.send(file=gif)

@bot.command()
async def i_got_sth(ctx):
    gif=discord.File(st["thatallyougot"])
    await ctx.send(file=gif)

@bot.command()
async def love(ctx):
    gif=discord.File(st["theyloveme"])
    await ctx.send(file=gif)

@bot.command()
async def great(ctx):
    gif=discord.File(st["yeahgreat"])
    await ctx.send(file=gif)
    
bot.run(conf["TOKEN"])
