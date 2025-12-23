# lasst mich koche
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



""" with open("FerrarioFanClub/mainFile/login.txt") as f:
    for x in f:
        print(x)
    f.close() """