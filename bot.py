import json
import discord
from discord.ext import commands
import os
with open(".\config.json","r",encoding="UTF8") as config:
    conf=json.load(config)


intents=discord.Intents.all()


bot = commands.Bot(command_prefix="M ",intents=intents)

@bot.event
async def on_ready():
    print("bot is ready")


@bot.command()
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done")


@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"un - loaded {extension} done")


@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"re - loaded {extension} done")


@bot.command()
async def help(ctx):
    await ctx.send("hey")


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")
        #print(filename)


if __name__=="__main__":
    bot.run(conf["TOKEN"])
