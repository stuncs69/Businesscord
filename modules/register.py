import discord
from discord.ext import commands
from core import db_interactions as di

class Registry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='register', aliases=['reg'])
    async def register(self, ctx):
        