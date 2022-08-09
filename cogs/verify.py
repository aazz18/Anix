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
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name}! Please verify yourself with the command `verify {self.key}` in the {member.guild.name} server. If you have any questions, please ask a staff member. Have fun!")
    @commands.Cog.listener()
    async def on_message(self, message):
        
        while True:
            await self.bot.process_commands(message)
            await message.delete()
            if message.author.bot:
                return
            if message.channel.id == 1006614884718485555:
                await message.channel.purge(limit=1)
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