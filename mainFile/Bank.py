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

def Kredit(username, amount):
    dbtest.update_debt(username, amount)
    dbtest.update_bank(username, amount)


def bank(username, taschengeld,):
    Kontostand = dbtest.get_balance(username)
    print("willkommen in der Bank!")
    print("Dein aktueller Kontostand ist:", Kontostand)
    print("Deine aktuellen Schulden sind:", dbtest.get_debt(username))
    print("Wie ich sehe hats du:", taschengeld, " moneten in der Tasche.")

    exit = False

    while exit == False:
        
        bankwahl = input("Möchtest du Geld einzahlen(e), abheben(a), Kredit aufnehmen(k) oder zurück ins Casino(c)?: ")
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
            
        elif bankwahl == "k":
            kreditbetrag=(input("wie viel Kredit möchtest du aufnehmen, 50(a), 100(b) 500(c) 1000(d)?: "))
            if kreditbetrag=="a":
                kreditbetrag=int(50)
            elif kreditbetrag=="b":
                kreditbetrag=int(100)   
            elif kreditbetrag=="c":
                kreditbetrag=int(500)   
            elif kreditbetrag=="d":
                kreditbetrag=int(1000)
            else:
                print("Ungültige Eingabe.")
                continue
            Kredit(username, kreditbetrag)
            print("Dein neuer Kontostand ist:", dbtest.get_balance(username))
            print("Du hast jetzt", taschengeld, "moneten in der Tasche.")
            
        elif bankwahl == "c":
            print("Rückkehr zum Casino.")
            exit = True
        else:
            print("Ungültige Eingabe.")
    
    return taschengeld

