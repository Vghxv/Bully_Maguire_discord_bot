import json
import discord
from discord.ext import commands
import os
with open(".\config.json","r",encoding="UTF8") as config:
    conf=json.load(config)


intents=discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print("bot is ready")


@bot.command()
async def l(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done")


@bot.command()
async def ul(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"un - loaded {extension} done")


@bot.command()
async def rl(ctx,extension):
    
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"re - loaded {extension} done")


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename}"[:-3])


if __name__=="__main__":
    bot.run(conf["TOKEN"])
