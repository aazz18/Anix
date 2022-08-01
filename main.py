import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description='A bot for the Discord server', case_insensitive=True, activity=discord.Activity(type=discord.ActivityType.watching, name="<3"), owner_id=975641516431265812, intents=intents)
bot.remove_command('help')

async def isowner(ctx):
    if ctx.author.id != bot.owner_id:
        await ctx.send(embed=discord.Embed(title=":x: Error", description="You are not the owner of this bot.", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))
        return False
    return True

async def done(ctx, message):
    await ctx.send(embed=discord.Embed(title=":white_check_mark: Done", description=str(message), color=discord.Color.green()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))

async def not_found(ctx, extension):
    await ctx.send(embed=discord.Embed(title=":x: Error", description=f"The cog `{extension}` was not found.", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))
@bot.command(name='cog', description='Loads a cog', brief='Loads a cog')
async def cog(ctx, extension):
    await ctx.message.delete()
    """>cog <cog> - Owner only"""
    if await isowner(ctx):
        try:
            bot.load_extension(f'cogs.{extension}')
            await done(ctx, f'Cog `{extension}` loaded')
        except commands.errors.ExtensionNotLoaded:
            await not_found(ctx, extension)
    return
@bot.command(name='uncog', description='Unloads a cog', brief='Unloads a cog')
async def uncog(ctx, extension):
    """>uncog <cog> - Owner only"""
    await ctx.message.delete()
    if await isowner(ctx):
        try:
            bot.unload_extension(f'cogs.{extension}')
            await done(ctx, f'Cog `{extension}` unloaded')
        except commands.errors.ExtensionNotLoaded:
            await not_found(ctx, extension)
    return
@bot.command(name='reloadcog', description='Reloads a cog', brief='Reloads a cog')
async def reload(ctx, extension):
    """>reloadcog <cog> - Owner only"""
    await ctx.message.delete()
    if await isowner(ctx):
        try:
            bot.reload_extension(f'cogs.{extension}')
            await done(ctx, f'Cog `{extension}` reloaded')
        except commands.errors.ExtensionNotLoaded:
            await not_found(ctx, extension)
    return
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
    
bot.run("MTAwMzY1NzE3ODA1OTY1MzI5MQ.Gvt5Ou.MpCrILfhPM4TehWHhph-m1tHbK3-8n36P7BEEU")
