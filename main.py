import random
import numpy as np
#   TODO: Selector między posiłkiem na 'słodko' lub 'słono'

dishes = {}
dishes_length = len(dishes)-1
choosed_dish = ""
def welcome():
    print("Witaj! Wybierz akcje poniżej wpisując odpowiednio 1 lub 2 \n 1. Wybierz Posiłek\n 2. Dodaj Posiłek")
    first_choose = int(input("Odpowiedź: "))
    return first_choose

def dish_choice(first_choose):
    global choosed_dish
    print(len(dishes))
    print(dishes.keys())
    dishes_list = []
    for keys in dishes:
        dishes_list.append(keys)
        # print(dishes_list)
    dishes_length = len(dishes_list)-1
    print(type(dishes_length))
    random_dish = random.randint(0,dishes_length)
    print(random_dish)
    choosed_dish = dishes_list[random_dish]
    print(choosed_dish)

def dish_is_good():
    global choosed_dish
    dish_good = int(input("Czy wybrany posiłek Ci odpowiada ? Jeśli TAK wybierz 1 lub 2 jeśli NIE:  "))
    if dish_good == 1:
        # print(choosed_dish)
        print(dishes[choosed_dish])
        return True
    elif dish_good == 2:
        dish_choice(first_choose=1)
        dish_is_good()
    else:
        print("Invalid syntax!")
        return False


def dish_and_ingredients_add():
    key = input("nazwa dania")
    list_of_ingredients = input("skladniki")
    def add_values_in_dict(dishes, key, list_of_ingredients):
            ''' Append multiple values to a key in
                    the given dictionary '''
            if key not in dishes:
                dishes[key] = list()
            dishes[key].append(list_of_ingredients)
            print(dishes)
            return dishes
    add_values_in_dict(dishes, key, list_of_ingredients)

def choosing():
    choose_loop = False
    while choose_loop == False:
        first_choose = welcome()
        if first_choose == 1:
            dish_choice(first_choose)
            dish_good = dish_is_good()
            while dish_good == False:
                dish_choice(first_choose)
                dish_good = dish_is_good()
        elif first_choose == 2:
            dish_and_ingredients_add()
            print(choosed_dish)
choosing()