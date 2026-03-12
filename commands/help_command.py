import discord

async def handle_help(message):
    # Main help embed
    embed = discord.Embed(
        title="Linocut Bot - Command Help",
        description="Linocut is a Discord bot that manages custom substitutions and provides useful utility commands.",
        color=0x7289DA
    )
    
    # Basic Commands
    embed.add_field(
        name=" Basic Commands",
        value="`.hello` - Bot responds with 'no'\n"
              "`.ID` - Shows the current channel ID\n"
              "`.fact` - Shows a random fact about the bot",
              
        inline=False
    )
    
    # Utility Commands (Tilde prefix)
    embed.add_field(
        name="Utility Commands (~ prefix)",
        value="`~solve [equation]` - Solves mathematical expressions\n"
              "`~bing` - Shows bot latency in milliseconds\n"
              "`~wheel [item1, item2, ...]` - Randomly picks from comma-separated list\n"
              "`~count [item1, item2, ...]` - Counts items in comma-separated list",
        inline=False
    )
    
    # Substitution Management
    embed.add_field(
        name="Substitution System",
        value="`.del [trigger]` - Delete a substitution trigger\n"
              "`trigger -> response` - Create user substitution\n"
              "`.lis` - Lists available substitutions",
        inline=False
    )
    
    # Server Rules Management
    embed.add_field(
        name=" Rules Management",
        value="`.rules` - Display current channel rules\n"
              "`.set rules [text]` - Set new channel rules *(Admin only)*\n"
              "`.no rules` - Remove channel rules *(Admin only)*",
        inline=False
    )
    
    # Admin Commands
    embed.add_field(
        name="Admin Commands",
        value="`.list` - List all substitutions in current channel\n"
              "`.full` - List substitutions across all channels\n"
              "`.delete [trigger]` - Delete a substitution trigger\n"
              "`trigger ~> response` - Create admin substitution. Can be used by a minimods when set up.\n"
              "`.add [role] @user` - Add role to mentioned users. Can be used by a minimods when set up.\n"
              "`.remove [role] @user` - Remove role from mentioned users. Can be used by a minimods when set up.\n"
              "`.announce [message]` - Send announcement with special permissions. Can be used by a minimods when set up.",
        inline=False
    )
    
    # Examples
    embed.add_field(
        name="💡 Examples",
        value="• `~solve 2+2*3` → Solves to 8\n"
              "• `~wheel pizza, burger, tacos` → Randomly picks one\n"
              "• `hello ~> Hello there!` → Creates substitution\n"
              "• `.set rules Be respectful` → Sets channel rules",
        inline=False
    )
    
    embed.set_footer(text="Use commands without < > brackets. Admin commands require server admin permissions.")
    
    await message.channel.send(embed=embed)
