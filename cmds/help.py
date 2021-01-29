import discord
from discord.ext import commands


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['commands'])
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(title="Доступные команды", colour=discord.Colour(0xffeb00), description="*`[аргумент=X]` - необязательный аргумент, если он не будет указан - будет стоять стандартное значение X.*\n*`(аргумент)` - обязательный аргумент, без него команда не сработает.*")

        embed.set_author(name="OpenWorld Alpha 1.3.1 (21d29c)", icon_url="https://cdn.discordapp.com/avatars/802644475541323817/3d424f28bae3e1cd2dbb0b184af7b0c0.webp?size=128")

        embed.add_field(name="`!help | !commands`", value="Выводит данное сообщение.")
        embed.add_field(name="`!about | !info`", value="Выводит сообщение с информацией о боте.")
        embed.add_field(name="`!roll [максимальное_число=100]`", value="Данная команда выведет случайное число от 1 до указанного.", inline=True)
        embed.add_field(name="`!start_relay | !call (название_контакта)`", value="Начинает \"звонок\" в указанный канал. При этом все сообщения (кроме команд) из данного канала будут транслироваться в указанный.")
        embed.add_field(name="`!stop_relay | !hang`", value="Завершает \"звонок\". Сообщения перестают передаваться в другой канал.")

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Common(bot))