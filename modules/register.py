import discord
from discord.ext import commands
from core import db_interactions as di
from core import embed
from core import data_interactions as datai
from pymongo import MongoClient

client = MongoClient("mongodb+srv://business:doUeTyy8tulrIEI8@cluster0.vp1o3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["businesscord"]
users = db["users"]

class Registry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='register', aliases=['reg'])
    async def register(self, ctx):
        if di.check_if_exists(ctx.author.id):
            await ctx.send(embed=embed.error("Already registered!", "You can only register one main company."))
        else:
            await ctx.send(embed=embed.allowed('You are now CEO of {} Inc.!'.format(ctx.author.name), "Your office stands in the USA, and you managed to get a kickstarter of 10000$."))
            struct = {
                "id":ctx.author.id,
                "company_name": f"{ctx.author.name} Inc.",
                "cash": 10000,
                "country":"usa",
                "type":"office",
                "max_income":2000,
                "min_income":10,
                "company_level": 1,
                "subcompany":{},
                "crypto":{
                    "btc":0,
                    "eth":0,
                    "xrp":0,
                    "shib":0,
                    "doge":0,
                    "sol":0
                }
            }
            users.insert_one(struct)
    
    @commands.command()
    async def test_stuff(self, ctx):
        lol = users.find_one({"id": ctx.author.id})
        await ctx.send(lol)

def setup(bot):
    bot.add_cog(Registry(bot))

            
