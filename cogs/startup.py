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
def setup(bot):
    bot.add_cog(Startup(bot))
    print("Startup cog loaded")
