import discord
import os

# CONFIGURATION FOR ROLE MANAGEMENT
# For commercial/public use: Replace these with your own server's role IDs or leave empty to disable
# To find role IDs: Right-click role in Discord (Developer Mode must be enabled) -> Copy ID

# Mini-mod role ID that can manage roles (set to None to disable mini-mod feature)
roleToCheck = None  # Replace with your mini-mod role ID if desired

# List of role IDs that mini-mods can manage (admins can manage all roles regardless)
# Leave empty [] to disable mini-mod role management
rolesToAdd = []  # Add your server's role IDs here if you want mini-mod management

# Working variables - do not modify
currentRolesToAdd = []
currentUsersToAdd = []

async def add_role(message, arg):
    # Check if user is admin OR has minimod role (if configured)
    user_roles = [role.id for role in message.author.roles]
    is_admin = message.author.guild_permissions.administrator
    is_minimod = roleToCheck is not None and roleToCheck in user_roles
    
    if is_admin or is_minimod:
        roleToAdd = None
        arg = arg.replace(',', '').replace('\n', '').replace('\t', '').strip()
        arg = arg.split("@")
        
        for i in range(1, len(arg)):
            mention = arg[i].strip().replace(',', '').replace('\n', '').replace('\t', '')
            has_ampersand = '&' in mention
            mention = mention.replace('<', '').replace('>', '')
            import re
            id_match = re.search(r'\d+', mention)
            
            # If we found an ID, determine if it's a role or user mention
            if id_match:
                found_id = int(id_match.group())
                
                if has_ampersand:
                    role_obj = message.guild.get_role(found_id)
                    if role_obj and found_id in rolesToAdd:
                        currentRolesToAdd.append(role_obj)
                    elif role_obj:
                        await message.channel.send(f"Role '{role_obj.name}' is not in the allowed roles list")
                else:
                    user_obj = message.guild.get_member(found_id)
                    if user_obj:
                        currentUsersToAdd.append(user_obj)
                continue
            
            # If no ID found, check if it's a role name
            mention_clean = re.sub(r'\d+', '', mention).replace('&', '').strip()
            
            role_found = False
            for role_id in rolesToAdd:
                role_obj = message.guild.get_role(role_id)
                if role_obj and mention_clean == role_obj.name:
                    currentRolesToAdd.append(role_obj)
                    role_found = True
                    break
            
            if not role_found and mention_clean:
                user_obj = message.guild.get_member_named(mention_clean)
                if user_obj:
                    currentUsersToAdd.append(user_obj)
                else:
                    await message.channel.send(f"'{mention_clean}' not found as role or user")
                    
        # now take all those users and give them the current roles to add
        for user in currentUsersToAdd:
            for role in currentRolesToAdd:
                await user.add_roles(role) 
        await message.channel.send("Finished adding the roles")
        
        # Clear the lists after use
        currentRolesToAdd.clear()
        currentUsersToAdd.clear()
    else:
        await message.channel.send("You don't have permission to use this command. Only admins and minimods can manage roles.")



async def remove_role(message, arg):
    #do the same but instead adding, remove the roles 
    # Check if user is admin OR has minimod role (if configured)
    user_roles = [role.id for role in message.author.roles]
    is_admin = message.author.guild_permissions.administrator
    is_minimod = roleToCheck is not None and roleToCheck in user_roles
    
    if is_admin or is_minimod:
        currentRolesToRemove = []
        currentUsersToRemove = []
        roleToRemove = None
        # Clean the argument by removing commas, extra spaces, and other unwanted characters
        arg = arg.replace(',', '').replace('\n', '').replace('\t', '').strip()
        # take the arg and see if it contains any @ to specific users that will get the role
        arg = arg.split("@")
        
        # Process each @ mention (skip index 0 as it's empty)
        for i in range(1, len(arg)):
            mention = arg[i].strip().replace(',', '').replace('\n', '').replace('\t', '')
            # Clean Discord mention formatting but preserve & to detect role mentions
            has_ampersand = '&' in mention
            mention = mention.replace('<', '').replace('>', '')
            # Extract numeric IDs for lookup
            import re
            id_match = re.search(r'\d+', mention)
            
            # If we found an ID, determine if it's a role or user mention
            if id_match:
                found_id = int(id_match.group())
                
                if has_ampersand:
                    # This is a role mention like <@&roleid>
                    role_obj = message.guild.get_role(found_id)
                    if role_obj and found_id in rolesToAdd:
                        currentRolesToRemove.append(role_obj)
                    elif role_obj:
                        await message.channel.send(f"Role '{role_obj.name}' is not in the allowed roles list")
                else:
                    # This is a user mention like <@userid>
                    user_obj = message.guild.get_member(found_id)
                    if user_obj:
                        currentUsersToRemove.append(user_obj)
                    # Don't show error message - might be a role name to check later
                continue
            
            # If no ID found, check if it's a role name
            mention_clean = re.sub(r'\d+', '', mention).replace('&', '').strip()
            
            # Check if mention_clean matches a role name
            role_found = False
            for role_id in rolesToAdd:
                role_obj = message.guild.get_role(role_id)
                if role_obj and mention_clean == role_obj.name:
                    currentRolesToRemove.append(role_obj)
                    role_found = True
                    break
            
            if not role_found and mention_clean:
                # Try as username if it's not empty
                user_obj = message.guild.get_member_named(mention_clean)
                if user_obj:
                    currentUsersToRemove.append(user_obj)
                else:
                    await message.channel.send(f"'{mention_clean}' not found as role or user")
                    
        # now take all those users and remove them from the current roles to remove
        for user in currentUsersToRemove:
            for role in currentRolesToRemove:
                await user.remove_roles(role) # remove the role from the user
        await message.channel.send("Finished removing the roles")
        
        # Clear the lists after use
        currentRolesToAdd.clear()
        currentUsersToAdd.clear()
    else:
        await message.channel.send("You don't have permission to use this command. Only admins and minimods can manage roles.")