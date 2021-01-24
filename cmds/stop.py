import discord, requests, random
from discord.ext import commands

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['stop'])
    @commands.guild_only()
    async def roll_print(self, message):
        rndnum=random.randint(1,100)
        await message.channel.send('Выпало {} из 100'.format(rndnum))

def setup(bot):
    bot.add_cog(Common(bot))