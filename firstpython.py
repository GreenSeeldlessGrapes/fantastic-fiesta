while True:
    try:
        x = int(input("On a scale of 1 to 10, how much do you hate the antichrist? "))
        if x > 0:
            print("I HATE THE ANTI CHRIST " * x)
            exit()
        else:
            import random
            print("LOSER!! " * random.randint(1,100000))
            exit()
    except ValueError:
        print("I can only interpret your hatred in intergers, try again ")
    except MemoryError:
        print("YOU HATE THE ANTI CHRIST " * 7777777)
        exit()
    except OverflowError:
        print("YOU HATE THE ANTI CHRIST " * 7777777)
        exit()
