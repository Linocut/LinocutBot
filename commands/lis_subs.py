import pandas as pd
import os

async def handle_lis(message):
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sub.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            triggerList = []
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
            dchan = message.channel.id
            df = df.loc[df['channel'] == dchan]
            df = df['trigger']
            for x in df:
                triggerList.append(x)
    except (FileNotFoundError, OSError):
        print("Error: Could not access sub.csv file.")
        return
    
    triggerList.sort()
    if not triggerList:
        await message.channel.send(
            "No triggers have been made yet. Use Trigger -> Response to make a trigger."
        )
    else:
        string = (" " + str(triggerList))
        n = 1970
        split_string = [
            string[i:i + n] for i in range(0, len(string), n)
        ]
        for n in range(0, len(split_string)):
            await message.channel.send("List message " +
                                       str(n + 1) + ":" +
                                       split_string[n])
