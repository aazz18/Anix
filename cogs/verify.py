import discord
from discord.ext import commands
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import random
import string
class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # generate a random password called self.key
        self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(16))
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 1006599826315685888:
            welcomeid = 1006604054643875911
        elif member.guild.id == 1002659843720617995:
            welcomeid = 1002659844353970320
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description=f"Welcome to the {member.guild.name}! Please read the rules. If you have any questions, please ask a staff member. Have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description=f"Welcome to the {member.guild.name}! Please verify yourself with the verification command `>verify {self.key}`.", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image())
    @commands.command(name='verify', aliases=['v'])
    async def verify(self, ctx, key):
        await ctx.message.delete()
        if ctx.guild.id == 1006599826315685888:
            verifyRole = discord.utils.get(ctx.guild.roles, id=1006600830738243584)
        else:
            verifyRole = discord.utils.get(ctx.guild.roles, name="Verified")
        if verifyRole in ctx.author.roles:
          await ctx.author.send(f"<@{ctx.author.id}>", delete_after=60, embed=discord.Embed(description="You are already verified!", color=discord.Color.red()).set_footer(text=f"This message will automatically delete itself after 60 seconds.", icon_url=ctx.author.avatar_url).set_author(name="Error", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/crossmark-red.png?token=GHSAT0AAAAAABV3GFY4J4T3G6OGZTZLGGXQYXOQENQ"))
          return
        
        if str(self.key) == key:
            await ctx.author.add_roles(verifyRole)
            await ctx.author.send(f"<@{ctx.author.id}>",delete_after=60, embed=discord.Embed(description="You have been verified!", color=discord.Color.green()).set_footer(text=f"This message will automatically delete itself after 60 seconds.", icon_url=ctx.author.avatar_url).set_author(name="Verified", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/checkmark-green.png?token=GHSAT0AAAAAABV3GFY562BKGYAAD6XVUZCYYXSUEMA"))
        else:
            await ctx.author.send(f"<@{ctx.author.id}>",delete_after=60, embed=discord.Embed(description="Invalid key. Please try again.", color=discord.Color.red()).set_footer(text=f"This message will automatically delete itself after 60 seconds.", icon_url=ctx.author.avatar_url).set_author(name="Error", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/crossmark-red.png?token=GHSAT0AAAAAABV3GFY4J4T3G6OGZTZLGGXQYXOQENQ"))
            self.key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(16))
            await ctx.author.send(f"<@{ctx.author.id}>",delete_after=60, embed=discord.Embed(description=f"Your verification command is `>verify {self.key}`.", color=discord.Color.red()).set_footer(text=f"This message will automatically delete itself after 60 seconds.", icon_url=ctx.author.avatar_url).set_author(name="Error", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/crossmark-red.png?token=GHSAT0AAAAAABV3GFY4J4T3G6OGZTZLGGXQYXOQENQ"))
        


def setup(bot):
    bot.add_cog(Verify(bot))
    print("Verify cog is loaded")