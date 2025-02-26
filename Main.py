from tkinter import *

top = Tk()
top.title("My pets")

listbox = Listbox(top, height=10,
                  width=15,
                  bg="gray",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")

top.geometry("300x250")

label = Label(top, text=" PETS")

listbox.insert(1, "Cat")
listbox.insert(2, "Wolf")
listbox.insert(3, "Dog")
listbox.insert(4, "Hamster")
listbox.insert(5, "Guppy")
listbox.insert(6, "Gerbil")
listbox.insert(7, "Snake")

listbox.pack()
label.pack()

scroll_bar = Scrollbar(top)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(top,
                 yscrollcommand=scroll_bar.set)

for line in range(1, 8):
    mylist.insert(END, "Cosen Pet x " + str(line))

mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

top.mainloop()
