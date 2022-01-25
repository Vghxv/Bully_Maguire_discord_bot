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


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(934773565084033094)
    await channel.send(f"you trash, {member}"[:-5])


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(934773565084033094)
    await channel.send(f"bye, {member}"[:-5])


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")
if __name__=="__main__":
    bot.run(conf["TOKEN"])
