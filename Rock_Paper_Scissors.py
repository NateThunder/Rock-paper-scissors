import random

while True:
    choice = input("Lets play rock paper scissors. For rock 🪨  type 'r' for paper 📄 type p and for scissors ✀  type 's'").capitalize()
    print("\n")
    options= ("R", "P", "S")

    computer = random.choice(options)

    if choice != ("R") and choice != ("P") and choice != ("S"):
        print("Hey buddy, that not a choice!")
        break
    if computer == choice:
        match computer:
            case "R":
                print("I chose rock It's a draw. GG\n\n")
            case "p":
                print("I chose paper It's a draw. GG\n\n")
            case "s":
                print("I chose scissors It's a draw. GG\n\n")                        
    if computer == "R" and choice == "P":
        print("I chose Rock 🪨\n\nOh no you win\n\n")
    if computer == "R" and choice == "S":
        print("I chose Rock 🪨\n\nYaay I win!!!\n\n") 
    if computer == "P" and choice == "S":
        print("I chose Paper 📄\n\nAw nooo, you win!\n\n")
    if computer == "P" and choice == "R":
        print("I chose Paper 📄\n\nYaay I am the winner\n\n")    
    if computer == "S" and choice == "R":
        print("I chose Scissors ✀\n\nNoo I lose!\n\n")
    if computer == "S" and choice == "P":
        print("I chose Scissors ✀\n\nI am the winner!!!!\n\n")

    print("Cool Cool Cool, lets play again!\n\n")