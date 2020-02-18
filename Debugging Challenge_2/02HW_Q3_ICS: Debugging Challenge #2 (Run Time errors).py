from tkinter import *
print('henry')
# Base window - this is required in order for the program to run
win=Tk()

# Title setting for the program window
win.title("Get those frames to fit!")

# Mainframe that holds everything, the big bag!
mf=Frame(win)
mf.grid(row=0, column=0)

# Widget Holders - Frames
# These frames are nested inside of the mainframe
# This is the parent of all the widgets you make, they will go into one of these three frames

# Top - Left Frame
wf1=Frame(mf, bg='red')
wf1.grid(row=0, column=0)

# Top - Right Frame
wf2=Frame(mf, bg='blue')
wf2.grid(row=0, column=1)

# Bottom - Frame (Spans the two column widths)
wf3=Frame(mf, bg='yellow')
wf3.grid(row=1, column=0, columnspan=2, sticky="NSEW")

# Sub Frames These will hold the size of the program
# NOTE: the parent of these frames are the widget holders
# NOTE_2: the grid locations are 0,0 for each one since they're nested in the widget frame
sf1 = Frame(wf1, height=350, width=400, bg='red')
sf1.grid(row=0, column=0)
sf2 = Frame(wf2, height=350, width=150, bg='blue')
sf2.grid(row=0, column=0)
sf3 = Frame(wf3, height=300, width=550, bg='yellow')
sf3.grid(row=0, column=0, columnspan=2, rowspan=2)

# Widgets in wf1
photo = PhotoImage(file="pikachu.png")
pikachu=Label(wf1, image=photo)
pikachu.photo=photo  #backup reference to the photo
pikachu.grid(row=0, column=0, stick=(E,W))

# Widgets in wf2
l1 = Label(wf2, text="Enemy Hp:")
l1.grid(row=0, column=0, sticky=EW)
l2 = Label(wf2, text="Player Hp:")
l2.grid(row=1, column=0, sticky=EW)

ehp = IntVar() #Don't forget the parentheses! Without them this does not work!
ehp.set(10)

enemy_hp = Label(wf2, textvariable=ehp)
enemy_hp.grid(row=0, column=1, sticky="EW")

# Widgets in wf3
b1=Button(wf3, text="atk1")
b1.grid(row=0, column=0, sticky=(N,S,E,W))

b2=Button(wf3, text="atk2")
b2.grid(row=0, column=1, sticky=(N,S,E,W))

b3=Button(wf3, text="atk3")
b3.grid(row=1, column=0, sticky=(N,S,E,W))

b4=Button(wf3, text="atk4")
b4.grid(row=1, column=1, sticky=(N,S,E,W))

print('henry')
# Calls the GUI window, THIS MUST be below all of your Tk code.
# If this is not present a window will not appear
win.mainloop()
