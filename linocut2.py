# This bot is linocut. It was made by Jasmine Darman(Cliff) 
# This file is what you run to set up. 

# Import handlers for help, fact, and rules commands
from commands.help_command import handle_help
from commands.fact_command import handle_fact
from commands.rules_command import handle_rules
from commands.set_rules_command import handle_set_rules
from commands.no_rules_command import handle_no_rules
from commands.role_command import add_role
from commands.role_command import remove_role
# Import additional sub handlers
from commands.sub_trigger_response import handle_sub_trigger_response
from commands.sub_trigger_lookup import handle_sub_trigger_lookup
from commands.admin_trigger_response import handle_admin_trigger_response
from commands.annoucementPermission import handle_announcement
import os
import discord
from csv import writer
from discord.ext.commands import has_permissions, CheckFailure, CommandNotFound
from dotenv import load_dotenv
import pandas as pd

from random import *
from discord.ext import commands

import numpy as np
intents = discord.Intents.all()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# client = discord.Client()
client = commands.Bot(command_prefix="~", intents = intents)


# Import command modules
from commands.solve_command import solve
from commands.bing_command import bing
from commands.wheel_command import wheel
from commands.count_command import count

# Import sub handlers for on_message
from commands.list_subs import handle_list
from commands.full_subs import handle_full
from commands.lis_subs import handle_lis
from commands.del_subs import handle_del
from commands.delete_subs import handle_delete

# Add commands to bot
client.add_command(solve)
client.add_command(bing)
client.add_command(wheel)
client.add_command(count)

button = [' ~> ']
button2 = [' -> ']


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to the following guild(s): \n'
          f'{guild.name}(Id: {guild.id} )\n')


def filter_rows_by_values(df, col, values):
    return df[df[col].isin(values) == False]


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('no')
        return
    if message.content.startswith('.ID'):
        await message.channel.send(message.channel.id)
        return
    messageContent = message.content
    if len(messageContent) > 0:
        from discord import Member
        is_admin = False
        if isinstance(message.author, Member):
            is_admin = getattr(message.author.guild_permissions, 'administrator', False)
        # .list
        if is_admin and message.content.startswith(".list"):
            await handle_list(message)
        # .full
        if is_admin and message.content.startswith(".full"):
            await handle_full(message)
        # .del
        if message.content.startswith(".del "):
            await handle_del(message)
        # .lis
        if message.content == ".lis":
            await handle_lis(message)
        # .delete
        if is_admin and message.content.startswith(".delete "):
            await handle_delete(message)
        if message.content.startswith(".add"):
            arg = message.content[5:]  # Extract everything after ".add "
            await add_role(message, arg)
        if message.content.startswith(".remove"):
            arg = message.content[8:]  # Extract everything after ".remove "
            await remove_role(message, arg)
        # .announce
        if message.content.startswith(".announce "):
            await handle_announcement(message)

    await handle_admin_trigger_response(message, button)

    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'my-csv.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
            word = False
            under = message.content.lower()
            for a in df["trigger"]:
                if under == a:
                    df = df[df.trigger == str(under)]
                    for b in df["channel"]:
                        if str(message.channel.id) == b:
                            df = df[df.channel == str(message.channel.id)]
                            index_y = int(
                                df[df["trigger"] == str(under)].index.values[0])
                            word = True
                            csv_file.close()
                            break
            if word:
                await message.channel.send(df.at[int(index_y), 'response'])
    except OSError as e:
        print(f"Error reading CSV: {e}")
    await handle_sub_trigger_lookup(message)

    # Info and rules commands
    if message.content.startswith(".help"):
        await handle_help(message)
    if message.content.startswith(".fact"):
        await handle_fact(message)
    if message.content.startswith(".set rules"):
        await handle_set_rules(message)
    if message.content.startswith(".rules"):
        await handle_rules(message)
    if message.content.startswith(".no rules"):
        await handle_no_rules(message)
    
    # Handle non-admin trigger responses with -> for non-command messages
    if not message.content.startswith(".") and not message.content.startswith("~"):
        await handle_sub_trigger_response(message, button2)
    
    # Process Discord.py commands (like ~solve, ~bing, etc.)
    await client.process_commands(message)

# Start the Discord bot
if __name__ == "__main__":
    client.run(TOKEN)




