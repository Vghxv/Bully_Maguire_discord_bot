import json
import discord
from discord.ext import commands
from core.classes import Cog_Extension


with open(".\settings.json","r",encoding="UTF8") as settings:
    st=json.load(settings)


class react(Cog_Extension):


    @commands.command()
    async def dance(self,ctx):
        gif=discord.File(st["bully-maguire-dance"])
        await ctx.send(file=gif)


    @commands.command()
    async def pizza(self,ctx):
        gif=discord.File(st["pizza"])
        await ctx.send(file=gif)


    @commands.command()
    async def i_got_sth(self,ctx):
        gif=discord.File(st["thatallyougot"])
        await ctx.send(file=gif)


    @commands.command()
    async def love(self,ctx):
        gif=discord.File(st["theyloveme"])
        await ctx.send(file=gif)


    @commands.command()
    async def great(self,ctx):
        gif=discord.File(st["yeahgreat"])
        await ctx.send(file=gif)


def setup(bot):
    bot.add_cog(react(bot))