import discord, requests

class Common(object):

    def __init__(self, bot):
        self.bot = bot

    def relaying(ctx, connected_link=''):
        msg=ctx.content
        authorname='{} @ #{} ({})'.format(ctx.author.display_name, ctx.channel.name, ctx.guild.name)
        authoravatar='https://cdn.discordapp.com'+ctx.author.avatar_url._url

        jsonabc={
            "content": msg,
            "username": authorname,
            "avatar_url": authoravatar
        }

        if connected_link!='' and ctx.author.bot==False and not(msg[0]=='!'):
            requests.post(url=connected_link, json=jsonabc)