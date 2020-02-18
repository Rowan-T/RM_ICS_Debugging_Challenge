import tkinter
from tkinter import *
from tkinter import messagebox
food=True
order=[]

#menu time
menu_options={1: {'name':'Burger', 'price':2.79, 'desc':'Delicious meaty meal!'},
              2: {'name':'Custard', 'price':2.29, 'desc':'Just like grandma used to make!'},
              3: {'name':'Corn Dog', 'price':4.99, 'desc':'Now with extra corn!'},
              4: {'name':'Grilled Cheese', 'price':4.99, 'desc':'Now with extra cheese!'},
              5: {'name': 'Curds', 'price':3.49, 'desc':'A classic!'},
              6: {'name':'Bottled Water', 'price':1.69, 'desc':'A refreshing beverage!'},
              7: {'name':'Soft Drink', 'price':1.69, 'desc':'Fizzy and delicious!'},
              8: {'name':'Classic Value Basket', 'price':3.00, 'desc':'For commoners!'},
              9: {'name':'Premium Value Basket', 'price':4.00, 'desc':'Fit for a king!'}}

burger_add_ons={1: {'name':'Cheese', 'price':.99, 'desc':'Solid cow juice!'},
                2: {'name':'Lettuce', 'price':.99, 'desc':'Leafy greens!'},
                3: {'name':'Tomato', 'price':.99, 'desc':'Is it a fruit or vegetable?'},
                4: {'name':'Onion', 'price':.99, 'desc':'Delicious rings!'},
                5: {'name':'Mayonnaise', 'price':0, 'desc':'The good sauce!'},
                6: {'name':'Veggie Burger', 'price':1.99, 'desc':'For the vegans.'}}

custard_add_ons={1: {'name':'Cheesecake Chunks', 'price':.99, 'desc':'Heart attack in custard form!'},
                 2: {'name':'Hershey Bars', 'price':.99, 'desc':'Your favorite snack, now in custard!'},
                 3: {'name':'Peanut Butter', 'price':.99, 'desc':'Peanut sauce, now in custard!'},
                 4: {'name':'Brownie Bites', 'price':.99, 'desc':'Brownie delight, now in custard!'},
                 5: {'name':'Strawberry', 'price':.99, 'desc':'Your favorite berry, now in custard!'}}

def chungus()
    if messagebox.askyesno('Menu', 'Would you like a burger?'):
        order.append(menu_options[1]['name'])
        if messagebox.askyesno('Add-Ons', 'Would you like cheese?'):
            print(burger_add_ons[1]['name'], burger_add_ons[1]['price'])
            order.append(burger_add_ons[1]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like lettuce?'):
            print(burger_add_ons[2]['name'], burger_add_ons[2]['price'])
            order.append(burger_add_ons[2]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like tomato?'):
            print(burger_add_ons[3]['name'], burger_add_ons[3]['price'])
            order.append(burger_add_ons[3]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like onion?'):
            print(burger_add_ons[4]['name'], burger_add_ons[4]['price'])
            order.append(burger_add_ons[4]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like mayonnaise?'):
            print(burger_add_ons[5]['name'], burger_add_ons[5]['price'])
            order.append(burger_add_ons[5]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like this to be a veggie burger?'):
            print(burger_add_ons[6]['name'], burger_add_ons[6]['price'])
            order.append(burger_add_ons[6]['name'])
    elif messagebox.askyesno('Menu', 'Would you like some custard?'):
        order.append(menu_options[2]['name'])
        if messagebox.askyesno('Add-Ons', 'Would you like cheesecake chunks?'):
            print(custard_add_ons[1]['name'], custard_add_ons[1]['price'])
            order.append(custard_add_ons[1]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like Hershey bars?'):
            print(custard_add_ons[2 'name'], custard_add_ons[2]['price'])
            order.append(custard_add_ons[2]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like peanut butter?'):
            print(custard_add_ons[3]['name'], custard_add_ons[3]['price'])
            order.append(custard_add_ons[3]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like brownie bites?'):
            print(custard_add_ons[4]['name'], custard_add_ons[4]['price'])
            order.append(custard_add_ons[4]['name'])
        elif messagebox.askyesno('Add-Ons', 'Would you like strawberry?'):
            print(custard_add_ons[5]['name'], custard_add_ons[5]['price'])
            order.append(custard_add_ons[5]['name'])
    elif messagebox.askyesno('Menu', 'Would you like some corn dog?'):
        print(menu_options[3]['name'], menu_options[3]['price'])
        order.append(menu_options[3]['name'])
    elif messagebox.askyesno('Menu', 'Would you like grilled cheese?'):
        print(menu_options[4]['name'], menu_options[4]['price'])
        order.append(menu_options[4]['name'])
    elif messagebox.askyesno('Menu', 'Would you like some curds?'):
        print(menu_options[5]['name'], menu_options[5]['price'])
        order.append(menu_options[5]['name'])
    elif messagebox.askyesno('Menu', 'Would you like some bottled water?'):
        print(menu_options[6]['name'], menu_options[6]['price'])
        order.append(menu_options[6]['name'])
    elif messagebox.askyesno('Menu', 'Would you like a soft drink?'):
        print(menu_options[7]['name'], menu_options[7]['price'])
        order.append(menu_options[7]['name'])
    elif messagebox.askyesno('Menu', 'Would you like a classic value basket?'):
        print(menu_options[8]['name'], menu_options[8]['price'])
        order.append(menu_options[8]['name'])
    elif messagebox.askyesno('Menu', 'Would you like a premium value basket?'):
        print(menu_options[9]['name'], menu_options[9]['price'])
        order.append(menu_options[9]['name'])


def final()
    input("How would you like to pay for this?\n> ")
    price=0
    for item in order:
        if item == 'Premium Value Basket':
            price = price + menu_options[9]['price']
        elif item == 'Classic Value Basket':
            price = price + menu_options[8]['price']
        elif item == 'Soft Drink':
            price = price + menu_options[7]['price']
        elif item == 'Bottled Water':
            price = price + menu_options[6]['price']
        elif item == 'Curds':
            price = price + menu_options[5]['price']
        elif item == 'Grilled Cheese':
            price = price + menu_options[4]['price']
        elif item == 'Corn Dog':
            price = price + menu_options[3]['price']
        elif item == 'Custard':
            price = price + menu_options[2]['price']
        elif item == 'Cheesecake Chunks':
            price = price + custard_add_ons[1]['price']
        elif item == 'Hershey Bars':
            price = price + custard_add_ons[2]['price']
        elif item == 'Peanut Butter':
            price = price + custard_add_ons[3]['price']
        elif item == 'Brownie Bites':
            price = price + custard_add_ons[4]['price']
        elif item == 'Strawberry':
            price = price + custard_add_ons[5]['price']
        elif item == 'Burger':
            price = price + menu_options[1]['price']
        elif item == 'Cheese':
            price = price + burger_add_ons[1]['price']
        elif item == 'Lettuce':
            price = price + burger_add_ons[2]['price']
        elif item == 'Tomato':
            price = price + burger_add_ons[3]['price']
        elif item == 'Onion':
            price = price + burger_add_ons[4]['price']
        elif item == 'Mayonnaise':
            price = price + burger_add_ons[5]['price']
        elif item == 'Veggie Burger':
            price = price + burger_add_ons[6]['price']
    price = price * 1.01
    print(order)
    print('Your total is:', price)


root=Tk()
root.title("CULVER'S")

#frame time for baby
mf = Frame(root, height=300, width=400)
mf.grid(row=0, column=0, sticky=(N, S, E, W)
win = Frame(root, height=200, width=400)
win.grid(row=1, column=0, sticky=(N, S, E, W)

#button madness
b1 = Button(text="Options", command=chungus)
b1.grid(row=2, column=0, sticky=(N, S, E, W)
b2 = Button(text="Print", command=final)
b2.grid(row=3, column=0, sticky=(N, S, E, W)
b3 = Button(text="Quit", command=root.destroy)
b3.grid(row=4, column=0, sticky=(N, S, E, W)

#labels and other shit
giglamesh=StringVar()
giglamesh.set("Your Options for Tonight's Menu")
Label(win, textvariable=giglamesh).grid(row=0, column=0)

#peechure
hell=PhotoImage(file='logo.png')
Label(mf, image=hell).grid(row=1, column=0)

root.mainloop()

#when complete it should look like an order window
#property of ella ristic
#error count: 8
