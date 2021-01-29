import discord, json, globalvars
from discord.ext import commands

with open('cfg.json') as cfg_f:
    cfg=json.loads(cfg_f.read())
    addresses=cfg['address_book']

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['call'])
    @commands.guild_only()
    async def start_relay(self, ctx, address=''):
        if address in addresses:
            print('Bot has connected to', address)
            await ctx.channel.send('*Вы успешно подключились к {}.*'.format(address))
            globalvars.rllink=addresses[address]
        else:
            await ctx.channel.send('*Контакт не найден.*')

def setup(bot):
    bot.add_cog(Common(bot))