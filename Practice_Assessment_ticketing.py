from tkinter import *

#define  class
class Circus:

    def __init__(self, name, availabilty, capacity):
        self._name = name
        self._avalibilty = availabilty
        self._capacity = capacity
        shows.append(self)

def update_label(): 
  #set the value of show_list
   show_list.set("")
   for p in shows:
      show_list.set(show_list.get() + p._name + "  There Are: " + str(p._avalibilty) + " Tickets Available \n" )


shows = []
show_times = []

Circus("10AM Show", 100, 150)
Circus("3PM Show", 50, 150)
Circus("8PM Show", 150, 250)


root= Tk()
root.title("Circus Tickets")
root.resizable(width=FALSE, height=FALSE)
root.geometry('500x300')

#set up a label to display the cureent showings
show_list = StringVar()

title_lbl = Label(root, text="Current Showings", justify=LEFT).grid(row=0)
shows_lbl = Label(root, textvariable=show_list).grid(row=1)

#set up a option menu

selected_shows = StringVar()
selected_shows.set(show_times[0])

#three parameters: Location, selected item, list of all items
ticket_menu = OptionMenu(root, selected_shows, *show_times)
ticket_menu.grid(row=1)


pizza_price = StringVar()
price_lbl = Label(root, textvariable=pizza_price, width=10)
price_lbl.grid(row=1, column=1)

select_btn = Button(root, text="Select", command=update_label)
select_btn.grid(row=1, column=1)


update_label()  
root.mainloop()
