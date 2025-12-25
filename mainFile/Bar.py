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
                print("Du hast", dbtest.get_drink_name(drinkwahl), "bestellt.")
                taschengeld -= dbtest.get_drink_price(drinkwahl)
                print("Du hast jetzt:", taschengeld, "moneten in der Tasche.")


            




if __name__ == "__main__":
   
    bar()
