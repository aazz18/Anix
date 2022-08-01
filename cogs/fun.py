from ast import alias
import random
import discord
from discord.ext.commands import Bot, errors
from discord.ext import commands
import aiohttp
async def info(ctx, title, description):
    await ctx.send(embed=discord.Embed(title=title, description=description, color=discord.Color.blue()).set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url))
class Fun(commands.Cog):
    """Fun commands"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="usernamegen", aliases=['username', 'user', 'nickname', 'nicknamegen'], brief="Generates a random username and applies to your nickname.", description="Generates a random username and applies to your nickname.")
    async def usernamegen(self, ctx):
        ">usernamegen"
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://username-gen.herokuapp.com/") as resp:
                username = await resp.json(content_type=None)
                await info(ctx, ":tada: Nickname Changed", "Changed your nickname to `" + username + "`")
                await ctx.author.edit(nick=username["username"])
    @commands.command(name="8ball", aliases=['8b'], brief="Answers a question", description="Answers a question with a random answer.")
    async def eightball(self, ctx, *, question):
        ">8ball <question>"
        await ctx.message.delete()
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await info(ctx, "8ball", f"Question: {question}\nAnswer: {random.choice(answers)}")
    @commands.command(name="roll", aliases=['dice', 'random'], brief="Rolls a dice", description="Rolls a dice.")
    async def roll(self, ctx, dice=None):
        """>roll <dice>"""
        await ctx.message.delete()
        if dice is None:
            dice = 6
        if dice.isdigit() and int(dice) > 0:
            await info(ctx, "Roll", f"You rolled a `{random.randint(1, int(dice))}`")
    @commands.command(name="flip", aliases=['coin'], brief="Flips a coin", description="Flips a coin.")
    async def flip(self, ctx):
        """>flip"""
        await ctx.message.delete()
        await info(ctx, "Flip", f"You flipped a `{random.choice(['heads', 'tails'])}`")
    @commands.command(name="dicksize", aliases=['dick, dicklength'], brief="Gets the size of your dick.")
    async def dicksize(self, ctx):
        """>dicksize"""
        await ctx.message.delete()
        await info(ctx, "Dick", f"You measured your dick and your size was `{random.randint(1,20)}` inches long!")
    @commands.command(name='pfp', aliases=['profile_picture'], brief='Gets profile picture of an user.')
    async def pfp(self, ctx, *, member:discord.Member):
        """>pfp [user]"""
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title="Flashed", description=f"You a took a picture of {ctx.author.name}.", color=discord.Color.blue(), image=ctx.author.avatar_url).set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url))
def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog loaded")