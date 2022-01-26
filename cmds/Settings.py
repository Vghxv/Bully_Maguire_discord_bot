import json
#import discord
from discord.ext import commands
from core.classes import Cog_Extension
with open(".\settings.json","r",encoding="UTF8") as settings:
    st=json.load(settings)


class Settings(Cog_Extension):


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms) gonna cry")
    # @commands.command()
    # async def about(self):




def setup(bot):
    bot.add_cog(Settings(bot))