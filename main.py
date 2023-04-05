import random

import numpy as np
#   TODO: Selector pomiędzy 'wybierz posiłek' a 'dodaj posiłek'
#   TODO: Selector między posiłkiem na 'słodko' lub 'słono'
#   TODO: Losowanie posiłku z tablicy
#   TODO: Selector czy posiłek odpowiada użytkownikowi
#   TODO: Warunek if
#   TODO: Wyświetlanie składników jeśli posiłek odpowiada.

dishes = ["pomidorowa","grzybowa","serowa"]
ingredients = ["cos"]
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

def add_dish():


first_choose = welcome()
if first_choose == 1:
    dish_choice(first_choose)

dish_good = dish_is_good()
while dish_good == False:
    dish_choice(first_choose)
    dish_good = dish_is_good()
