import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import random
with open(".\settings.json","r",encoding="UTF8") as settings:
    st=json.load(settings)

class Chat(Cog_Extension):
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


        if "dance" in msco and msg.author != self.bot.user:
            message=random.choice(st["dance"])
            if message.endswith(".gif"):
                gif=discord.File(message)
                await msg.channel.send(file=gif)
            else:
                await msg.channel.send(message)


        if "pizza" in msco and msg.author != self.bot.user:
            message=random.choice(st["pizzatime"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)


        if "got" in msco and msg.author != self.bot.user:
            message=random.choice(st["got"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)
        
        
        if "fuck" in msco and msg.author != self.bot.user:
            message=random.choice(st["fuck"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)
        

        if "love" in msco and msg.author != self.bot.user:
            message=random.choice(st["love"])
            if message.endswith(".jpg"):
                jpg=discord.File(message)
                await msg.channel.send(file=jpg)
            else:
                await msg.channel.send(message)

def setup(bot):
    bot.add_cog(Chat(bot))