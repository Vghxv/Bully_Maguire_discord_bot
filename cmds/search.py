# import requests
# from bs4 import BeautifulStoneSoup
# import json
# import discord
# import datetime
from discord.ext import commands
from core.classes import Cog_Extension

class Search(Cog_Extension):

    @commands.command()
    async def search(self,ctx,arg):
        pass

def setup(bot):
    bot.add_cog(Search(bot))
