# notes for day27

#Tkinter GUI
from tkinter import *


def button_clicked():
    my_label['text'] = input.get()

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "normal"))
my_label.grid(column=0, row=0)


#Button
button = Button(text="Push Me", command=button_clicked)
button.grid(column=1 , row=1)

#Button
new_button = Button(text="Push Me 2")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)





window.mainloop()

###
if 0:
     def add(*args):
          return sum(args)

     print(add(1,2,3))

if 0:
     def calculate(n, **kwargs):
          print(kwargs)
          n += kwargs['add']
          n *= kwargs['multiply']
          return n

     calculate(2, add=3, multiple=5)
     
if 0:
     class Car:
          def __init__(self, **kw):
               self.make = kw.get('make')
               self.model = kw.get('model', 'GT-R')

     car = Car(make='Nisson')
     print(car.model)




