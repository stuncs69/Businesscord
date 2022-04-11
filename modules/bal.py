from discord.ext import commands
from core import embed as em
import discord
from core import db_interactions as di

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bal(self, ctx):
        if di.check_if_exists(ctx.author.id):
            user = di.get_user(ctx.author.id)
            embed = em.allowed("Your balance is {} USD".format(user["cash"]), "You can check your balance by typing `b!bal`.")
            await ctx.send(embed=embed)
        else:
            embed = em.error("Not registered!", "You can register by typing `b!register`.")
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(Balance(bot))