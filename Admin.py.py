#Admin details
admin_keys= {"Rathan":"Rathanprakash1998"}

#stock details
menu= {1:{'dishname': 'Tandoori chicken','dishid':1, 'dishquantity':4,'price':240,'discount':40,'stock':10}, 
        2:{'dishname': 'Vegan Burger','dishid':2, 'dishquantity':1,'price':320,'discount':20,'stock':10},
        3:{'dishname': 'Truffle cake','dishid':3, 'dishquantity':500,'price':900,'discount':30,'stock':10}}

def add_new_dish():
    dishname= input("Enter the dish name:")
    dishid= int(input("Enter the dishid:"))
    dishquantity= int(input("Enter the dishquantity:"))
    price= int(input("Enter the dish name:"))
    discount= int(input("Enter the dish name:"))
    stock= int(input("Enter the dish name:"))
    menu[dishid] = {
        "dishname": dishname,
        "dishid": dishid,
        "dishquantity":dishquantity,
        "price": price,
        "discount": discount,
        "stock": stock,
    }
    print("The dish" + dishname + "is >>> successfully <<< added")
    return menu

def edit_from_dish():
    dishid = int(input("Enter the dishid which you want to edit:"))
    a = input("Enter the dishname")
    b = int(input("Enter the dishquantity"))
    c = int(input("Enter the discount"))
    d = int(input("Enter the price"))
    e = int(input("Enter the stock")) 
    menu[dishid]["dishname"]=a
    menu[dishid]["dishquantity"]=b
    menu[dishid]["discount"]=c
    menu[dishid]["price"]=d
    menu[dishid]["stock"]=e
    print("dish edited successfully")
    return menu

def price_cal(dish):
    dish = int(input("Enter dishid:"))
    d= menu[dish]["price"]
    c= menu[dish]["discount"]
    n= d-(d*c/100)
    return n 

def piece_dish(i):
        print("dish Name:", menu[i]["dish name"])
        print("Pric:", menu[i]["price"],"INR")
        print("Dish ID:", menu[i]["Dish ID"])
        print("Stock:", menu[i]["Stock"])
        print("Quantity:", menu[i]["dishquantity"],"pieces")
        print("Discount:", menu[i]["discount"],"%")

def gm_dish(i):
        print("dish Name:", menu[i]["dish name"])
        print("Pric:", menu[i]["price"],"INR")
        print("Dish ID:", menu[i]["Dish ID"])
        print("Stock:", menu[i]["Stock"])
        print("Quantity:", menu[i]["dishquantity"],"gm")
        print("Discount:", menu[i]["discount"],"%")

def show_menu():
    b=[1,2]
    a=[3]
    print("Here is he menu of Rathan restaurant")
    for i in b:
        piece_dish(i)
    for i in a:
        gm_dish(i)

def remove_dish():
    l = int(input("Enter he dishid which you want to exit"))
    menu.pop(l)
    print("remove item sucsessfully")
    return menu
       
       
    

