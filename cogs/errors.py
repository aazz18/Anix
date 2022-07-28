import os
import discord
from discord.ext.commands import Bot, errors
from discord.ext import commands
async def send_embed(ctx, error):
    await ctx.send(embed=discord.Embed(title=":x: Error", description=f"{error}", color=discord.Color.red()), delete_after=5)
class Errors(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError) -> None:
        if isinstance(error, commands.NoPrivateMessage):
            await send_embed(ctx, "This command cannot be used in private messages.")
        elif isinstance(error, commands.DisabledCommand):
            await send_embed(ctx, "This command is disabled.")
        elif isinstance(error, commands.ArgumentParsingError):
            await send_embed(ctx, "Invalid arguments.")
def setup(bot):
    bot.add_cog(Errors(bot))
    print("Errors cog loaded")