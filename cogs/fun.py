import random
import os
import discord
from discord.ext.commands import Bot, errors
from discord.ext import commands
import aiohttp

async def done(ctx, message):
    await ctx.send(embed=discord.Embed(title=":white_check_mark: Done", description=str(message), color=discord.Color.green()))
class Fun(commands.Cog):
    """Fun commands"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="usernamegen", aliases=['username', 'user', 'nickname'], brief="Generates a random username", description="Generates a random username and applies to your nickname.")
    async def usernamegen(self, ctx):
        ">usernamegen"
        await ctx.message.delete()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://username-gen.herokuapp.com/") as resp:
                username = await resp.json(content_type=None)
                await ctx.author.edit(nick=username["username"])
                await done(ctx, "Changed your nickname to `" + username + "`")
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
        await ctx.send(embed=discord.Embed(title=":8ball: 8ball", description=f"Question: {question}\nAnswer: {random.choice(answers)}", color=discord.Color.blue()))
    @commands.command(name="roll", aliases=['dice', 'random'], brief="Rolls a dice", description="Rolls a dice.")
    async def roll(self, ctx, *, dice=None):
        ">roll <dice>"
        await ctx.message.delete()
        if dice.isdigit() and int(dice) > 0 and dice is not None:
            await ctx.send(embed=discord.Embed(title=":game_die: Dice", description=f"You rolled a {random.randint(1, int(dice))}", color=discord.Color.blue()))
        else:
            await ctx.send(embed=discord.Embed(title=":game_die: Dice", description=f"You rolled a {random.randint(1, 6)}", color=discord.Color.blue()))
    @commands.command(name="flip", aliases=['coin'], brief="Flips a coin", description="Flips a coin.")
    async def flip(self, ctx):
        ">flip"
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title=":game_die: Coin", description=f"You flipped a {random.choice(['heads', 'tails'])}", color=discord.Color.blue())) 
    @commands.command(name="dicksize", aliases=['dick, dicklength'], brief="Gets the size of your dick")
    async def dicksize(self, ctx):
        ">dicksize"
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(title=":eggplant: Dick", description=f"You measured your dick and your size was: {random.randint(1,20)} inches long!", color=discord.Color.blue()))
def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog loaded")