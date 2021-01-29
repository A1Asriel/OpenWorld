import discord, random, json
from discord.ext import commands

with open('cfg.json') as cfg_f:
    cfg=json.loads(cfg_f.read())
    version=cfg['version']

class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = [])
    @commands.guild_only()
    async def roll(self, ctx, num='100'):

        try:
            if int(num)>1000000:
                await ctx.channel.send('Ошибка: аргумент не может быть выше **1000000**.')
                return
            elif int(num)<2:
                await ctx.channel.send('Ошибка: аргумент не может быть ниже **2**.')
                return
        except:
            await ctx.channel.send('Ошибка: неправильный аргумент.')
            return

        rndnum=random.randint(1,int(num))

        embed = discord.Embed(title="Число от 1 до {}".format(num), colour=discord.Colour(0xffeb00), description="Игроку {} выпало **{}** из **{}**.".format(ctx.author.mention,rndnum,num))

        embed.set_author(name="OpenWorld", icon_url="https://cdn.discordapp.com/avatars/802644475541323817/3d424f28bae3e1cd2dbb0b184af7b0c0.webp?size=128")
        embed.set_footer(text="OpenWorld {}".format(version))

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Common(bot))