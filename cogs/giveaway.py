import discord
from discord.ext import commands
from discord.ext.commands import Bot, errors
import aiohttp
import asyncio
import os
import random
import datetime

async def giveaway_embed(self, ctx, title, description, color, footer):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text=footer)
    return embed
class Giveaway(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command(name='giveaway', aliases=['g', 'gw'])
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx, mins: int, *, prize:str, channel: discord.TextChannel = None):
        await ctx.message.delete()
        if channel is None:
            channel = ctx.channel
        giveaway = await channel.send(embed=await giveaway_embed(self, ctx, f"Giveaway started by {ctx.author.name}", f"{prize}", discord.Color.blue(), f"Ends at {ctx.message.created_at + datetime.timedelta(minutes=mins)}"))
        await giveaway.add_reaction('🎉')
        await asyncio.sleep(mins)
        msg = await channel.channel.fetch_message(giveaway.id)
        userlist = msg.reactions[0].users().flatten()
        userlist.pop(userlist.index(ctx.author))
        winner = random.choice(userlist)
        await channel.send(embed=await giveaway_embed(self, ctx, f"Giveaway ended by {ctx.author.name}", f"{prize}", discord.Color.green(), f"Congrats {winner.name}#{winner.discriminator}"))
        await winner.send(embed=await giveaway_embed(self, ctx, f"You won the giveaway!", f"{prize}", discord.Color.green(), f"Congrats {winner.name}#{winner.discriminator}"))
        await giveaway.delete()

def setup(bot):
    bot.add_cog(Giveaway(bot))
    print('Giveaway cog loaded')