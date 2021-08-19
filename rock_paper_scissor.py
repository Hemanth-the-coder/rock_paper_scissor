from random import randint
elements = ["rock", "paper", "scissor"]
player_name=input("enter your name = ")
while(True):
    player_input=input("Select option = ")
    print("\n")
    if player_input not in elements:
        print("enter valid option\n")
        continue
    computer=elements[randint(0,2)]
    print("computer's option = "+computer)
    print("\n")
    if computer==elements[0] and player_input=="scissor":
        print("results = computer wins")
        print("\n")
    elif computer==elements[1] and player_input=="rock":
        print("results = computer wins")
        print("\n")
    elif computer==elements[2] and player_input=="paper":
        print("results = computer wins")
        print("\n")
    elif computer==player_input:
        print("results = tied")
        print("\n")
    else:
        print("results = "+player_name+" wins")
    print("exit   y/n")
    wish=input()
    if wish=="y":
        break 