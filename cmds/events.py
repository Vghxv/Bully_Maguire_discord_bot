# import discord
from discord.ext import commands
from core.classes import Cog_Extension


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
        if "no" in msg.content:
            await msg.channel.send("gonna cry")




def setup(bot):
    bot.add_cog(Events(bot))