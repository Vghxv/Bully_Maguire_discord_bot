from discord.ext import commands
from core.classes import Cog_Extension


class Memberio(Cog_Extension):


    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(936646320104546335)
        await channel.send(f"you trash, {member}"[:-5])


    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(936646320104546335)
        await channel.send(f"bye, {member}"[:-5])


def setup(bot):
    bot.add_cog(Memberio(bot))