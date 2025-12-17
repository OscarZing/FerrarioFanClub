
def roulette():
    import random
    from Bank import Kontostand

    print ('Wilkommen zum Roulette Spiel!')
    spielwahl = input("Willst du spielen? (j/n): ")

    while spielwahl == 'j':

        bet=int(input("Wie viel möchtest du setzen? "))

        if bet > Kontostand:

            print("Du hast nicht genug moneten!")
            bet=int(input("Wie viel möchtest du setzen? "))
        else: continue

        gewinnzahl = random.randint(0,36)

#wie uf was alles söt mer setzte chöne? also ob nur zahle oder au Farb etc. bzw so strass und was es sust no für möglichkeite git?