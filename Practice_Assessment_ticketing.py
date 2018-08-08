from tkinter import *

#define  class
class Circus:

    def __init__(self, name, availabilty, capacity):
        self._name = name
        self._avalibilty = availabilty
        self._capacity = capacity
        shows.append(self)
        show_names.append(name)
        print(self._name, self._availabilty)

def update_label(): 
  #set the value of show_list
   show_list.set("")
   for p in shows:
      show_list.set(show_list.get() + p._name + "  There Are: " + str(p._avalibilty) + " Tickets Available \n" )

def add():
    for p in shows:
        if p._name == selected_shows.get():
            print(selected_shows.get())
            number_of_tickets.set(number_of_tickets.get() + qty.get())


shows = []
show_times = []

Circus("10AM Show", 100, 150)
Circus("3PM Show", 50, 150)
Circus("8PM Show", 150, 250)


root= Tk()
root.title("Circus Tickets")
root.resizable(width=FALSE, height=FALSE)
root.geometry('500x300')

#set up a label to display the current showings
show_list = StringVar()

title_lbl = Label(root, text="Current Showings", justify=LEFT).grid(row=0)
shows_lbl = Label(root, textvariable=show_list).grid(row=1)

# add optionmenu
selected_shows = StringVar()
selected_shows.set(show_times[0])

show_menu = OptionMenu(root, selected_shows, *show_times)
show_menu.grid(row=2)

# entry field for the quantity of the pizza being ordered
qty = IntVar()
qty.set(0)
qty_entry = Entry(root, textvariable=qty).grid(row=3)

# button to add to order
add_btn = Button(root, text="Add to purchase", command=add).grid(row=4)

# cost label
number_of_tickets = IntVar()
number_of_tickets.set(0)
number_of_tickets_lbl = Label(root, textvariable=number_of_tickets, width=10).grid(row=1, column=1)



update_label()  
root.mainloop()
