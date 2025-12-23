from Slots import slots 
from login import login, signup
logsecc=False

print("Willkommen im Ferrario Fan Club Casino!")

logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")

while logsecc==False:
    if logopin =="l":
        logsecc=login()
    elif logopin =="r":
        if signup()==True:
            print("Registrierung erfolgreich! Du kannst dich jetzt einloggen.")
            logsecc=True
        else:
            continue
    else: 
        print("Ungültige Eingabe.")
        logopin=input("Möchtest du dich einloggen (l) oder registrieren (r)? ")
        continue


