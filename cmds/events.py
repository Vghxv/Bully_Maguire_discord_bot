import discord
from discord.ext import commands
from core.classes import Cog_Extension


class events(Cog_Extension):


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms) gonna cry")


def setup(bot):
    bot.add_cog(events(bot))