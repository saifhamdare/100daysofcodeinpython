from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    KM_result.config(text=f"{km}")


window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=80)
window.config(padx=20,pady=20)

is_equal_label = Label(text="is equal to: ")
is_equal_label.grid(row=3,column=2)

miles_input = Entry(width=15)
miles_input.grid(row=2,column=3)

miles_label=Label(text=" Miles")
miles_label.grid(row=2,column=4)

KM_result=Label(text="0")
KM_result.grid(row=3,column=3)

KM_label=Label(text="Km")
KM_label.grid(row=3,column=4)

Calculate_button= Button(text="Calculate",command=miles_to_km)
Calculate_button.grid(row=4,column=3)

window.mainloop()

