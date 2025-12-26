from Roulette import roulette
from Slots import slots 
from login import login, signup
import dbtest
import Bank
import time
import Bar
logsecc=False
taschengeld=100
start_drinking = 0
dbtest.show_table('user')


print("Willkommen im Ferrario Fan Club Casino!")

logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")


while logsecc==False:
    if logopin =="l":
        logsecc, username = login()
        if logsecc == True:
            print("Erfolgreich eingeloggt!")
        else:
            print("Username nicht gefunden oder Passwort falsch.")

    elif logopin =="r":
        if signup()==True:
            logopin = "l"
            print("Registrierung erfolgreich! Du kannst dich jetzt einloggen.")
        else:
            print("Username existiert bereits. Wähle einen anderen. Oder melde dich mit diesem an:")
    else: 
        print("Ungültige Eingabe.")
        logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")
        continue

print("Hallo", username, "!")
print("Du hast", taschengeld, "moneten in der Tasche.")

while True:

    option = input("Möchtest du in die Bank (b) Bar (ba), Slots (s) spielen oder Roulette (r) spielen?: ")

    if option == 'b':
        taschengeld = Bank.bank(username, taschengeld)
    
    if option == "ba":
        taschengeld, start_drinking = Bar.bar(username,taschengeld,start_drinking)

    elif option == 's':
        taschengeld = slots(taschengeld)

    elif option == 'r':
        taschengeld = roulette(taschengeld)