from discord.ext import commands
from core.classes import Cog_Extension
import discord

class Moneyback(Cog_Extension):
    @commands.command()
    async def money(self,ctx,a1,a2,a3):
        embed=discord.Embed(title="Creditor", description=f"{ctx.author}", color=0xbc3434)
        embed.set_author(name="I need that money @_@")
        embed.add_field(name="debtor", value=f"{a1}", inline=True)
        embed.add_field(name="money", value=f"${a2}", inline=True)
        embed.add_field(name="detail", value=f"{a3}", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moneyback(bot))