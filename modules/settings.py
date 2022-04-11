from discord_components import DiscordComponents, ComponentsBot, Button, ButtonStyle
import discord, asyncio
from discord.ext import commands
from core import db_interactions as di
from core import embed
from core import data_interactions as datai
from pymongo import MongoClient
import interactions

client = MongoClient("mongodb+srv://business:doUeTyy8tulrIEI8@cluster0.vp1o3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["businesscord"]
users = db["users"]

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='changename', aliases=['cn', 'change_name'])
    async def change_name(self, ctx, *, name):
        if di.check_if_exists(ctx.author.id):
            msg = await ctx.send(embed=embed.warning("Are you sure?","This change will cost you 1k USD."))
            for x in ['✅','❎']:
                await msg.add_reaction(x)
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['✅','❎']
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                user = users.find_one({"id": ctx.author.id})
                if user["cash"] >= 1000:
                    users.update_one({"id": ctx.author.id}, {"$inc": {"cash": -1000}, "$set": {"company_name": name}})
                    message =await ctx.send(embed=embed.allowed("Company name changed to {}".format(name), "We charged you 1k for this change."))
                    await message.add_reaction('✅')
            except asyncio.TimeoutError:
                await msg.delete()
                return

def setup(bot):
    bot.add_cog(Settings(bot))