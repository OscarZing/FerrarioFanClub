
def roulette():
    import random
    from Bank import Kontostand

    print ('Wilkommen zum Roulette Spiel!')
    spielwahl = input("Willst du spielen? (j/n): ")

    if spielwahl == 'j':

    
        while spielwahl == 'j': 

            betwahl = input("Möchtest du auf eine Zahl(z) oder Farbe(f) setzen?: ")

            while betwahl == 'z':
                
                bet=int(input("Wie viel möchtest du setzen? "))

                if bet > Kontostand:

                    print("Dein aktueller Kontostand ist:", Kontostand)
                    print("Du hast nicht genug moneten!")
                    continue

                if bet <= 0:

                    print("Bitte einen gültigen Betrag eingeben.")
                    continue
                    
                

                gewinnzahl = random.randint(0,36)

                tipp=int(input("Auf welche Zahl möchtest du setzen? (0-36): "))
                print("Die Gewinnzahl ist:", gewinnzahl)
                if tipp == gewinnzahl:
                    Kontostand += bet * 35
                    print("Herzlichen Glückwunsch! Du hast", bet * 35, "moneten gewonnen!")
                else:
                    Kontostand -= bet
                    print("Leider verloren. Dein neuer Kontostand ist:", Kontostand)
                
                spielwahl = input("Willst du nochmals spielen? (j/n): ")
                if spielwahl == 'j':
                    continue
                elif spielwahl == 'n':
                    print("Spiel wird beendet.")
                    break
                else:
                    while spielwahl != 'j' and spielwahl != 'n':
                        print("Ungültige Eingabe.")
                        spielwahl = input("Willst du nochmals spielen? (j/n): ")
            
            
            print("Spiel wird beendet.")

    elif spielwahl == 'n':
        print("Spiel wird beendet.")
    else:
        print("Ungültige Eingabe, Spiel wird beendet.")

roulette()
#wie und uf was alles söt mer setzte chöne? also ob nur zahle oder au Farb etc. bzw so strass und was es sust no für möglichkeite git?