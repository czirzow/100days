import pandas as pd

nato_file = 'csv/nato.csv'

#"a".capitalize()
nato_df = pd.read_csv(nato_file)
lookup = { c.letter:c.code for (_,c) in nato_df.iterrows() }


alpha = []
while True:
    line = input('Enter first and last name: ')
    if line.lower() == 'exit':
        break

    alpha = [ lookup[l] for l in line.upper() if l in lookup]
    print(alpha)
    print("You can type 'exit' to quit")

print("\nGlad to help you today, I'm here to translate")

