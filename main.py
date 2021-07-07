from tkinter import *

def calculate():
    miles =float(mile_input.get())
    km = round(miles * 1.609)
    km_label.config(text= km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label_text = Label(text = "is equal to")
label_text.grid(column=0, row=1)

mile_input = Entry()
mile_input.grid(column=1,row=0)

km_label = Label(text=0)
km_label.grid(column=1, row=1)

button = Button(text="Calculate", command= calculate)
button.grid(column=1, row=2)

miles_unit_label = Label(text = "Miles")
miles_unit_label.grid(column=2, row=0)

km_unit_label = Label(text = "km")
km_unit_label.grid(column=2, row=1)




window.mainloop()