import pandas as pd
import os

async def handle_sub_trigger_lookup(message):
    try:
        # Use absolute path to ensure file is found
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sub.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
    except (FileNotFoundError, OSError):
        # If file doesn't exist or can't be opened, just return without doing anything
        return
    
    wordInSub = False
    under = message.content.lower()
    for a in df["trigger"]:
        if under == a:
            df = df[df.trigger == str(under)]
            for b in df["channel"]:
                if message.channel.id == b:
                    df = df[df.channel == message.channel.id]
                    index_y = int(
                        df[df["trigger"] == str(under)].index.values)
                    wordInSub = True
                    break
    if wordInSub:
            await message.channel.send(df.at[int(index_y), 'response'])
