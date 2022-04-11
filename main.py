import discord
from discord.ext import commands
from core import embed
from core import db_interactions as di

bot = commands.Bot(command_prefix="b!")

@bot.event
async def on_ready():
    print("[+] Bot online.")

# send error message on every error
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(embed=embed.error("Command Error", str(error)))

import os
for x in os.listdir('./modules'):
    if x.endswith('.py'):
        bot.load_extension(f'modules.{x[:-3]}')
        print("[!] Loaded module: " + x)

bot.run("OTYyNDQ1MzQ4NDEwODg4Mjg0.YlHpFA.poCBL-J9TwgQPcpWABPAV9Uv5jQ")