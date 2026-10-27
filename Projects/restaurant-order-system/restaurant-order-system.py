print("=========================================")
print("            RESTAURANT ORDER             ")
print("=========================================")
name = input("name:").lower().strip()
famely = input("family name:").lower().strip()
phon =int(input("enter phon number:"))
order_topic = {
    "ّFast Food" : False,
    "Traditional Food" : False,
    "Vegetarian Food" : False,
    "Salads" : False,
    "Cokes or coffes" : False
}
fast_food = {
    "Margherita": 0,
    "Pepperoni": 0,
    "Neapolitan": 0,
    "Buffalo chicken": 0
}
traditional_food = {
    "Kebab": 0,
    "Ghormeh sabzi": 0,
    "Zereshk rice": 0,
    "Dizi": 0
}
vegetarian_food = {
    "Ratatouille": 0,
    "Vegetable Pasta": 0,
    "Hummus": 0,
    "Lentil Soup": 0
}
salad_list = {
    "Garden salad": 0,
    "Pasta salad": 0,
    "Chicken salad": 0,
    "Mixed green salad": 0
}
coke_list = {
    "Coca-cola": 0,
    "Pepsi": 0,
    "Nescofe": 0,
    "Beer": 0
}
Checkout = False
while True:
    print("1.Fast food ","\n","2.Traditional food ","\n","3.Vegetarian food ","\n","4.Checkout ","\n","5.Exit ","\n")
    order = input("What do you want to eat? ").lower().strip()
    if order in ("1","f","fast","fast food"):
        print("1.Margherita ","\n","2.Pepperoni ","\n","3.Neapolitan ","\n","4.Buffalo chicken","\n","5.Erase","\n")
        order_topic["ّFast Food"] = True
        fast_order = input("which ones? ").lower().strip()
        if fast_order in ("1","m","margherita"):
            fast_food["Margherita"] += int(input("And how many? "))
        elif fast_order in ("2","p","pepperoni"):
            fast_food["Pepperoni"] += int(input("And how many? "))
        elif fast_order in ("3","n","neapolitan"):
            fast_food["Neapolitan"] += int(input("And how many? "))
        elif fast_order in ("4","b","buffalo","buffalo chicken"):
            fast_food["Buffalo chicken"] += int(input("And how many? "))
        elif fast_order in ("5","e","erase"):
            order_topic["ّFast Food"] = False
            if any(value > 0 for value in fast_food.values()):
                order_topic["ّFast Food"] = True
            continue
        ask_forcountinue = input("want to order more(y/n)? ")
        if ask_forcountinue in ("1","y","yes"):
            continue
        else:
            Checkout = True