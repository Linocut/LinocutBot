import pandas as pd
import os

async def handle_full(message):
    fullTriggerList = []
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'my-csv.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            colNames = ["trigger", "response", "channel"]
            df = pd.read_csv(csv_file, names=colNames, header=None)
            df = df['trigger']
            for x in df:
                fullTriggerList.append(x)
                fullTriggerList.sort()
            if not fullTriggerList:
                await message.channel.send(
                    "There's nothing here, which is a big problem. You cant even make anything in the chat if there's nothing here...oh well"
                )
            else:
                string = (" " + str(fullTriggerList))
                n = 1970
                split_string = [
                    string[i:i + n] for i in range(0, len(string), n)
                ]
                for n in range(0, len(split_string)):
                    await message.channel.send("Full list message " +
                                               str(n + 1) + ":" +
                                               split_string[n])
    except OSError as e:
        await message.channel.send(myString)
    except Exception as e:
        print(f"Error reading CSV: {e}")
