cart = {}
totCost=0
name = 'not declared'
from random import uniform
    
def shoppingCart():
    global name
    
    name = input('Howdy! What\'s your name?\t')
    ask()

def ask():
    while True:
        ask=input(f'Hey there {name}! What would you like to do in your shopping cart? Options: Add/Remove/Display/Quit\t')
        if ask == 'Add' or ask == 'add':
            add()
        elif ask == 'Remove' or ask == 'remove':
            remove()
        elif ask == 'Display' or ask == 'display':
            display()
        elif ask == 'Quit' or ask == 'quit':
            print('Have a nice day!')
            break
        else:
            print("Sorry! Please try again, selecting one of the available options\n")

            
def add():
    item = input('What would you like to add to your cart?\t')
    num = input('How many would you like to add?\t')
    
    if item not in cart:
        cart[item]={'total':num,'price':(round(uniform(1.10, 4.59), 2))}
        print(f'Great, {num} {item} added!\n')
    else:
        cart[item]['total']+=num


def remove():
    item = input('What would you like to remove from your cart?\t')
    
    if item in cart:
        num = input('How many would you like to remove?\t')
        cart[item]['total']=int(cart[item]['total'])-int(num)
        if cart[item]['total']<1:
            print(f"All {item}\'s removed from cart\n")
            del cart[item]
        else:
            print(f"{num} {item}\'s removed, {cart[item]['total']} remain\n")
    else:
        print(f"Sorry there are no {item}\'s in your cart.\nPlease try again\n")

        
def cost():
    global totCost
    totCost=0
    for k in cart:
        totCost=float(totCost)+((int(cart[k]['total']))*(float(cart[k]['price'])))

        
def display():
    global totCost
    cost()
    totCost="%.2f" % round(totCost, 2)
    print('\nYour cart contains:')
    for k in cart:
        print(f"{cart[k]['total']} {k}\'s for {cart[k]['price']} each")
    print(f'Your check out total is {totCost}.\n')

    
shoppingCart()