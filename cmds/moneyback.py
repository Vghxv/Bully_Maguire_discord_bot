from discord.ext import commands
from core.classes import Cog_Extension
import discord

class Moneyback(Cog_Extension):
    @commands.command()
    async def money(self,ctx,debtormoney):
        
        embed=discord.Embed(title="Creditor", description=f"{ctx.author}", color=0xbc3434)
        embed.set_author(name="I need that money @_@")
        embed.add_field(name="debtor", value=f"{debtor}", inline=True)
        embed.add_field(name="money", value=f"${money}", inline=True)
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Moneyback(bot))