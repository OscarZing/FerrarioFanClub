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

def Kredit_aufnehmen(username, amount):
    dbtest.update_debt(username, amount)
    dbtest.update_bank(username, amount)

def Kredit_abzahlen(username, amount):
    if amount > dbtest.get_balance(username):
        print("Du hast nicht genug moneten im Konto.")
        return 0
    if amount < 0:
        print("Ungültiger Betrag.")
        return 0
    else:
        dbtest.update_debt(username, -amount)
        return amount


def bank(username, taschengeld,):
    Kontostand = dbtest.get_balance(username)
    print("willkommen in der Bank!")
    print("Dein aktueller Kontostand ist:", Kontostand)
    print("Deine aktuellen Schulden sind:", dbtest.get_debt(username))
    print("Wie ich sehe hats du:", taschengeld, " moneten in der Tasche.")

    exit = False

    while exit == False:
        
        bankwahl = input("Möchtest du Geld einzahlen(e), abheben(a), Kredit verwalten(k) oder zurück ins Casino(c)?: ")
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
            print("Du hast noch", dbtest.get_debt(username), "Schulden")
            kreditwahl = input("willst du ein Kredit aufnehmen(a), oder abzahlen(b)")
            if kreditwahl == "a":
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
                Kredit_aufnehmen(username, kreditbetrag)
                print("Dein neuer Kontostand ist:", dbtest.get_balance(username))
                print("Du hast noch", dbtest.get_debt(username), "Schulden")
                print("Du hast jetzt", taschengeld, "moneten in der Tasche.")
            
            elif kreditwahl == "b":
                if dbtest.get_debt(username) == 0:
                    print("Du hast keine Schulden.")
                    continue            

                else:
                    kreditbetrag = int(input("Wie viel möchtest du zurück zahlen?: "))
                    
                    if dbtest.get_debt(username)-kreditbetrag < 0:
                        kreditbetrag = dbtest.get_debt(username) 
                    
                    a = -Kredit_abzahlen(username,kreditbetrag)
                    dbtest.update_bank(username,a)
                    print("Du hast noch", dbtest.get_debt(username), "Schulden")
                    print("Dein neuer Kontostand ist:", dbtest.get_balance(username))

            else:
                print("Ungültige eingabe.")

                

            
        elif bankwahl == "c":
            print("Rückkehr zum Casino.")
            exit = True
        else:
            print("Ungültige Eingabe.")
    
    return taschengeld

