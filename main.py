import argparse
import asyncio
import json
import sys

import discord
from discord.ext import commands

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, help='discord token', default=None)
parser.add_argument('--command-prefix', type=str, help='command prefix', default='!')
parser.add_argument('--print-guilds-info', action='store_true')
args = parser.parse_args()

if args.token is not None:
    token = args.token
else:
    with open('token.txt', 'r') as f:
        token = f.readline()

# Configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

intents = discord.Intents.default()

client = discord.Client(intents=intents)
# client = commands.Bot(intents=intents, command_prefix=args.command_prefix)  # only if use commands


@client.event
async def on_ready():
    print(f'Inkeeper bot logged in as {client.user}')

    # show bot servers and channels information
    if args.print_guilds_info:
        for guild in client.guilds:
            print('guild id  ', guild.id)
            print('guild name', guild.name)
            for channel in guild.text_channels:
                print(f'> {channel.id:<22} {channel}')

    for bot in config['bots']:
        guildid = bot['guildid']
        channelid = bot['channelid']
        with open(bot['chatbot'], 'r') as f:
            bot['chat'] = json.load(f)
        bot['channel'] = client.get_guild(guildid).get_channel(channelid)

    print(f'Inkeeper bot ready')


@client.event
async def close():
    print(f'Inkeeper bot closing')


def parse_chatbot_string(string, user=None):
    if user is not None:
        string = string.replace('<user.mention>', user.mention)
    return string


@client.event
async def on_member_join(member):
    if not client.is_ready() or member.bot:
        return
    for bot in config['bots']:
        if member.guild.id == bot['guildid']:
            try:
                await bot['channel'].send(parse_chatbot_string(bot['chat']['hello'], member))
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print(f"ERROR: L{exc_tb.tb_lineno:4} -", e)
                await asyncio.sleep(args.refresh)
                pass


async def process_message(message, bot):
    if message.content == 'aubergiste:<debug.simulate.join>':
        await on_member_join(message.author)
    if message.content.startswith(args.command_prefix):
        cmd = message.content[len(args.command_prefix):]
        if cmd in bot['chat'].keys():
            try:
                await bot['channel'].send(parse_chatbot_string(bot['chat'][cmd], message.author))
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print(f"ERROR: L{exc_tb.tb_lineno:4} -", e)
                await asyncio.sleep(args.refresh)
                pass


@client.event
async def on_message(message):
    if not client.is_ready() or message.author.bot:
        return
    for bot in config['bots']:
        if message.channel == bot['channel']:
            await process_message(message, bot)

    # await client.process_commands(message)  # only if use commands


client.run(token)
