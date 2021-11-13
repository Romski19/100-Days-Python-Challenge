from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=60, pady=20)


def conversion():
    miles = input_miles.get()
    km = 1.609344 * float(miles)
    label_result.config(text=km)


input_miles = Entry(width=15)
input_miles.grid(column=1, row=0)

label_mile = Label(text="Miles", font=("Arial", 10, "bold"))
label_mile.grid(column=2, row=0)
label_mile.config(padx=10, pady=10)

# labels result

label_equal_to = Label(text="equal to", font=("Arial", 10, "bold"))
label_equal_to.grid(column=0, row=1)

label_result = Label(text="result", font=("Arial", 10, "bold"))
label_result.grid(column=1, row=1)
label_result.config(padx=20, pady=0)

label_km = Label(text="Kilometer/s", font=("Arial", 10, "bold"))
label_km.grid(column=2, row=1)

btn = Button(text="Calculate", command=conversion)
btn.grid(column=1, row=2)
label_result.config(padx=0, pady=20)

window.mainloop()
