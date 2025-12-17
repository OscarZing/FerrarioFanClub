def slots():
    import random
    from Bank import Kontostand
    
    print('Wilkommen zum Slot Machine Spiel!')
    print('Jeder Spielzug kostet 5 moneten.')
    spielWahl = input('Willst du spielen? (j/n): ')
    if spielWahl == 'j':   

        symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '7️⃣ ']

        while spielWahl == 'j':
            print('Dein aktueller Kontostand ist:', Kontostand)
            Kontostand -=5
            if Kontostand < 5:           
                print("Du hast nicht genug moneten, um weiterzuspielen!")
                break
            else:
                slot_1 = random.randint(0,6)
                slot_2 = random.randint(0,6)
                slot_3 = random.randint(0,6)

#                print(slot_1, slot_2, slot_3)

                print(symbols[slot_1], symbols[slot_2], symbols[slot_3])

                if slot_1 == slot_2 == slot_3:
                    if slot_1 == 6:
                        Kontostand += 1005
                        print("Mega Jackpot! Du hast 1000 moneten gewonnen!")
                        print("Dein neuer Kontostand ist:", Kontostand)

                    else:
                        Kontostand += 205   
                        print("Jackpot! Du hast 200 moneten gewonnen!")
                        print("Dein neuer Kontostand ist:", Kontostand)

                else:
                    print("Nächstes mal gewinnst du!")
                    print("Dein neuer Kontostand ist:", Kontostand)

                spielWahl = input("Möchtest du nochmal spielen? (j/n): ")

                if spielWahl == 'j':
                    continue
                elif spielWahl == 'n':
                    print("Spiel wird beendet.")
                    break 
                else:
                    while spielWahl != 'j' and spielWahl != 'n':
                        print("Ungültige Eingabe.")
                        spielWahl = input("Möchtest du nochmal spielen? (j/n): ")  
        print("Spiel wird beendet.")
                    
    elif spielWahl == 'n':
        print("Spiel wird beendet.")
    else:
        print("Ungültige Eingabe, Spiel wird beendet.")

slots()