import pandas as pd
import os
from csv import writer

async def handle_sub_trigger_response(message, button2):
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sub.csv')
        messageContent = message.content
        for word in button2:
            if word in messageContent:
                msg = message.content.split(" -> ")
                trigger = msg[0].lower()
                response = msg[1]
                with open(csv_path, 'r', encoding="utf8") as csv_file:
                    colNames = ["trigger", "response", "channel"]
                    df = pd.read_csv(csv_file,
                                     names=colNames,
                                     header=None)
                    for n in df["trigger"]:
                        if trigger == n:
                            ok = False
                            df = df[df.trigger == str(trigger)]
                            for b in df["channel"]:
                                if message.channel.id == b:
                                    ok = True
                            if ok:
                                index_y = int(df[df["channel"] ==
                                    message.channel.id].index.values[0])
                                with open(csv_path, 'r', encoding="utf8") as csv_file:
                                    df = pd.read_csv(csv_file,
                                                     header=None)
                                    with open(csv_path,
                                              'w', encoding="utf8") as csv_file:
                                        df.at[index_y, 1] = response
                                        df = df.dropna()
                                        df.to_csv(csv_file,
                                                  index=False,
                                                  header=False)
                                        await message.channel.send(
                                            "changed.")
                                        return
                            else:
                                await message.channel.send(
                                    f"you said {trigger} i should say {response}"
                                )
                                subsitution = [
                                    trigger, response, message.channel.id
                                ]
                                with open(csv_path, 'a', encoding="utf8") as csv_file:
                                    writer_object = writer(csv_file)
                                    writer_object.writerow(subsitution)
                                    csv_file.close()
                                    return
                if df.shape[0] == 0:
                    await message.channel.send(
                        f"you said {trigger} i should say {response}")
                    subsitution = [trigger, response, message.channel.id]
                    with open(csv_path, 'a', encoding="utf8") as csv_file:
                        writer_object = writer(csv_file)
                        writer_object.writerow(subsitution)
                        csv_file.close()
                        return
                if trigger != n:
                    string = "You said: " + trigger + " I should say: " + response
                    n = 1970
                    split_string = [
                        string[i:i + n]
                        for i in range(0, len(string), n)
                    ]
                    subsitution = [trigger, response, message.channel.id]
                with open(csv_path, 'a', encoding="utf8") as csv_file:
                    writer_object = writer(csv_file)
                    writer_object.writerow(subsitution)
                    csv_file.close()
                for n in range(0, len(split_string)):
                    await message.channel.send(split_string[n])
    except (FileNotFoundError, OSError):
        print("Error: Could not access sub.csv file.")
    except Exception as e:
        print(f"Error processing trigger: {str(e)}")
