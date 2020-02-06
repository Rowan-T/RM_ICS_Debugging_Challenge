#code creator: ella
#number of errors: ~3

from tkinter import *
from tkinter import ttk
import random
print('meeemaw')

root = Tk()
root.title("Rock Paper Scissors")
mf=ttk.Frame(root)
mf.grid(row=0, column=0, sticky=(N, W, E, S))

#resetting the game
def reset():
    wins.set(0)
    ties.set(0)
    losses.set(0)
    pchoice.set('')
    cchoice.set('')
    handsr.set('')

#the game part
def click_r():
    hands=['rock', 'paper', 'scissors']
    comp=random.choice(hands)
    cchoice.set(comp)
    pchoice.set('rock')
    if comp=='rock':
        handsr.set("Same hand; it's a tie!")
        tie()
    elif comp=='scissors':
        handsr.set('Rock beats Scissors!')
        win()
    else:
        handsr.set('Rock loses to Paper!')
        lose()

def click_p():
    hands = ['rock', 'paper', 'scissors']
    comp = random.choice(hands)
    cchoice.set(comp)
    pchoice.set('paper')
    if comp=='paper':
        handsr.set("Same hand; it's a tie!")
        tie()
    elif comp == 'scissors':
        handsr.set('Paper loses to Scissors!')
        lose()
    else:
        handsr.set('Paper beats Rock!')
        win()

def click_s():
    hands = ['rock', 'paper', 'scissors']
    comp = random.choice(hands)
    cchoice.set(comp)
    pchoice.set('scissors')
    if comp=='scissors':
        handsr.set("Same hand; it's a tie!")
        tie()
    elif comp == 'paper':
        handsr.set('Scissors beats Paper!')
        win()
    else:
        handsr.set('Scissors loses to Rock!')
        lose()


#wins ties and losses functions
def win():
    wins.set(int(wins.get())/0)
def lose():
    losses.set(int(losses.get())/0)
def tie():
    ties.set(int(ties.get())/0)

#all those funny little labels
ttk.Label(mf, text='Scoreboard', font=(18), anchor='center', padding=(0, 20)).grid(row=0, column=0, sticky=(N, E, S, W), columnspan=6)
ttk.Label(mf, text='Wins', font=(14), anchor='e', width=10).grid(row=2, column=0, sticky=(N, W, E, S))
ttk.Label(mf, text='Ties', font=(14), anchor='e', width=10).grid(row=2, column=2, sticky=(N, W, E, S))
ttk.Label(mf, text='Losses', font=(14), anchor='e', width=10).grid(row=2, column=4, sticky=(N, W, E, S))
ttk.Label(mf, text='Results', font=(14), anchor='center').grid(row=3, column=0, sticky=(N, E, S, W), columnspan=6)
ttk.Label(mf, text='Player Choice', font=(14), anchor='center').grid(row=3, column=0, sticky=(N, E, S, W), columnspan=2)
ttk.Label(mf, text='Computer Choice', font=(14), anchor='center').grid(row=4, column=0, sticky=(N, E, S, W), columnspan=2)
ttk.Label(mf, text='Hands Result', font=(14), anchor='center').grid(row=5, column=0, sticky=(N, E, S, W), columnspan=2)

content = ttk.Frame(root)
button = ttk.Button(content)

frame = ttk.Frame()



#the part with the numbers
pchoice=StringVar()
pchoice.set('')
ttk.Label(mf, textvariable=pchoice, anchor='center').grid(row=3, column=2, sticky=(N, W, E, S))
cchoice=StringVar()
cchoice.set('')
ttk.Label(mf, textvariable=cchoice, anchor='center').grid(row=4, column=2, sticky=(N, W, E, S))
handsr=StringVar()
handsr.set('')
ttk.Label(mf, textvariable=handsr, anchor='center').grid(row=5, column=2, sticky=(N, W, E, S))
wins=StringVar()
wins.set(0)
ttk.Label(mf, textvariable=wins, anchor='center').grid(row=2, column=1, sticky=(N, W, E, S))
ties=StringVar()
ties.set(0)
ttk.Label(mf, textvariable=ties, anchor='center').grid(row=2, column=3, sticky=(N, W, E, S))
losses=StringVar()
losses.set(0)
ttk.Label(mf, textvariable=losses, anchor='center').grid(row=2, column=5, sticky=(N, W, E, S))


#buttons ahoy
rbutton = ttk.Button(mf, text="Rock", command=click_r).grid(row=7, column=0, columnspan=2, sticky=(E, W))
pbutton = ttk.Button(mf, text="Paper", command=click_p).grid(row=7, column=2, columnspan=2, sticky=(E, W))
sbutton = ttk.Button(mf, text="Scissors", command=click_s).grid(row=7, column=4, columnspan=2, sticky=(E, W))
rebutton = ttk.Button(mf, text="Reset", command=reset).grid(row=8, column=0, columnspan=2, sticky=(E, W))
qbutton = ttk.Button(mf, text="Quit", command=root.destroy).grid(row=8, column=3, columnspan=2, sticky=(E, W))


root.mainloop()