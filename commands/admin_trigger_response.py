import pandas as pd
import os
from csv import writer

# CONFIGURATION FOR ADMIN TRIGGER CREATION
# Role that can create admin triggers (in addition to server admins)
# Set to None to allow only admins to create admin triggers (~> responses)
trigger_role_id = None  # Replace with your trigger-creation role ID if desired

async def handle_admin_trigger_response(message, button):
    # Check if user is admin or has the trigger role (if configured)
    user_roles = [role.id for role in message.author.roles]
    is_admin = hasattr(message.author, 'guild_permissions') and message.author.guild_permissions and message.author.guild_permissions.administrator
    has_trigger_role = trigger_role_id is not None and trigger_role_id in user_roles
    
    if is_admin or has_trigger_role:
        messageContent = message.content
        if not message.content.startswith("."):
            for word in button:
                if word in messageContent:
                    try:
                        msg = message.content.split(" ~> ")
                        trigger = msg[0].lower()
                        response = msg[1]
                        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'my-csv.csv')
                        
                        with open(csv_path, 'r', encoding="utf8") as csv_file:
                            colNames = ["trigger", "response", "channel"]
                            df = pd.read_csv(csv_file, names=colNames, header=None)
                            
                            for n in df["trigger"]:
                                if trigger == n:
                                    ok = "nothing"
                                    df = df[df.trigger == str(trigger)]
                                    for b in df["channel"]:
                                        if str(message.channel.id) == b:
                                            ok = "something"
                                    if ok == "something":
                                        index_y = int(df[df["channel"] == str(message.channel.id)].index.values[0])
                                        with open(csv_path, 'r', encoding="utf8") as csv_file:
                                            df = pd.read_csv(csv_file, header=None)
                                            with open(csv_path, 'w', encoding="utf8") as csv_file:
                                                df.at[index_y, 1] = response
                                                df = df.dropna()
                                                df.to_csv(csv_file, index=False, header=False)
                                                await message.channel.send("changed.")
                                                return
                                    if ok == "nothing":
                                        await message.channel.send(f"you said {trigger} i should say {response}")
                                        substitution = [trigger, response, message.channel.id]
                                        with open(csv_path, 'a', encoding="utf8") as csv_file:
                                            writer_object = writer(csv_file)
                                            writer_object.writerow(substitution)
                                            csv_file.close()
                                            return
                            
                            if df.shape[0] == 0:
                                await message.channel.send(f"you said {trigger} i should say {response}")
                                substitution = [trigger, response, message.channel.id]
                                with open(csv_path, 'a', encoding="utf8") as csv_file:
                                    writer_object = writer(csv_file)
                                    writer_object.writerow(substitution)
                                    csv_file.close()
                                    return
                            if trigger != n:
                                string = "You said: " + trigger + " I should say: " + response
                                n = 1970
                                split_string = [
                                    string[i:i + n]
                                    for i in range(0, len(string), n)
                                ]
                                substitution = [trigger, response, message.channel.id]
                                with open(csv_path, 'a', encoding="utf8") as csv_file:
                                    writer_object = writer(csv_file)
                                    writer_object.writerow(substitution)
                                    csv_file.close()
                                for n in range(0, len(split_string)):
                                    await message.channel.send(split_string[n])
                            
                    except (FileNotFoundError, OSError):
                        print("Error: Could not access my-csv.csv file.")
                    except Exception as e:
                        print(f"Error processing admin trigger: {str(e)}")
