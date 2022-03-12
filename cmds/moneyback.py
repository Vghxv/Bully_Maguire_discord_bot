from discord.ext import commands
from core.classes import Cog_Extension
import discord

class Moneyback(Cog_Extension):
    @commands.command()
    async def money(self,ctx,debtormoney):
        arr = debtormoney.split()
        embed=discord.Embed(title="Creditor", description=f"{ctx.author}", color=0xbc3434)
        embed.set_author(name="I need that money @_@")
        for i in range(len(arr)/3):
            embed.add_field(name="debtor", value=f"{arr[3*i]}", inline=True)
            embed.add_field(name="money", value=f"${arr[3*i+1]}", inline=True)
            embed.add_field(name="detail", value=f"{arr[3*i+2]}", inline=True)
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Moneyback(bot))