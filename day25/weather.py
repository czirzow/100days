import pandas

data = pandas.read_csv('data/weather_data.csv')
#print(type(data))
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

count = len(temp_list)
total = 0
for value in temp_list:
    total += value

print(f"total: {total}")
print(f"count: {count}")
if count == 0:
    print("something went wrong")
else:
    print(f"total: {total/count}")

#but of course ...
print("the easier way...")
print(sum(temp_list) / len(temp_list))

# and even easier:
print(data['temp'].mean())

