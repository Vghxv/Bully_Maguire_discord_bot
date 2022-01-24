import json
import discord
from discord.ext import commands

with open(".\config.json","r",encoding="UTF8") as config:
    configs=json.load(config)
intents=discord.Intents.all()

bot = commands.Bot(command_prefix='~',intents=intents)

#fuck

@bot.event

async def on_ready():
    channel = bot.get_channel(934773565084033094)
    await channel.send("hey guys")
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")
# @bot.event

# async def on_member_join(member):
#     channel = bot.get_channel(934773565084033094)
#     await channel.send(f"you trash, {member}")

# @bot.event

# async def on_member_remove(member):
#     channel = bot.get_channel(934793872712810536)
#     await channel.send(f"bye, {member}")

bot.run(configs["TOKEN"])