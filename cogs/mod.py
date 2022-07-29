import discord
from discord.ext import commands
import asyncio
async def good_info_dm(member, message,link):
    await member.send(embed=discord.Embed(title=f":white_check_mark: {message}", color=discord.Color.green()).set_image(url=link))

async def good_info_channel(ctx, message,link):
    await ctx.send(embed=discord.Embed(title=f":white_check_mark: {message}", color=discord.Color.green()).set_image(url=link))

async def bad_info_dm(member, message,link):
    await member.send(embed=discord.Embed(title=f":x: {message}", color=discord.Color.red()).set_image(url=link))

async def bad_info_channel(ctx, message,link):
    await ctx.send(embed=discord.Embed(title=f":x: {message}", color=discord.Color.red()).set_image(url=link))

class Mod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name='kick', aliases=['k'], brief='Kicks a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """>kick <user> [reason]"""
        if reason is None:
            reason = "No reason given"
        await member.kick(reason=reason)
        await bad_info_dm(member, f"You have been kicked from {ctx.guild.name} for the following reason: {reason}.", "https://c.tenor.com/3P9eAxWcegoAAAAM/mocha-drop.gif")
        await bad_info_channel(ctx, f"{member.mention} has been kicked for the following reason: {reason}.", "https://c.tenor.com/3P9eAxWcegoAAAAM/mocha-drop.gif")
    @commands.command(name='ban', aliases=['b'], brief='Bans a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """>ban <user> [reason]"""
        if reason is None:
            reason = "No reason given"
        await member.ban(reason=reason)
        await bad_info_dm(member, f"You have been banned from {ctx.guild.name} for the following reason: {reason}.", "https://thumbs.gfycat.com/PlayfulFittingCaribou-size_restricted.gif")
        await bad_info_channel(ctx, f"{member.mention} has been banned for the following reason: {reason}.", "https://thumbs.gfycat.com/PlayfulFittingCaribou-size_restricted.gif")
    @commands.command(name='unban', aliases=['ub'], brief='Unbans a user from the server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """>unban <user>"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await good_info_channel(ctx, f"{user.mention} has been unbanned.", "https://c.tenor.com/V7cHxMXwENQAAAAC/trollmites-unbanned.gif")
                return
        await ctx.send("User is not banned.")
    @commands.command(name='clear', aliases=['c'], brief='Clears a number of messages from the chat')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """>clear <amount>"""
        await ctx.channel.purge(limit=amount)
        await good_info_channel(ctx, f"{amount} messages have been deleted.", "https://c.tenor.com/2T_mpBdB1kgAAAAM/discord-delete-message.gif")
    @commands.command(name='mute', aliases=['m'], brief='Mutes a user from the server')
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """>mute <user> [reason]"""
        if reason is None:
            reason = "No reason given"
        await member.remove_roles(993573859322253383)
        await good_info_dm(member, f"You have been muted from {ctx.guild.name} for the following reason: {reason}.", "https://c.tenor.com/zS02vRH6AsMAAAAM/turn-down-volume-mute.gif")
        await good_info_channel(ctx, f"{member.mention} has been muted for the following reason: {reason}.", "https://c.tenor.com/zS02vRH6AsMAAAAM/turn-down-volume-mute.gif")
    @commands.command(name='unmute', aliases=['um'], brief='Unmutes a user from the server')
    @commands.has_permissions(mute_members=True)
    async def unmute(self, ctx, member: discord.Member):
        """>unmute <user>"""
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(993573859322253383)
        await good_info_channel(ctx, f"{member.mention} has been unmuted.", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTol2ZeYckq8-2xwX_nCWiWQO_lv5FILtasqw&usqp=CAU")
        await good_info_dm(member, f"You have been unmuted from {ctx.guild.name}.", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTol2ZeYckq8-2xwX_nCWiWQO_lv5FILtasqw&usqp=CAU")