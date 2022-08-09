import os
import discord
from discord.ext.commands import Bot
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description='A bot for the Discord server', case_insensitive=True, activity=discord.Activity(type=discord.ActivityType.watching, name="<3"), owner_id=1003654642309279874, intents=intents)
bot.remove_command('help')

async def isowner(ctx):
    if ctx.author.id != bot.owner_id:
        await ctx.send(embed=discord.Embed(description="You are not the owner of this bot.", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url).set_author(name="Error", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/crossmark-red.png?token=GHSAT0AAAAAABV3GFY4J4T3G6OGZTZLGGXQYXOQENQ"))
        return False
    return True

async def done(ctx, message):
    await ctx.send(embed=discord.Embed(description=str(message), color=discord.Color.green()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url).set_author(name="Done", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/checkmark-green.png?token=GHSAT0AAAAAABV3GFY562BKGYAAD6XVUZCYYXSUEMA"))

async def not_found(ctx, extension):
    await ctx.send(embed=discord.Embed(description=f"The cog `{extension}` was not found.", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url).set_author(name="Error", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/crossmark-red.png?token=GHSAT0AAAAAABV3GFY4J4T3G6OGZTZLGGXQYXOQENQ"))
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
@bot.command(name='clear_owner', description='Clears messages', brief='Clears messages')
async def clear_owner(ctx, amount=5):
    """>clear_owner <amount> - Owner only"""
    await ctx.message.delete()
    if await isowner(ctx):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(color=discord.Color.green(), delete_after=5).set_image(url="https://c.tenor.com/2T_mpBdB1kgAAAAM/discord-delete-message.gif").set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)).set_author(name=f"{amount} messages have been deleted", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/checkmark-green.png?token=GHSAT0AAAAAABV3GFY562BKGYAAD6XVUZCYYXSUEMA")
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
    
bot.run(os.environ.get('TOKEN', None))
