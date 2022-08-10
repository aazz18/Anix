import discord
from discord.ext import commands
import random
import string
class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # generate a random password called self.key
        self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits) for i in range(16))
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 1006599826315685888:
            welcomeid = 1006604054643875911
        elif member.guild.id == 1002659843720617995:
            welcomeid = 1002659844353970320
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description=f"Welcome to the {member.guild.name}! Please read the If you have any questions, please ask a staff member. Have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name}! Please verify yourself with the key `{self.key}` in the {member.guild.name} server. If you have any questions, please ask a staff member. Have fun!- This message will automatically delete itself after 60 seconds.", delete_after=60)
    @commands.command(name='verify', aliases=['v'])
    async def verify(self, ctx, key):
        verifyRole = discord.utils.get(ctx.guild.roles, name="Verified")
        if str(self.key) == key:
            if verifyRole in ctx.author.roles:
                await ctx.author.send(f"<@{ctx.author.id}> You are already verified!- This message will automatically delete itself after 60 seconds.", delete_after=60)
            await ctx.author.add_roles(verifyRole)
            await ctx.author.send(f"<@{ctx.author.id}>You have been verified! - This message will automatically delete itself after 60 seconds.", delete_after=60)
            await self.bot.process_commands(ctx)
        else:
            await ctx.author.send(f"<@{ctx.author.id}> Invalid key. Please try again. - This message will automatically delete itself after 60 seconds.", delete_after=60)
            self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits) for i in range(16))
            await ctx.author.send(f"<@{ctx.author.id}> Your new verification key is `{self.key}`. Please verify yourself in the {ctx.guild.name} server. - This message will automatically delete itself after 60 seconds.", delete_after=60)
        


def setup(bot):
    bot.add_cog(Verify(bot))
    print("Verify cog is loaded")