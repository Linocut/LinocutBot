# Linocut Discord Bot

A Discord bot that manages custom substitutions and provides useful utility commands for Discord servers.

## Features

- **Custom Substitutions**: Create trigger/response pairs that automatically respond when keywords are mentioned
- **Math Solver**: Solve mathematical expressions with the `~solve` command
- **Random Tools**: `~wheel` for random selection, `~bing` for latency checking
- **Role Management**: Add/remove roles from users (configurable permissions)
- **Rules System**: Set and display channel rules
- **Announcements**: Send announcements with role mentions

## Setup

1. Create a bot at [Discord Developer Portal](https://discord.com/developers/applications)
2. Copy the bot token
3. Create a `.env` file with:
   ```
   DISCORD_TOKEN=your_bot_token_here
   DISCORD_GUILD=your_server_name_here
   ```
4. Install requirements: `pip install -r requirements.txt`
5. Run the bot: `python linocut2.py`

## Discord Permissions

**Essential Permissions:**
- View Channels
- Send Messages  
- Read Message History
- Embed Links
- Use External Emojis

**Optional Permissions:**
- Manage Roles (for role commands)
- Mention @everyone, @here, and All Roles (for announcements)
- Manage Messages (recommended)

Calculate permissions at: https://discordapi.com/permissions.html

## Configuration

For advanced features like role management, see [CONFIGURATION.md](CONFIGURATION.md)

## Commands

Type `.help` in Discord for a complete command list with examples.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See [LICENSE](LICENSE) for details.

- Free for personal/educational use
- Commercial use prohibited
- Issues: jelloismynick@gmail.com
- Creator: Jasmine Darman (Cliff)