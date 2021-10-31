
wlcmMsg = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
menuMsg = """Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
lastMsg = """***********************************
** What would you like to order? **
***********************************"""
def printer(welcoming,menu,order):
    print(welcoming)
    print(menu)
    print(order)

def ordering(menu):
    taking_orders = True
    order_list=[]
    while taking_orders:
        order = input("> ")
        existing_item = menu.find(order)
        if order == "quit":
            taking_orders = False

        elif existing_item !=-1:
            order_list.append(order)
            repeat_order = order_list.count(order)
            print("{} order of {} have been added to your meal".format(repeat_order , order))
        else:
            print("sorry we don\'t have this item")



if __name__=="__main__":
    printer(wlcmMsg,menuMsg,lastMsg)
    ordering(menuMsg)