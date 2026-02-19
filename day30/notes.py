# notes day 30
#



def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
try:
    make_pie(4)
except Exception as e:
    print(f"Error: {e}")
else:
    pass

