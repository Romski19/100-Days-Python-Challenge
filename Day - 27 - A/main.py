from tkinter import *

window = Tk()
window.title("GUI by TKinter")
window.minsize(width=600, height=600)

# Label

my_label = Label(text="Hello World", font=("Arial", 60, "bold"))
my_label.pack()

# Input (textbox)
input_text = Entry(width=50)
input_text.pack()


# function to change text from Hello world
def button_click():
    my_label["text"] = "New Text"
    my_label.config(text=input_text.get())


# button prop
btn = Button(text="Click Me", command=button_click)
btn.pack()

# always at the end v
window.mainloop()
