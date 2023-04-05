import random

import numpy as np
#   TODO: Selector pomiędzy 'wybierz posiłek' a 'dodaj posiłek'
#   TODO: Selector między posiłkiem na 'słodko' lub 'słono'
#   TODO: Losowanie posiłku z tablicy
#   TODO: Selector czy posiłek odpowiada użytkownikowi
#   TODO: Warunek if
#   TODO: Wyświetlanie składników jeśli posiłek odpowiada.

posilki = ["pomidorowa","grzybowa","serowa"]
skladniki = {posilki[0]:"pomidory"}

def powitanie():
    print("Witaj! Wybierz akcje poniżej wpisując odpowiednio 1 lub 2 \n 1. Wybierz Posiłek\n 2. Dodaj Posiłek")
    first_choose = int(input("Odpowiedź: "))
    return first_choose

def wybor_posilku(first_choose):
    # print(first_choose)
    print(len(posilki))
    posilki_length = len(posilki)-1
    print(posilki[random.randint(0,posilki_length)])

def posilek_is_good():
    posilek_good = int(input("Czy wybrany posiłek Ci odpowiada ? Jeśli TAK wybierz 1 lub 2 jeśli NIE:  "))
    if posilek_good == 1:
        print(skladniki)
        return True
    elif posilek_good == 2:
        return False
    else:
        print("Invalid syntax!")
        return False

first_choose = powitanie()
if first_choose == 1:
    wybor_posilku(first_choose)

posilek_good = posilek_is_good()
while posilek_good == False:
    wybor_posilku(first_choose)
    posilek_good = posilek_is_good()
