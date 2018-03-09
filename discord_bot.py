import os
import json
import discord
import random
import leaguestats
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='?')
tokens = {}


def get_token():
    global tokens
    if not os.path.exists('token.json'):
        print('No token file found')
        return
    with open("token.json", 'r') as token_file:
        tokens = json.loads(token_file.read())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='bot things'))

@bot.command(pass_context=True)
async def ign(ctx, in_game_name: str):
    """Gets the league profile of the user. \n
    Ignore spaces when inputting the IGN."""

    await leaguestats.get_stats(ctx, bot, in_game_name)

if __name__ == "__main__":
    get_token()
    leaguestats.initialize_watcher(tokens)
    bot.run(tokens['discord_token'])