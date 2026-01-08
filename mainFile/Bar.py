import dbtest
import time
import random

def random_events(username, taschengeld):
    random_event = 100
    drunk = dbtest.get_betrunkrnheit(username)/100
    #print(drunk)

    random_zahl = random.randint(15,100)
    
    print(random_zahl)

    if random_zahl < drunk:
        random_event = random.randint(0,9)
    
    match random_event:
        
        case 0:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du bist in einem Mülleimer aufgewacht, doch du bemerkst du hast 100 Moneten mehr in der Tasche.","\n","Du gest zurück ins Casino")
            random_event = 100
            taschengeld += 100
            return taschengeld, True
        case 1:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du liegst in einem umbekannten bett, und bemerkst das all dein Geld verschwunden ist.","\n","Du gest zurück ins Casino.")
            taschengeld = 0
            random_event = 100
            return taschengeld, True
        case 2:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du liegst in deinem Bett und entscheidest dich zurück ins Casino zu gehen")
            random_event = 100
            return taschengeld, True
        case 3:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Es scheint das du gestorben und in der Hölle gelandet bist.","\n","Du gest aber ein Deal mit dem Teufel ein und wirst wiederbelebt.","\n","Wär braucht Liebe wenn man auch Glückspiel hat oder?")
            random_event = 100
            return taschengeld, True
        case 4:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du bist im Krankenhaus.","\n","Du gest zurück ins Casino")

            random_event = 100
            return taschengeld, True
        case 5:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du bist zuhause, aber als du auf dein Handy schaust siehst du, dass du all deine Moneten, welche du im Konto hattest, Gespendet hast .","\n","Du gest zurück ins Casino")
            dbtest.update_bank(username,-dbtest.get_balance(username))
            random_event = 100
            return taschengeld, True
        case 6:
            print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Du bist zuhause, aber als du auf dein Handy schaust siehst du, dass Elon Musk dein Kontostand verdoppelt hat.","\n","Du gest zurück ins Casino")
            dbtest.update_bank(username,dbtest.get_balance(username))
            random_event = 100
            return taschengeld, True
        
        case 7:
            print("8")
            random_event = 100
        case 8:
            print("9")
            random_event = 100
        case 9:
            print("10")
            random_event = 100
    return taschengeld
    




def menu():

    print("Hier ist die Getränkekarte:")
    print("-----------------------------------")
    print("Nummer | Drinkname     | Preis | Alkoholgehalt(%) | Menge(cl)")
    print("-----------------------------------")

    drinks = dbtest.get_all_drinks()
    for drink in drinks:
        print(f"{drink[0]:<6} | {drink[1]:<13} | {drink[2]:<5} | {drink[3]:<16} | {drink[4]:<8}")



def bar(username, taschengeld, start_drinking):
    
    case == False


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

                taschengeld, case = random_events(username,)
                if case == True:
                    return taschengeld, start_drinking
                else:
                    pass
                




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
   
    '''dbtest.update_betrunkenheit("1","50")

    x,y = bar("1", 100, 1766769120)'''

    print("Du wachst auf, mit starken Kopfschmerzen und schaust dich um.","\n", "Es scheint das du gestorben und in der Hölle gelandet bist.","\n","Du gest aber ein Deal mit dem Teufel ein und wirst wiederbelebt","\n","Wär braucht Liebe wenn man auch Glückspiel hat")

    
