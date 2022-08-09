import discord
from discord.ext import commands
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
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description=f"Welcome to the {member.guild.name}! Please read the If you have any questions, please ask a staff member. Have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name}! Please verify yourself with the key `{self.key}` in the {member.guild.name} server. If you have any questions, please ask a staff member. Have fun!")
    @commands.Cog.listener()
    async def on_message(self, message):
        while True:
            if message.author.bot:
                return
            if message.channel.id == discord.utils.get(message.guild.channels, name=f'verify').id:
                try: 
                    message.channel.purge(limit=1)
                except discord.Forbidden:
                    pass
                verifyRole = discord.utils.get(message.guild.roles, name="Verified")
                if str(self.key) in message.content:
                    if verifyRole in message.author.roles:
                        await message.author.send(f"<@{message.author.id}> You are already verified!- This message will automatically delete after 60 seconds.", delete_after=60)
                        await self.bot.process_commands(message)
                        break
                    await message.author.add_roles(verifyRole)
                    await message.author.send(f"<@{message.author.id}>You have been verified!- This message will automatically delete after 60 seconds.", delete_after=60)
                    await self.bot.process_commands(message)
                    break
                else:
                    await message.author.send(f"<@{message.author.id}> Invalid key. Please try again. - This message will automatically delete after 60 seconds.", delete_after=60)
                    self.key = random.randint(100000, 999999)
                    await message.author.send(f"<@{message.author.id}> Your new verification key is `{self.key}`. Please verify yourself in the {message.guild.name} server. - This message will automatically delete after 60 seconds.", delete_after=60)

def setup(bot):
    bot.add_cog(Verify(bot))
    print("Verify cog is loaded")