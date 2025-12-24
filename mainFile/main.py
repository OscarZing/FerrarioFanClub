
from Slots import slots 
from login import login, signup
import dbtest
logsecc=False

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

print(username)
