# lasst mich koche
def login():
    username = input("Gib deinen Usernamen ein: ")
    password = input("Gib dein Passwort ein: ")
    

    with open("FerrarioFanClub/mainFile/login.txt", "r") as f:
        for x in f:
           if x.strip() == username + "//" + password:
               print("Erfolgreich eingeloggt!")
               return True
           print("Username nicht gefunden oder Passwort falsch.")
           return False
        f.close()
    
def signup():
    username = input("Wähle einen Usernamen: ")

    with open("FerrarioFanClub/mainFile/login.txt", "r+") as f:
        for x in f:
            if x.strip().startswith(username + "//"):
                print("Username existiert bereits. Wähle einen anderen.")
                return False
        password = input("Wähle ein Passwort: ")
        f.writelines(username + "//" + password + "\n")
        return True

            
    
    #open("FerrarioFanClub/mainFile/login.txt", "a").writelines(username + "//" + password + "\n")
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    signup()


"""
    userid = input("Gib deine UserID ein: ")
    try:
        loginfile = open("FerrarioFanClub/mainFile/login.txt", "a")
        loginfile.writelines(userid + "\n")
        loginfile.close()
    except FileNotFoundError:
        passloginfile = open("FerrarioFanClub/mainFile/login.txt", "x")
        passloginfile.writelines(userid + "\n")
        passloginfile.close()

    loginfile = open("FerrarioFanClub/mainFile/login.txt", "r")
    userid = loginfile.readline()
    """



""" with open("FerrarioFanClub/mainFile/login.txt") as f:
    for x in f:
        print(x)
    f.close() """

