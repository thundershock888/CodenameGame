import discord

from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.counter = 0

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... Welcome Bacc.'.format(member))
        self._last_member = member
        self.counter += 1

    @commands.command()
    async def times(self, ctx, *args):
        await ctx.send(f"we greeted{self.counter} people!")

    @commands.command()
    async def func(self, ctx: commands.Context, a: int, b: int, *args):
        await ctx.send(f"{a} {b} {args}")
