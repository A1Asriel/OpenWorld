import discord, json
from discord.ext import commands

with open('cfg.json') as cfg_f:
    cfg=json.loads(cfg_f.read())
    owner=cfg['owner']

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['destroy'])
    @commands.guild_only()
    async def stop(self, ctx):
        if ctx.author.id==owner:
            await self.bot.close()
        else:
            await ctx.channel.send('Бот может быть остановлен только его создателем.')

def setup(bot):
    bot.add_cog(Common(bot))