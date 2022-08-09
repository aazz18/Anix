import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
import aiohttp, datetime
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
        # check channel id
        if message.guild.id == 1002659843720617995:
            webhook_link = "https://discord.com/api/webhooks/1005833505143521370/wcuNMexVDIOuKP6TG5Dr8Y14omvjtT5XEQZUhAtW-sD0eY1F34guIHfrYHXJG8uxnkhq"
        elif message.guild.id == 1006599826315685888:
            webhook_link = "https://discord.com/api/webhooks/1006602350154219530/hBdHTW522_RdMtQRmTZxy95Te4bOZI57cdkFeFGiBnq7VklpUXTr9U_jBj8oqBHQGSQX"
        else:
            webhook_link = "https://discord.com/api/webhooks/1005453283760017420/Fh05qxFq1UsFfn4F6w_7vEUqk7NPFIkWLDAFIwF6D4qAxsjjI3VGM-D0ghoD_uaMzEbn"

            
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(str(webhook_link), adapter=AsyncWebhookAdapter(session))
            embed=discord.Embed(title=f"{message.guild.name}", description=f"in <#{message.channel.id}>", color=discord.Color.blue(),timestamp=datetime.datetime.utcnow())

            embed.add_field(name=f"Message", value=f"{message.content}", inline=False)
            if message.attachments:
                # check if attachment is an image or not
                if message.attachments[0].filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    embed.set_image(url=message.attachments[0].url)
                if len(message.attachments) > 1:
                    embed.add_field(name="Attachments", value=f"Found {len(message.attachments)} attachments", inline=False)
                else:
                    embed.add_field(name= f"Attachment", value=f"[Attachment]({message.attachments[0].url})", inline=False)

            embed.add_field(name="Click here to jump to message", value=f"[Jump]({message.jump_url})", inline=False)
            embed.set_author(name=f"{message.author.name}#{message.author.discriminator}", icon_url=f"{message.author.avatar_url}")
            embed.set_footer(text=f"Sent by {message.author.name}#{message.author.discriminator}", icon_url=f"{message.guild.icon_url}")
            await webhook.send(embed=embed,avatar_url='https://cdn.discordapp.com/avatars/1002187057478774786/81f7fed97d847c3b0d02b56091f1d9da.webp', username='Anix Logger')
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Logger(bot))
    print("Logger cog loaded")