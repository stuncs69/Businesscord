from unittest import skip
import discord, aiohttp
from discord.ext import commands
from core import db_interactions as di

class CryptoInvesting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def cbuy(self, ctx, crypto_code, amount:int):
        if di.check_if_exists(ctx.author.id):
            exit()

def setup(bot):
    bot.add_cog(CryptoInvesting(bot))