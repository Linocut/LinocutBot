import pandas as pd
import os

async def handle_no_rules(message):
    try:
        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'rules.csv')
        with open(csv_path, 'r', encoding="utf8") as csv_file:
            df = pd.read_csv(csv_file, header=None)
            for n in df[0]:
                if int(message.channel.id) == int(n):
                    index_x = int(
                        df[df[0] == int(message.channel.id)].index.values[0])
                    df = df.drop([index_x])
                    df = df.dropna()
                    with open(csv_path, 'w', encoding="utf8") as csv_file:
                        df.to_csv(csv_file, index=False, header=False)
                        await message.channel.send(
                            f"Deleted the rules. :)")
    except (FileNotFoundError, OSError):
        print("Error: Could not access rules.csv file.")
    except Exception as e:
        print(f"Error deleting rules: {str(e)}")
