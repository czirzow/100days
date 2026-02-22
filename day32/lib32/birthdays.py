import pandas as pd
import datetime as dt

csv_file = 'data/birthdays.csv'

def today():

    birthdays = {}

    try:
        df = pd.read_csv(csv_file)

    except FileNotFoundError as e:
        print(f"Unable to open file: {e}")
        return birthdays
    except pd.errors.EmptyDataError as e:
        print(f"Problem parsing file: {e}")
        return birthdays
    except pd.errors.ParserError as e:
        print(f"Problem parsing file: {e}")
        return birthdays
    else:
        now = dt.datetime.now()
        birthdays = {r.person:r.email for (_,r) in df.iterrows()
                     if r.month == now.month and r.day == now.day}
        return birthdays

