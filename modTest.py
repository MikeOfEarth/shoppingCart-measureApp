from random import uniform
cart = {'milk' : {'total':3,"price":1.41},'bread' : {'total':2,"price":2.15}}
# name = input('Howdy! What\'s your name?\t')

# for k in cart:
#     print(f"{cart[k]['total']} {k}\'s for {cart[k]['price']}")

def area():
    w=input('What is the width of your area?\t')
    h=input('And the height?\t')
    print(f'Your square footage is {float(w)*float(h)} sqft')

def circumference():
    r=input('What is the radius of your circle?\t')
    print(f'Your circumference is {round(2*3.14159*float(r),2)} units')