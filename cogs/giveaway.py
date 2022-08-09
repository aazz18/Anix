import discord
from discord.ext import commands
import asyncio
import random
import datetime

async def giveaway_embed(self, ctx, title, description, color, footer):
    embed=discord.Embed(description=description, color=color).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url).set_author(name=title, icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/checkmark-green.png?token=GHSAT0AAAAAABV3GFY562BKGYAAD6XVUZCYYXSUEMA")
    embed.set_footer(text=footer)
    return embed
class Giveaway(commands.Cog):
    """Giveaway commands"""
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name='giveaway', aliases=['g', 'gw'])
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx, mins: int, *, prize:str, channel: discord.TextChannel = None):
        await ctx.message.delete()
        if channel is None:
            channel = ctx.channel
        giveaway = await channel.send(embed=await giveaway_embed(ctx, f"Giveaway started by {ctx.author.name}", f"{prize}", discord.Color.blue(), f"Ends at {ctx.message.created_at + datetime.timedelta(minutes=mins)}"))
        await giveaway.add_reaction('🎉')
        await asyncio.sleep(mins)
        msg = await channel.channel.fetch_message(giveaway.id)
        userlist = msg.reactions[0].users().flatten()
        userlist.pop(userlist.index(ctx.author))
        winner = random.choice(userlist)
        await channel.send(embed=await giveaway_embed(ctx, f"Giveaway ended by {ctx.author.name}", f"{prize}", discord.Color.green(), f"Congrats {winner.name}#{winner.discriminator}"))
        await winner.send(embed=await giveaway_embed(ctx, f"You won the giveaway!", f"{prize}", discord.Color.green(), f"Congrats {winner.name}#{winner.discriminator}"))
        await giveaway.delete()

def setup(bot):
    bot.add_cog(Giveaway(bot))
    print('Giveaway cog loaded')