# LINOCUT BOT - CONFIGURATION GUIDE

## Role Management Setup (Optional)

To use the role management features, you need to configure role IDs in these files:

### 1. commands/role_command.py
- `roleToCheck`: Set to your "mini-moderator" role ID (or leave as None to disable)
- `rolesToAdd`: List of role IDs that mini-mods can manage (or leave empty [])

### 2. commands/annoucementPermission.py  
- `announcement_role_id`: Role that can use .announce command (or None for admin-only)
- `mention_role_id`: Role to @mention in announcements (or None for no mention)

### 3. commands/admin_trigger_response.py
- `trigger_role_id`: Role that can create admin triggers with ~> (or None for admin-only)

## How to Find Role IDs
1. Enable Developer Mode in Discord (User Settings > Advanced > Developer Mode)
2. Right-click on any role in your server
3. Click "Copy ID"
4. Replace the `None` values with your copied IDs

## Example
```python
roleToCheck = 1234567890123456789  # Your mini-mod role ID
rolesToAdd = [1111111111111111111, 2222222222222222222]  # Roles mini-mods can manage
announcement_role_id = 3333333333333333333  # Role for announcements
trigger_role_id = 4444444444444444444  # Role for admin trigger creation
```

## Security Note
The original version contained hardcoded role IDs that could identify the original server. These have been removed for privacy and commercial distribution.