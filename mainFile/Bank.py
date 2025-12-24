import dbtest

def abheben(username, amount):
    Kontostand = dbtest.get_balance(username)
    if amount <= Kontostand:
        dbtest.update_bank(username, -amount)
        return amount
    else:
        print("Nicht genug Guthaben.")
        return 0

def einzahlen(username, amount, taschengeld):
    if amount > taschengeld:
        print("Du hast nicht genug moneten in der Tasche.")
        return 0
    if amount < 0:
        print("Ungültiger Betrag.")
        return 0
    else:
        dbtest.update_bank(username, amount)
        return amount


def bank(username, taschengeld):
    Kontostand = dbtest.get_balance(username)
    print("willkommen in der Bank!")
    print("Dein aktueller Kontostand ist:", Kontostand)
    print("Wie ich sehe hats du:", taschengeld, " moneten in der Tasche.")

    exit = False

    while exit == False:
        
        bankwahl = input("Möchtest du Geld einzahlen(e), abheben(a) oder zurück ins Casino(c)?: ")
        if bankwahl == "e":
            einzahlung=int(input("Wie viel möchtest du einzahlen?: "))
            taschengeld -= einzahlen(username, einzahlung, taschengeld)
            print("Dein neuer Kontostand ist:", dbtest.get_balance(username))
            print("Du hast jetzt", taschengeld, "moneten in der Tasche.")
            

        elif bankwahl == "a":
            abhebung=int(input("Wie viel möchtest du abheben?: "))
            taschengeld += abheben(username, abhebung)
            print("Dein neuer Kontostand ist:", dbtest.get_balance(username))
            print("Du hast jetzt", taschengeld, "moneten in der Tasche.")
            
            
        elif bankwahl == "c":
            print("Rückkehr zum Casino.")
            exit = True
        else:
            print("Ungültige Eingabe.")
    
    return taschengeld

