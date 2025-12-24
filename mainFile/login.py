# lasst mich koche
import dbtest

def login():
    username = input("Gib deinen Usernamen ein: ")
    password = input("Gib dein Passwort ein: ")
    
    if dbtest.check_password(username, password)==True:
        return True
    
    
    
    '''with open("FerrarioFanClub/mainFile/login.txt", "r") as f: ---de shit isch wenn man mit de Textdatei arbeitet---
        for x in f:
           if x.strip() == username + "//" + password:
               print("Erfolgreich eingeloggt!")
               return True
        print("Username nicht gefunden oder Passwort falsch.")
        return False'''
        
def signup():
    username = input("Wähle einen Usernamen: ")

    if dbtest.check_if_user_exists(username) == True:
        return False
    else:
        password = input("Wähle ein passwort:")
        dbtest.insert_user(username,password)
        return True

    '''with open("FerrarioFanClub/mainFile/login.txt", "r+") as f: ---de shit isch wenn man mit de Textdatei arbeitet---
        for x in f:
            if x.strip().startswith(username + "//"):
                print("Username existiert bereits. Wähle einen anderen.")
                return False
        password = input("Wähle ein Passwort: ")
        f.writelines(username + "//" + password + "\n")
        return True'''

            

    
    
    
    
    
    
    
    
    
    

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

