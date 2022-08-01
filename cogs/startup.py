import discord
from discord.ext.commands import Bot
from discord.ext import commands
class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as: ' + self.bot.user.name + '#' + self.bot.user.discriminator + ' - (' + str(self.bot.user.id) + ')')
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Left guild: {guild.name} - {str(guild.id)}')
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 993573362221715546:
            welcomeid = 993573959062790154
        elif member.guild.id == 1002659843720617995:
            welcomeid = 1002659844353970320
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description="Please read the rules and have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}!', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name}! Please read the rules and have fun!")
def setup(bot):
    bot.add_cog(Startup(bot))
    print("Startup cog loaded")