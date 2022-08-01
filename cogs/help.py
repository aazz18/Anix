import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.errors import Forbidden
async def send_embed(ctx, embed):
    
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)
class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def help(self, ctx, *module):
        await ctx.message.delete()
        module = " ".join(module)
	
        prefix = ">"
        
        owner = self.bot.owner_id
        bot_name = "Anix"
        general_color =  discord.Color.dark_blue()
        specific_color =   discord.Color.dark_orange()
        error_color = discord.Color.red()
        if len(module) == 0:
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            emb = discord.Embed(title='Commands and modules', color=general_color,
                                description=f'Use `{prefix}help <module/command>` to gain more information about that module '
                                            f':smiley:\n')

            cogs_desc = ''
            for cog in self.bot.cogs:
                if not "Errors" == cog and not 'Startup' == cog:
                    cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            emb.add_field(name='Modules', value=cogs_desc, inline=False)
            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden and command.name != 'cog' and command.name != 'uncog' and command.name != 'reloadcog':
                    commands_desc += f'{command.name} | {command.brief}\n'

            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.add_field(name="About", value=f"\n\
                                    {bot_name} is maintained by `CriticRay#5008`")
        else:
            for cog in self.bot.cogs:
                if cog.lower() == module.lower():

                    emb = discord.Embed(title=f'{cog}  Commands', description=self.bot.cogs[cog].__doc__,
                                        color=specific_color)

                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.brief + f"\nUsage: `{command.help}`", inline=False)
                    break

            else:
                for command in self.bot.walk_commands():
                    if command.name.lower() == module.lower().splitlines()[0] and not command.hidden and not command.name.lower() == 'cog' and not command.name.lower() == 'uncog' and not command.name.lower() == 'reloadcog' and not command.name.lower() == 'nuke':
                        emb = discord.Embed(title=f'{command.name}', description=f"`{command.help}`", color=specific_color, inline=False)
                        emb.add_field(name=f"{command.brief}", value=command.brief, inline=False)
                        break
                    else:
                        emb = discord.Embed(title="What's that?!",
                                                description=f"I've never heard from a module/command called `{module}` before :scream:",
                                                color=error_color)

        emb.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)
        await send_embed(ctx, emb)
def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog loaded")