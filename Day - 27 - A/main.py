from tkinter import *

window = Tk()
window.title("GUI by TKinter")
window.minsize(width=600, height=600)
# padding
window.config(padx=20, pady=20)


# function to change text from Hello world
def button_click():
    my_label["text"] = "New Text"
    my_label.config(text=input_text.get())


# Label
my_label = Label(text="Hello World", font=("Arial", 40, "bold"))
# Pack default is center
# my_label.pack()
# Place can manipulate GUI design alignment (so specific)
# my_label.place(x=200, y=250)
# Grid manipulate design thru grid system (cannot mix with pack)
my_label.grid(column=0, row=0)


# button prop
btn_new = Button(text="Button New", command=button_click)
btn_new.grid(column=2, row=0)


# button prop
btn = Button(text="Click Me", command=button_click)
btn.grid(column=1, row=1)


# Input (textbox)
input_text = Entry(width=10)
input_text.grid(column=3, row=2)




# always at the end v
window.mainloop()
