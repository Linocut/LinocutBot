import pandas as pd
import os

async def handle_rules(message):
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rules.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            df = pd.read_csv(csv_file, header=None)
            pizza = False
            for n in df[0]:
                if str(message.channel.id) == str(n):
                    with open(csv_path, 'r', encoding="utf8") as csv_file:
                        colNames = ["channel", "rules"]
                        df = pd.read_csv(csv_file,
                                         names=colNames,
                                         header=None)
                        number = df[df["channel"] == int(
                            message.channel.id)].index.values
                        await message.channel.send(df.at[int(number[0]) if len(number) > 0 else 0,
                                                         "rules"])
                        pizza = True
    except (FileNotFoundError, OSError):
        print("Error: Could not access rules.csv file.")
    except Exception as e:
        print(f"Error accessing rules: {str(e)}")
    
    if not pizza:
        await message.channel.send("no rules~")
