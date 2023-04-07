import random

import numpy as np
#   TODO: Selector między posiłkiem na 'słodko' lub 'słono'

dishes = ["pomidorowa","grzybowa","serowa"]
ingredients = ["cos"]
dishes_length = len(dishes)-1
def welcome():
    print("Witaj! Wybierz akcje poniżej wpisując odpowiednio 1 lub 2 \n 1. Wybierz Posiłek\n 2. Dodaj Posiłek")
    first_choose = int(input("Odpowiedź: "))
    return first_choose

def dish_choice(first_choose):
    # print(first_choose)
    print(len(dishes))
    dishes_length = len(dishes)-1
    print(dishes[random.randint(0,dishes_length)])

def dish_is_good():
    dish_good = int(input("Czy wybrany posiłek Ci odpowiada ? Jeśli TAK wybierz 1 lub 2 jeśli NIE:  "))
    if dish_good == 1:
        print(ingredients[0])
        return True
    elif dish_good == 2:
        return False
    else:
        print("Invalid syntax!")
        return False

def add_dish(first_choose):
    global dishes
    new_dish_name = str(input("Podaj nazwe dania które chcesz wpisać do swojej listy: ")).lower()
    print(new_dish_name)
    print(type(new_dish_name))
    print(dishes)
    if new_dish_name in dishes:
        print("To danie znajduje się już na liście.")
    else:
        dishes.append(new_dish_name)
        print(dishes)
        new_ingredients_name = str(input("Podaj nazwe pierwszego składnika: ")).lower()
        ingredients_list = []
        lists = {new_dish_name: ingredients_list}
        lists[new_dish_name].append(new_ingredients_name)
        print(f"The new list named {new_dish_name} has been created.")
        print(lists[new_dish_name])


first_choose = welcome()
if first_choose == 1:
    dish_choice(first_choose)
    dish_good = dish_is_good()
    while dish_good == False:
        dish_choice(first_choose)
        dish_good = dish_is_good()
elif first_choose == 2:
    add_dish(first_choose)
