# Convert Miles to Kilometers.

from tkinter import Tk, Label, Button, Entry


class MilesToKm(Tk):


    def __init__(self):
        super().__init__()

        self.title('Mile to Km Converter')
        self.config(padx=20, pady=20)
        

    def calculate(self, miles):
        return round(miles * 1.60934, 2)

    def update_km_value(self):
        try:
            value = self.miles_entry.get()
            self.km_value_label['text'] = self.calculate(float(value))
        except ValueError:
            self.km_value_label['text'] = '** invalid **'

    def make_window(self):
        self.miles_entry = Entry(width=10)
        self.miles_entry.grid(column=1, row=0)

        self.miles_label = Label(text='Miles')
        self.miles_label.grid(column=2, row=0)

        self.is_equal_label = Label(text='is equal  to')
        self.is_equal_label.grid(column=0, row=1)

        self.km_value_label = Label(text='0')
        self.km_value_label.grid(column=1, row=1)

        self.km_label = Label(text='km')
        self.km_label.grid(column=2, row=1)

        self.calculate_button = Button(text='Calculate', command=self.update_km_value)
        self.calculate_button.grid(column=1, row=2)


m2k = MilesToKm()
m2k.make_window()
m2k.mainloop()


