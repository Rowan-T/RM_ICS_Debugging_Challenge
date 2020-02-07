# Grace Lawlor
# Debugging Challenge #2 (PART I)
# 02/03/2020

# Code pulled from the TBRPG GUI Project

# Ideally, the program should create a GUI window with a non-functional TBRPG "game"
# RUNTIME ERROR COUNT: 1

# Import tkinter and random
from tkinter import *

# Setting up the window
window = Tk()
window.title('Turn Based Combat')

# Background frame and image setup
display = Frame(window, bg='grey', width=400, height=400).grid(column=0, row=0, columnspan=2, rowspan=3, padx=10, pady=10)
background = PhotoImage(file='BG_Copy')
displayB = Label(display, image=background, borderwidth=0)
displayB.background = background
displayB.grid(display, column=0, row=0, rowspan=3, columnspan=2)

# Player image (display) and grid location
character = PhotoImage(file='LorenzoBG_Copy.png')
character = character.zoom(3)
displayC = Label(display, image=character, borderwidth=0)
displayC.character = character
displayC.grid(display, column=0, row=1)

# Opponent image (display) and grid location
enemy = PhotoImage(file='DireSkeletonBG_Copy.png')
enemy = enemy.zoom(3)
displayE = Label(display, image=enemy, borderwidth=0)
displayE.enemy = enemy
displayE.grid(display, column=1, row=1)

# Player character HP (display)
status = Frame(window, bg='grey').grid(column=2, row=0, columnspan=2, rowspan=3)
CstatusHP = Label(status, text='Lorenzo HP:', width=13, height=9, anchor='w').grid(column=2, row=0)
C_HP = IntVar()
C_HP.set(20)
CstatusHPval = Label(status, textvariable=C_HP, width=10, height=9, anchor='c').grid(column=3, row=0)

# Player character HP (display)
EstatusHP = Label(status, text='Enemy HP:', width=13, height=9, anchor='w').grid(column=2, row=1)
E_HP = IntVar()
E_HP.set(50)
EstatusHPval = Label(status, textvariable=E_HP, width=10, height=9, anchor='c').grid(column=3, row=1)

# Printout frame (for spacing purposes)
PO_SPC = Frame(status, width=152, height=114).grid(column=2, row=2, columnspan=2)

# Attack feedback frame (display)
A_FB = StringVar()
A_FB.set('Prepare for battle...')
feedback = Message(status, textvariable=A_FB, font=('default', 7), width=240, anchor='w').grid(column=2, row=2, columnspan=2, sticky=NSEW)

# Abilities background frame
abilities = Frame(window, bg='grey')
abilities.grid(column=0, row=3, columnspan=4, rowspan=2)

# Ability buttons
a1 = Button(abilities,text='Vicious Mockery', width=42, height=3).grid(column=0, row=0, padx=5, pady=5)
a2 = Button(abilities,text='Magic Missile', width=42, height=3).grid(column=1, row=0, padx=5, pady=5)
a3 = Button(abilities,text='Song of Rest', width=42, height=3).grid(column=0, row=1, padx=5, pady=5)
a4 = Button(abilities,text='Expeditious Retreat (QUIT)', width=42, height=3).grid(column=1, row=1, padx=5, pady=5)

# Activate the window
window.mainloop()
