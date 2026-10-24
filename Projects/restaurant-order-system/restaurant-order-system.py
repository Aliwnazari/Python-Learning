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