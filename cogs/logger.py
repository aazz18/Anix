from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import Bot, errors
from discord.ext import commands
import aiohttp
class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            await self.bot.process_commands(message)
            return
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('https://discord.com/api/webhooks/1003671459069169825/zwjtlWbNPC5WuOEaDT0M81NEiBAebrKk0zjYanvKIqqyMgmWg_7ubQKJ98lCgKVFwcD5', adapter=AsyncWebhookAdapter(session))
            await webhook.send(f"{message.author.name}#{message.author.discriminator} in {message.guild.name} said: {message.content}", avatar_url='https://cdn.discordapp.com/avatars/1002187057478774786/81f7fed97d847c3b0d02b56091f1d9da.webp', username='Anix Logger')
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Logger(bot))
    print("Logger cog loaded")