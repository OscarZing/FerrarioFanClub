def slots():
    import 
    
    print('Wilkommen zum Slot Machine Spiel!')

    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '7️⃣']

    while True:
        slot_1 = random.randint(0,3)
        slot_2 = random.randint(0,3)
        slot_3 = random.randint(0,3)

        print(slot_1, slot_2, slot_3)

        print(symbols[slot_1], symbols[slot_2], symbols[slot_3])

        if slot_1 == slot_2 == slot_3:
            if slot_1 == 6:
                print("Mega Jackpot! You win the grand prize!")
            print("Jackpot! You win!")

        else:
            print("Better luck next time!")

slots()