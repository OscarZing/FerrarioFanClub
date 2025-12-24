import dbtest
from main import username

Kontostand = dbtest.get_balance(username)


def bank():
    Kontostand = dbtest.get_balance(username)
    print("willkommen in der Bank!")
    print("Dein aktueller Kontostand ist:", Kontostand)

    exit = False

    while exit == False:
        
        bankwahl = input("Möchtest du Geld einzahlen(e), abheben(a ) oder zurück zum Casino(c)?: ")
