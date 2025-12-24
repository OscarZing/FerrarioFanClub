
def roulette(taschengeld):
    import random
    #from Bank import Kontostand

    #Kontostand = 1000  # Placeholder for user's balance, replace with actual balance retrieval

    print ('Wilkommen zum Roulette Spiel!')
    spielwahl = input("Willst du spielen? (j/n): ")

    if spielwahl == 'j':

    
        while spielwahl == 'j': 

            betwahl = input("Möchtest du auf eine Zahl(z), eine Farbe(f) oder Gerade/Ungerade (g) setzen?: ")

            while betwahl == 'z':
                
                bet=int(input("Wie viel möchtest du setzen? "))

                if bet > taschengeld:

                    print("Dein aktueller Kontostand ist:", taschengeld)
                    print("Du hast nicht genug moneten!")
                    continue

                if bet <= 0:

                    print("Bitte einen gültigen Betrag eingeben.")
                    continue
                    
                

                gewinnzahl = random.randint(0,36)

                tipp=int(input("Auf welche Zahl möchtest du setzen? (1-36): "))
                print("Die Gewinnzahl ist:", gewinnzahl)
                if tipp == gewinnzahl:
                    taschengeld += bet * 35
                    print("Herzlichen Glückwunsch! Du hast", bet * 35, "moneten gewonnen!")
                else:
                    taschengeld -= bet
                    print("Leider verloren. Dein neuer Kontostand ist:", taschengeld )
                
                spielwahl = input("Willst du nochmals spielen? (j/n): ")
                if spielwahl == 'j':
                    break
                elif spielwahl == 'n':
                    print("Spiel wird beendet.")
                    break
                else:
                    while spielwahl != 'j' and spielwahl != 'n':
                        print("Ungültige Eingabe.")
                        spielwahl = input("Willst du nochmals spielen? (j/n): ")

            while betwahl == 'f':

                rotListe = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
                schwarzListe = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]
                
                bet=int(input("Wie viel möchtest du setzen? "))

                if bet > taschengeld:

                    print("Dein aktueller Kontostand ist:", taschengeld)
                    print("Du hast nicht genug moneten!")
                    continue

                if bet <= 0:

                    print("Bitte einen gültigen Betrag eingeben.")
                    continue
                    
                

                gewinnzahl = random.randint(0,36)

                tipp=input("Auf welche Farbe möchtest du setzen? (Rot (r)/Schwarz (s)): ")
                def print_gewinnfarbe(gewinnzahl):
                    print("Die Gewinnzahl ist:", gewinnzahl)
                    if gewinnzahl in rotListe:
                        print("Die Gewinnfarbe ist: Rot")
                    elif gewinnzahl in schwarzListe:
                        print("Die Gewinnfarbe ist: Schwarz")
                    else:
                        print("Die Gewinnfarbe ist: Grün (00)")
                if tipp == 'r' and gewinnzahl in [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36] or tipp == 's' and gewinnzahl in [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]:
                    taschengeld += bet * 2
                    print_gewinnfarbe(gewinnzahl)
                    print("Herzlichen Glückwunsch! Du hast", bet * 2, "moneten gewonnen!")

                elif tipp == 'r' and gewinnzahl not in [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36] or tipp == 's' and gewinnzahl not in [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]:
                    taschengeld -= bet
                    print_gewinnfarbe(gewinnzahl)
                    print("Leider verloren. Dein neuer Kontostand ist:", taschengeld)

                else:
                    print("Ungültige Eingabe.")
                    continue
                
                spielwahl = input("Willst du nochmals spielen? (j/n): ")
                if spielwahl == 'j':
                    break
                elif spielwahl == 'n':
                    print("Spiel wird beendet.")
                    break
                else:
                    while spielwahl != 'j' and spielwahl != 'n':
                        print("Ungültige Eingabe.")
                        spielwahl = input("Willst du nochmals spielen? (j/n): ")


            while betwahl == 'g':
                
                bet=int(input("Wie viel möchtest du setzen? "))

                if bet > taschengeld:

                    print("Dein aktueller Kontostand ist:", taschengeld)
                    print("Du hast nicht genug moneten!")
                    continue

                if bet <= 0:

                    print("Bitte einen gültigen Betrag eingeben.")
                    continue
                    
                

                gewinnzahl = random.randint(0,36)

                tipp=input("Worauf möchtest du setzen? (Gerade (g)/Ungerade (u)): ")
                def print_gewinnzahl(gewinnzahl):
                    print("Die Gewinnzahl ist:", gewinnzahl)
                    if gewinnzahl % 2 == 0 and gewinnzahl != 0:
                        print("Die Gewinnzahl ist: Gerade")
                    elif gewinnzahl % 2 == 1:
                        print("Die Gewinnzahl ist: Ungerade")
                    else:
                        print("Die Gewinnzahl ist: 00 (weder gerade noch ungerade)")
                if tipp == 'g' and gewinnzahl % 2 == 0 and gewinnzahl != 0 or tipp == 'u' and gewinnzahl % 2 == 1:
                    print_gewinnzahl(gewinnzahl)
                    taschengeld += bet * 2
                    print("Herzlichen Glückwunsch! Du hast", bet * 2, "moneten gewonnen!")

                elif tipp == 'g' and (gewinnzahl % 2 == 1 or gewinnzahl == 0) or tipp == 'u' and (gewinnzahl % 2 == 0 and gewinnzahl != 0):
                    print_gewinnzahl(gewinnzahl)
                    taschengeld -= bet
                    print("Leider verloren. Dein neuer Kontostand ist:", taschengeld)

                else:
                    print("Ungültige Eingabe.")
                    continue
                
                spielwahl = input("Willst du nochmals spielen? (j/n): ")
                if spielwahl == 'j':
                    break
                elif spielwahl == 'n':
                    print("Spiel wird beendet.")
                    break
                else:
                    while spielwahl != 'j' and spielwahl != 'n':
                        print("Ungültige Eingabe.")
                        spielwahl = input("Willst du nochmals spielen? (j/n): ")
            
            
    else:
        print("Ungültige Eingabe, Spiel wird beendet.")
    
    return taschengeld


