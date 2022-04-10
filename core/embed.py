from discord.ext import commands
from discord import Embed

def error(error:str, description:str):
    embed = Embed(color=0xFF0000)
    embed.add_field(name=f"<:error:962423626605424640> | {error}", value=description)
    return embed

def warning(warning:str, description:str):
    embed = Embed(color=0xFFA500)
    embed.add_field(name=f"<:warning:962423626462810263> | {warning}", value=description)
    return embed

def allowed(allowed:str, description:str):
    embed = Embed(color=0x00FF00)
    embed.add_field(name=f"<:allowed:962423626655748116> | {allowed}", value=description)
    return embed