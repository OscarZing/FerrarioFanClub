import dbtest



def menu():
    print("Hier ist die Getränkekarte:")
    print("-----------------------------------")
    print("Nummer | Drinkname     | Preis | Alkoholgehalt(%) | Menge(cl)")
    print("-----------------------------------")

    drinks = dbtest.get_all_drinks()
    for drink in drinks:
        print(f"{drink[0]:<6} | {drink[1]:<13} | {drink[2]:<5} | {drink[3]:<16} | {drink[4]:<8}")



def bar(username, taschengeld):


    print('Willkommen in der Bar!')
    wahl = input('Möchtest du die Getränkekarte sehen? (j/n): ')


    if wahl == 'j':

        while wahl == 'j':
            menu()
            drinkwahl=input('welchen drink möchten sie bestellen? geben die die Nummer ein: ')
            if int(drinkwahl) not in [num[0] for num in dbtest.get_all_numbers()]:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Nummer ein.")
                continue



            else:
                print("Du hast", dbtest.get_drinkname(drinkwahl), "bestellt.")
                taschengeld -= dbtest.get_price(drinkwahl)
                alk = dbtest.get_alcohol_content(drinkwahl) * dbtest.get_volume(drinkwahl)
                dbtest.update_betrunkenheit(username,alk)
                
                print("Du hast jetzt:", taschengeld, "moneten in der Tasche.")




            wahl = input("Möchtest du noch einen Drink bestellen? (j/n): ")
            if wahl == 'j':
                continue
            elif wahl == 'n':
                print("Bar wird verlassen.")
            else:
                while wahl != 'j' and wahl != 'n':
                        print("Ungültige Eingabe.")
                        wahl = input("Möchtest du noch einen Drink bestellen? (j/n): ")
                
                
    


if __name__ == "__main__":
   
    bar("1", 100)
