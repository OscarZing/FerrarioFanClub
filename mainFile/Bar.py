import dbtest
import time
import random

def random_events(username):
    random_event = 100
    drunk = dbtest.get_betrunkrnheit(username)/100
    print(drunk)

    random_zahl = random.randint(15,100)
    
    print(random_zahl)

    if random_zahl < drunk:
        random_event = random.randint(0,9)
    
    match random_event:
        
        case 0:
            print("1")
            random_event = 100
        case 1:
            print("2")
            random_event = 100
        case 2:
            print("3")
            random_event = 100
        case 3:
            print("4")
            random_event = 100
        case 4:
            print("5")
            random_event = 100
        case 5:
            print("6")
            random_event = 100
        case 6:
            print("7")
            random_event = 100
        case 7:
            print("8")
            random_event = 100
        case 8:
            print("9")
            random_event = 100
        case 9:
            print("10")
            random_event = 100
    




def menu():

    print("Hier ist die Getränkekarte:")
    print("-----------------------------------")
    print("Nummer | Drinkname     | Preis | Alkoholgehalt(%) | Menge(cl)")
    print("-----------------------------------")

    drinks = dbtest.get_all_drinks()
    for drink in drinks:
        print(f"{drink[0]:<6} | {drink[1]:<13} | {drink[2]:<5} | {drink[3]:<16} | {drink[4]:<8}")



def bar(username, taschengeld, start_drinking):


    timecheck= int(time.time() - start_drinking)

    print(timecheck)

    while dbtest.get_betrunkrnheit(username) != 0:
                
        dbtest.update_betrunkenheit(username,-1)
        timecheck-=1
        print(dbtest.get_betrunkrnheit(username))
        print(timecheck)

        if dbtest.get_betrunkrnheit(username) == 0 or timecheck == 0:
            timecheck = 0
            break


    print('Willkommen in der Bar!')
    wahl = input('Möchtest du die Getränkekarte sehen? (j/n): ')


    if wahl == 'j':


        

        while wahl == 'j':
            menu()
            drinkwahl=input('Um was zu bestellen geben sie die Nummer ein: um zurück ins Casino zu gehen geben sie (c) ein: ')
            
                 
            if drinkwahl== "c":
                return taschengeld, start_drinking
            
            
            elif int(drinkwahl) not in [num[0] for num in dbtest.get_all_numbers()]:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Nummer ein.")
                continue



            else:
                print("Du hast", dbtest.get_drinkname(drinkwahl), "bestellt.")
                taschengeld -= dbtest.get_price(drinkwahl)
                alk = dbtest.get_alcohol_content(drinkwahl) * dbtest.get_volume(drinkwahl)
                dbtest.update_betrunkenheit(username,alk)
                start_drinking = int(time.time())
                print(dbtest.get_betrunkrnheit(username))
                print("Du hast jetzt:", taschengeld, "moneten in der Tasche.")

                random_events(username)
                




            wahl = input("Möchtest du noch einen Drink bestellen? (j/n): ")
            if wahl == 'j':
                continue
            elif wahl == 'n':
                print("Bar wird verlassen.")
                return taschengeld, start_drinking
            else:
                while wahl != 'j' and wahl != 'n':
                        print("Ungültige Eingabe.")
                        wahl = input("Möchtest du noch einen Drink bestellen? (j/n): ")
    
    return taschengeld, start_drinking
                
                
    


if __name__ == "__main__":
   
    dbtest.update_betrunkenheit("1","50")

    x,y = bar("1", 100, 1766769120)
    
