# CONFIGURATION FOR ANNOUNCEMENT SYSTEM  
# For commercial/public use: Replace with your server's role IDs or set to None to disable
# To find role IDs: Right-click role in Discord (Developer Mode enabled) -> Copy ID

# Role ID that can use announcements (set to None to disable non-admin announcements)
announcement_role_id = None  # Replace with your announcement role ID

# Role ID to mention in announcements (set to None for no role mention)
mention_role_id = None  # Replace with role ID you want to mention in announcements

async def handle_announcement(message):
    # Check if user has admin permissions or announcement role (if configured)
    user_roles = [role.id for role in message.author.roles]
    is_admin = message.author.guild_permissions.administrator
    has_announcement_role = announcement_role_id is not None and announcement_role_id in user_roles
    
    if is_admin or has_announcement_role:
        # Extract the announcement text after ".announce "
        announcement_text = message.content[10:]  # Remove ".announce " (9 chars + 1 space)
        
        # Create the announcement with role mention (if configured)
        if mention_role_id is not None:
            announcement_message = f"<@&{mention_role_id}> {announcement_text}"
        else:
            announcement_message = announcement_text
        
        # Send the announcement in the same channel
        await message.channel.send(announcement_message)
    else:
        await message.channel.send("You don't have permission to make announcements.")