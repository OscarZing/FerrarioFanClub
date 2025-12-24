
from Slots import slots 
from login import login, signup
import dbtest
logsecc=False

dbtest.show_table('user')


print("Willkommen im Ferrario Fan Club Casino!")

logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")


while logsecc==False:
    if logopin =="l":
        logsecc=login()
        print("Erfolgreich eingeloggt!")
    elif logopin =="r":
        if signup()==True:
            print("Registrierung erfolgreich! Du kannst dich jetzt einloggen.")
            logsecc=True
        else:
            print("Username existiert bereits. Wähle einen anderen.")
            continue
    else: 
        print("Ungültige Eingabe.")
        logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")
        continue


