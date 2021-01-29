import discord, globalvars
from discord.ext import commands


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['hang'])
    @commands.guild_only()
    async def stop_relay(self, ctx):
        if globalvars.rllink!='':
            globalvars.rllink=''
            print('Bot has disconnected')
            await ctx.channel.send('*Вы завершили звонок.*')
        else:
            await ctx.channel.send('*Нет активного звонка.*')

def setup(bot):
    bot.add_cog(Common(bot))