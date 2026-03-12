import pandas as pd
import os
from csv import writer

async def handle_set_rules(message):
    msg = message.content.split(".set rules")
    rule = msg[1]
    
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rules.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            df = pd.read_csv(csv_file, header=None)
            for n in df[0]:
                if int(message.channel.id) == int(n):
                    with open(csv_path,'r', encoding="utf8") as csv_file:
                        df = pd.read_csv(csv_file, header=None)
                        with open(csv_path, 'w', encoding="utf8") as csv_file:
                            index_v = df[df[0] == int(message.channel.id)].index.values
                            df.at[int(index_v[0]) if len(index_v) > 0 else 0, 1] = rule
                            df = df.dropna()
                            df.to_csv(csv_file, index=False, header=False)
                            await message.channel.send("rule changed.")
                            return
        
        # If we reach here, the channel ID wasn't found, so add a new rule
        line = [message.channel.id, rule]
        with open(csv_path, 'a', encoding="utf8") as csv_file:
            writer_object = writer(csv_file)
            writer_object.writerow(line)
            csv_file.close()
            await message.channel.send(f"Rules set to: {rule}")
    except (FileNotFoundError, OSError):
        print("Error: Could not access rules.csv file.")
    except Exception as e:
        print(f"Error setting rules: {str(e)}")
