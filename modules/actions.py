import discord, asyncio, random, time
from discord.ext import commands
from core import db_interactions as di
from core import embed
from core import data_interactions as datai
from pymongo import MongoClient

client = MongoClient("mongodb+srv://business:doUeTyy8tulrIEI8@cluster0.vp1o3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["businesscord"]
users = db["users"]

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(name="fraud", description="Lets you commit fraud with a change to earn 1/5th of your max income, or to go bankrupt!", )
    async def fraud(self, ctx):
        if di.check_if_exists(ctx.author.id):
            msg = await ctx.send(embed=embed.warning("Are you sure you want to commit fraud? You can lose everything!"))
            
            for x in ['✅','❎']:
                await msg.add_reaction(x)

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['✅','❎']
            
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                user = users.find_one({"id": ctx.author.id})
                
                fraud_outcome = random.randint(1, 5)

                if fraud_outcome == 1:
                    to_add = user["max_income"] / 5

                    users.update_one({"id":ctx.author.id}, {"$inc": {"cash": to_add}})
                    msg = await ctx.send(embed=embed.allowed(f"You successfully violated the law and committed tax fraude! {to_add} has been added to your balance."))

                    time.sleep(5)
                    await msg.delete()

                elif fraud_outcome == 2:
                    users.delete_one({"id":ctx.author.id})
                    msg = await ctx.send(embed=embed.fail(f"You've been caught committing fraud. Your company has been forced to go bankrupt, and you will have to rebuild your empire."))

                    time.sleep(5)
                    await msg.delete()

            except asyncio.TimeoutError:
                await msg.delete()
                return

def setup(bot):
    bot.add_cog(Actions(bot))