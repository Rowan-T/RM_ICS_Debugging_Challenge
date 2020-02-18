# Grace Lawlor
# Debugging Challenge #2 (PART II)
# 02/05/2020

# Code pulled from the Fast Food Kiosk Project

# Ideally, the program should create a GUI window with a non-functional Chipotle ordering kiosk
# RUNTIME ERROR COUNT: 1


# Import tkinter
from tkinter import *

# Create the window
Window = Tk()
Window.title('Chipotle Burrito Maker')

# Default value for the Order variable
Order = 'Your Order:\n\nCost:'

# Title and images
Burrito = PhotoImage(file='Burrito_Copy.png')
LeftImage = Label(Window, image=Burrito, borderwidth=0).grid(column=0, row=0)
ProgramTitle = Label(Window, text='Chipotle Burrito Maker', font=('arial bold', 18), fg='white', bg='dark red', width=52, height=3)\
    .grid(column=1, row=0, columnspan=13)
RightImage = Label(Window, image=Burrito, borderwidth=0).grid(column=14, row=0)

# Base screen layout and widgets
BaseFrame = Frame(Window)
BaseFrame.grid(column=0, row=1, columnspan=15, rowspan=3)
BasePrompt = Label(BaseFrame, text='Choose a base for your burrito.', font=('arial', 13), width=107, height=4)
BasePrompt.grid(column=0, row=1, columnspan=15)
Chicken = Button(BaseFrame, text='Chicken', bg='light green', width=28, height=4)
Chicken.grid(column=0, row=2, columnspan=3, padx=5, pady=5)
Steak = Button(BaseFrame, text='Steak', bg='light green', width=28, height=4)
Steak.grid(column=4, row=2, columnspan=3, padx=5, pady=5)
CarneAsada = Button(BaseFrame, text='Carne Asada', bg='light green', width=28, height=4)
CarneAsada.grid(column=8, row=2, columnspan=3, padx=5, pady=5)
Barbacoa = Button(BaseFrame, text='Barbacoa', bg='light green', width=28, height=4)
Barbacoa.grid(column=12, row=2, columnspan=3, padx=5, pady=5)
Carnitas = Button(BaseFrame, text='Carnitas', bg='light green', width=28, height=4)
Carnitas.grid(column=2, row=3, columnspan=3, padx=5, pady=5)
Sofritas = Button(BaseFrame, text='Sofritas', bg='light green', width=28, height=4)
Sofritas.grid(column=6, row=3, columnspan=3, padx=5, pady=5)
Vegetarian = Button(BaseFrame, text='Vegetarian', bg='light green', width=28, height=4)
Vegetarian.grid(column=10, row=3, columnspan=3, padx=5, pady=5)

# Options layout and widgets
OptionsFrame = Frame(Window)
OptionsFrame.grid(column=0, row=4, columnspan=15, rowspan=3)
OrderFeedback = StringVar()
OrderFeedback.set(Order)
OrderPriceDisplay = Label(OptionsFrame, variable=OrderFeedback, font=('arial', 11), bg='light grey', width=107, height=4)
OrderPriceDisplay.grid(column=0, row=4, columnspan=15, pady=10)
GoBackButton = Button(OptionsFrame, text='Go Back', bg='light green', width=28, height=4)
GoBackButton.grid(column=4, row=5, columnspan=3, padx=5, pady=5)
ContinueButton = Button(OptionsFrame, text='Continue', bg='light green', width=28, height=4)
ContinueButton.grid(column=8, row=5, columnspan=3, padx=5, pady=5)
RestartButton = Button(OptionsFrame, text='Restart', bg='light green', width=28, height=4)
RestartButton.grid(column=4, row=6, columnspan=3, padx=5, pady=5)
QuitButton = Button(OptionsFrame, text='Quit', bg='light green', width=28, height=4)
QuitButton.grid(column=8, row=6, columnspan=3, padx=5, pady=5)

# Create the window
Window.mainloop()
