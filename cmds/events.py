import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import random
with open(".\settings.json","r",encoding="UTF8") as settings:
    st=json.load(settings)

class Events(Cog_Extension):


    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(934773565084033094)
        await channel.send(f"you trash, {member}"[:-5])


    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(934773565084033094)
        await channel.send(f"bye, {member}"[:-5])


    @commands.Cog.listener()
    async def on_message(self,msg):
        msco=msg.content
        if "no" in msco and msg.author != self.bot.user:
            message=random.choice(st["no"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)
        elif "dance" in msco and msg.author != self.bot.user:
            message=random.choice(st["dance"])
            if message.endswith(".gif"):
                gif=discord.File(message)
                await msg.channel.send(file=gif)
            else:
                await msg.channel.send(message)
        elif "pizza" in msco and msg.author != self.bot.user:
            message=random.choice(st["pizzatime"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)

        elif "got" in msco and msg.author != self.bot.user:
            message=random.choice(st["got"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)
        
        elif "love" in msco and msg.author != self.bot.user:
            message=random.choice(st["love"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)


def setup(bot):
    bot.add_cog(Events(bot))