import os
import discord
from discord.ext.commands import Bot, errors
from discord.ext import commands
async def send_embed(ctx, error):
    await ctx.send(embed=discord.Embed(title=":x: Error", description=f"{error}", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))
class Errors(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: commands.CommandError) -> None:
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        if isinstance(error, commands.NoPrivateMessage):
            await send_embed(ctx, "This command cannot be used in private messages.")
        elif isinstance(error, commands.DisabledCommand):
            await send_embed(ctx, "This command is disabled.")
        elif isinstance(error, commands.ArgumentParsingError):
            await send_embed(ctx, "Invalid arguments.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await send_embed(ctx, "Missing required argument.")
        elif isinstance(error, commands.CommandNotFound):
            await send_embed(ctx, "Command not found.")
def setup(bot):
    bot.add_cog(Errors(bot))
    print("Errors cog loaded")