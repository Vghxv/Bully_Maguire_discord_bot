import json
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
with open(".\settings.json","r",encoding="UTF8") as settings:
    st=json.load(settings)


class Settings(Cog_Extension):


    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms) gonna cry?")

    @commands.command()
    async def about(self,ctx):
        embed=discord.Embed(title="-----------------------------------------------------------------", description="Bully Maguire is a chat bot which would make you down specifically when you are in seventh heaven", color=0xaa1313,timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Bully Maguire", url="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjdxLPsu9H1AhVyIaYKHSrhBOwQFnoECBMQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTobey_Maguire&usg=AOvVaw05QGRl8qoUZzMxwXjy5bos", icon_url="https://pbs.twimg.com/profile_images/1399485270081380353/j3qja5r1_400x400.jpg")
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1399485270081380353/j3qja5r1_400x400.jpg")
        embed.add_field(name="Hobbies", value="treat others poorly", inline=True)
        embed.add_field(name="Favorite Food", value="pizza", inline=True)
        embed.add_field(name="Talent", value="dance", inline=True)
        embed.add_field(name="Pet Phrase", value="you trash", inline=True)
        embed.set_footer(text="wish you have a bad day")
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Settings(bot))