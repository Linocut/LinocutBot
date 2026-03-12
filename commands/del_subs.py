import pandas as pd
import os

async def handle_del(message):
    try:
        demsg = message.content.split(".del ")
        dtrig = demsg[1]
        word = False
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sub.csv')
        
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
            for a in df["trigger"]:
                if dtrig == a:
                    df = df[df.trigger == str(dtrig)]
                    for b in df["channel"]:
                        if message.channel.id == b:
                            df = df[df.channel == message.channel.id]
                            index_arr = df[df["trigger"] == str(dtrig)].index.values
                            index_y = int(index_arr[0]) if len(index_arr) > 0 else None
                            word = True
                            break
        if word:
                with open(csv_path, 'r', encoding="utf8") as csv_file:
                    colNames = ["trigger", "response", "channel"]
                    df = pd.read_csv(csv_file, names=colNames, header=None)
                    df = df.drop([index_y])
                    with open(csv_path, 'w', encoding="utf8") as csv_file:
                        df.to_csv(csv_file, index=False, header=False)
                        await message.channel.send(f"Deleted {dtrig}")
    except (FileNotFoundError, OSError):
        print("Error: Could not access sub.csv file.")
    except Exception as e:
        print(f"Error deleting trigger: {str(e)}")
