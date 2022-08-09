import discord
from discord.ext import commands
import aiohttp
import sqlite3
from bs4 import BeautifulSoup
async def good_info_channel(ctx, message, description, link):
    await ctx.send(embed=discord.Embed(title=f":white_check_mark: {message}", description=description, color=discord.Color.green()).set_image(url=link).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))

async def bad_info_channel(ctx, message, description, link):
    await ctx.send(embed=discord.Embed(title=f":x: {message}", description=description, color=discord.Color.red()).set_image(url=link).set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url))

class FanFic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    async def create_database(self,ctx):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS fanfic_finder (discord, fanfic_name)''')
        conn.close()
    async def check_if_user_in_database(self, ctx):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''SELECT fanfic_name FROM fanfic_finder WHERE discord = ?''', (ctx.author.id,))
        data = c.fetchone()
        conn.close()
        if not data:
            return False
        return True
    @commands.command(name='fanfic_s', aliases=['fanfic_finder_set_name', 'ff_set', 'ff_s', 'fanfic_finder_set'], brief='Set your fanfic preference')
    async def fanfic_s(self, ctx, *, fanfic_type):
        """>fanfic_s [fanfic_type]"""
        await self.create_database(ctx)
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''INSERT INTO fanfic_finder VALUES (?, ?)''', (ctx.author.id, fanfic_type))
        conn.commit()
        conn.close()
        await good_info_channel(ctx, "Your fanfic preference has been set", "", "")
        

    @commands.command(name='fanfic', aliases=['"ff", "fanfic_finder", "fanfic_search", "fanfic_search_finder", "fanfic_search_finder_finder"'], brief='Generates a random fanfic based on your taste with a random fanfic from fanfiction.net', description='Generates a random fanfic based on your taste with a random fanfic from fanfiction.net')
    async def fanfic(self, ctx):
        """>fanfic"""
        if await self.check_if_user_in_database(ctx) == False:
            await bad_info_channel(ctx, "You have not yet set a fanfic preference", "Please use the command `>fanfic_finder_set <fanfic name>` to set your fanfic preference", "https://i.imgur.com/XqQZQZg.png")
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('''SELECT fanfic_name FROM fanfic_finder WHERE discord = ?''', (ctx.author.id,))
        data = c.fetchone()
        conn.close()
        fanfic_type = data[0]
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://www.google.com/search?q={fanfic_type}') as resp:
                soup = BeautifulSoup(await resp.text(), 'html.parser')
                for link in soup.find_all('a'):
                    if 'fanfiction.net' in link.get('href'):
                        fanfic_url = link.get('href')
                        async with session.get(fanfic_url) as resp:
                            soup = BeautifulSoup(await resp.text(), 'html.parser')
                            for link in soup.find_all('a'):
                                if 'fanfic_title' in link.get('href'):
                                    fanfic_title = link.get('href')
                                    break
                        break
        await good_info_channel("Fanfic Found", f"Here is your random fanfic based on your preference: {fanfic_title} - {fanfic_url}", "")
def setup(bot):
    pass
    #bot.add_cog(FanFic(bot))
    #print('Fanfic Finder cog Loaded')


    