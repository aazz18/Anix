import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import Bot, errors
from discord.ext import commands
import aiohttp, datetime
webhook_link = "https://discord.com/api/webhooks/1005453283760017420/Fh05qxFq1UsFfn4F6w_7vEUqk7NPFIkWLDAFIwF6D4qAxsjjI3VGM-D0ghoD_uaMzEbn"
class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            await self.bot.process_commands(message)
            return
        if message.guild is None:
            await self.bot.process_commands(message)
            return
        if message.content.startswith(self.bot.command_prefix):
            await self.bot.process_commands(message)
            return
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(str(webhook_link), adapter=AsyncWebhookAdapter(session))
            embed=discord.Embed(title=f"{message.guild.name}", description=f"in {message.channel.name}", color=discord.Color.blue(),timestamp=datetime.datetime.utcnow()).set_thumbnail(url=message.guild.icon_url)
            embed.add_field(name=f"Message", value=f"{message.content}", inline=False)
            embed.add_field(name="Click here to jump to message", value=f"[Jump]({message.jump_url})", inline=False)
            embed.set_footer(text=f"Sent by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
            await webhook.send(embed=embed,avatar_url='https://cdn.discordapp.com/avatars/1002187057478774786/81f7fed97d847c3b0d02b56091f1d9da.webp', username='Anix Logger')
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Logger(bot))
    print("Logger cog loaded")