import discord, globalvars
from cmds.start_relay import Common as start_relay
from discord.ext import commands


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = [])
    @commands.guild_only()
    async def test(self, ctx):

        await ctx.channel.send(globalvars.rllink)


def setup(bot):
    bot.add_cog(Common(bot))