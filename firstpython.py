while True:
    try:
        x = int(input("On a scale of 1 to 10, how much do you hate the antichrist? "))
        print("I HATE THE ANTI CHRIST " * x)
        exit()
    except ValueError:
        print("I can only interpret hatred in intergers, try again ")
