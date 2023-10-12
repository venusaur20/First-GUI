#My first GUI yayy!
from tkinter import *



#--------------------- # SETS UP CANVAS
hasan_draws = Tk() 
hasan_draws.title("Hello World!")
hasan_draws.geometry('1000x500')


#--------------------- # METHODS
def suprise(): #creates function that alters the text to what has been inputed in the input bar
    typed_message = "You wrote: " + user_input.get()
    message.configure(text = typed_message)

#--------------------- # MENUS
menu = Menu(hasan_draws)
pop_down = Menu(menu)
pop_down.add_command(label = 'New')
menu.add_cascade(label = 'File', menu = pop_down)
hasan_draws.config(menu = menu)


#--------------------- # TEXT
message = Label(hasan_draws, text = "Ive been wanting to say hello for so long... ") #creates text
message.grid(column = 3, row = 4) #sets postion of the text


#--------------------- # INPUT BARS
user_input = Entry(hasan_draws, width = 50) #creates input bar of 50units length
user_input.grid(column = 3, row = 5)  #sets position of the input bar



#--------------------- # BUTTONS
clicky = Button(hasan_draws, text = "Hopefully this works" , bg = "blue", fg = "orange", command = suprise) #creates button with various qualities and runs "suprise" when clicked
clicky.grid(column = 5, row = 4) #sets postion of button


#--------------------- # FINALIZATION
hasan_draws.mainloop() #runs the GUI