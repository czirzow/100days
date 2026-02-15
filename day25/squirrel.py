# the squirrel project.
import pandas as pd

input_file = 'squirrel/2018_central_park.csv'
output_file = 'squirrel/results.csv'
field = 'Primary Fur Color'



squirrels = pd.read_csv(input_file)
#print(squirrels[field])

colors_dict = {
        "color": [],
        "qty": [],
        }

grouped = squirrels.groupby(by=field, dropna=True)
for name, positions in grouped:
        colors_dict['color'].append(name)
        colors_dict['qty'].append(len(positions))

distinct_colors =  pd.DataFrame(colors_dict)
distinct_colors.to_csv(output_file)




