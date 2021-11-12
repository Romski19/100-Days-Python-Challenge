import tkinter

window = tkinter.Tk()
window.title("GUI by TKinter")
window.minsize(width=600, height=600)

#Label

my_label = tkinter.Label(text="Hello World", font=("Arial", 60, "bold"))
my_label.pack()


# always at the end v
window.mainloop()