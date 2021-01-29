import discord, json

from discord.utils import get
from discord.ext import commands

try:
    with open('cfg.json') as cfg_f:
        cfg=json.loads(cfg_f.read())
        get_token=cfg['token']
        version=cfg['version']
        is_canary=cfg['is_canary']
except FileNotFoundError:
    print('Cannot access the config file.')
    input('Press Enter to close.')
    exit()

def get_prefix(bot, message):
    prefixes=["!"]
    return commands.when_mentioned_or(*prefixes)(bot, message)


cmds=['cmds.roll', 'cmds.stop']

bot=commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())

if is_canary:
	bot.activity=discord.Game('{} | CANARY'.format(version))
else: bot.activity=discord.Game('{}'.format(version))

if __name__=='__main__':
    for extension in cmds:
        bot.load_extension(extension)
        print('Loading module {}'.format(extension))


@bot.event
async def on_ready():
    print('Started OpenWorld {}'.format(version))



    

if input('Start bot? y/n ')=='y':
    bot.run(get_token, bot=True, reconnect=True)
else: exit()