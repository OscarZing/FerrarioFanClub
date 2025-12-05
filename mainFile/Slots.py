def slots():
    import random
    
    print('Wilkommen zum Slot Machine Spiel!')

    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '7️⃣ ']

    while True:
        slot_1 = random.randint(0,6)
        slot_2 = random.randint(0,6)
        slot_3 = random.randint(0,6)

        print(slot_1, slot_2, slot_3)

        print(symbols[slot_1], symbols[slot_2], symbols[slot_3])

        if slot_1 == slot_2 == slot_3:
            if slot_1 == 6:
                print("Mega Jackpot!")
            print("Jackpot!")

        else:
            print("Nächstes mal gewinnst du!")

        stopInput = input("Möchtest du nochmal spielen? (j/n): ")
        if stopInput == 'j':
            continue
        elif stopInput == 'n':
            break
        else:
            print("Ungültige Eingabe, Spiel wird beendet.")
            break

slots()