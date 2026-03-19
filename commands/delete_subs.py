import pandas as pd
import os

async def handle_delete(message):
    demsg = message.content.split(".delete ")
    dtrig = demsg[1]
    word = False
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'my-csv.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
            for a in df["trigger"]:
                if dtrig == a:
                    df = df[df.trigger == str(dtrig)]
                    for b in df["channel"]:
                        if str(message.channel.id) == str(b).strip():
                            matched = df[df["channel"].astype(str).str.strip() == str(message.channel.id)]
                            if not matched.empty:
                                index_y = int(matched.index.values[0])
                                word = True
                                break
            if word:
                try:
                    with open(csv_path, 'r', encoding="utf8") as csv_file:
                        colNames = ["trigger", "response", "channel"]
                        df = pd.read_csv(csv_file,
                                         names=colNames,
                                         header=None)
                        df = df.drop([index_y])
                    with open(csv_path, 'w', encoding="utf8") as csv_file:
                        df.to_csv(csv_file, index=False, header=False)
                        await message.channel.send(f"Deleted {dtrig}")
                except OSError as e:
                    print(f"Error updating CSV: {e}")
    except OSError as e:
        print(f"Error reading CSV: {e}")
