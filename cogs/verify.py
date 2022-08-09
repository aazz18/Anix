import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.key = None
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 1006599826315685888:
            welcomeid = 1006604054643875911
        elif member.guild.id == 1002659843720617995:
            welcomeid = 1002659844353970320
        self.key = random.randint(100000, 999999)
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description=f"Welcome to the {member.guild.name}! Please verify yourself with the command `verify` in the {member.guild.name} server. If you have any questions, please ask a staff member. Have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif").set_author(name="Done", icon_url="https://raw.githubusercontent.com/CriticRay/anix-images/main/checkmark-green.png?token=GHSAT0AAAAAABV3GFY562BKGYAAD6XVUZCYYXSUEMA"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name}! Please verify yourself with the command `verify {self.key}` in the {member.guild.name} server. If you have any questions, please ask a staff member. Have fun!")
    @commands.Cog.listener()
    async def on_message(self, message):
        while True:
            if message.author.bot:
                return
            if message.channel.id == 1006614884718485555:
                verifyRole = discord.utils.get(message.guild.roles, name="Verified")
                if message.content == self.key:
                    if verifyRole in message.author.roles:
                        await message.author.send(f"<@{message.author.id}> You are already verified!")
                        await self.bot.process_commands(message)
                        break
                    await message.author.add_roles(verifyRole)
                    await message.author.send(f"<@{message.author.id}>You have been verified!")
                    await self.bot.process_commands(message)
                    break
                else:
                    await message.author.send(f"<@{message.author.id}> Invalid key. Please try again.")
                    self.key = random.randint(100000, 999999)
                    await message.author.send(f"<@{message.author.id}> Your new verification key is `{self.key}`. Please verify yourself with the command `verify {self.key}` in the {message.guild.name} server. If you have any questions, please ask a staff member. Have fun!")

def setup(bot):
    bot.add_cog(Verify(bot))
    print("Verify cog is loaded")