import random
choice = input("Lets play rock paper scissors. For rock 🪨  type 'r' for paper 📄 type p and for scissors ✀  type 's'").capitalize()
print("\n")
options= ("R", "P", "S")

computer = random.choice(options)

if choice != ("R") and choice != ("P") and choice != ("S"):
    print("Hey buddy, that not a choice!")
    exit()
if computer == choice:
    print(f"I chose {computer} It's a draw. GG")
if computer == "R" and choice == "P":
    print("I chose Rock 🪨\n\nOh no you win")
if computer == "R" and choice == "S":
    print("I chose Rock 🪨\n\nYaay I win!!!") 
if computer == "P" and choice == "S":
    print("I chose Paper 📄\n\nAw nooo, you win!")
if computer == "P" and choice == "R":
    print("I chose Paper 📄\n\nYaay I am the winner")    
if computer == "S" and choice == "R":
    print("I chose Scissors ✀\n\nNoo I lose!")
if computer == "S" and choice == "P":
    print("I chose Scissors ✀\n\nI am the winner!!!!")