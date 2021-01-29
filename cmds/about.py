import discord
from discord.ext import commands


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['info'])
    @commands.guild_only()
    async def about(self, ctx):
        embed = discord.Embed(title="Информация о боте", colour=discord.Colour(0xffeb00), description="Это бот, который предназначен для RP-серверов. В данный момент в его функции входят генератор случайных чисел и ранняя реализация \"звонков\" между серверами.\n\n> *Чтобы получить информацию о доступных командах - введите `!help`.*")

        embed.set_author(name="OpenWorld Alpha 1.3.1 (21d29c)", icon_url="https://cdn.discordapp.com/avatars/802644475541323817/3d424f28bae3e1cd2dbb0b184af7b0c0.webp?size=128")
        embed.set_footer(text="Бот создан N1Nikita#5540", icon_url="https://cdn.discordapp.com/avatars/296735247213789215/33fd2c01530c4794448a4ca29c7a086d.png?size=128")

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Common(bot))