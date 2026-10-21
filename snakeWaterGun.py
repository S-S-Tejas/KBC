import random
print(f"{'-'*25}Snake, Water and Gun{'-'*25}")
list_robot = ['Snake', 'Water', 'Gun']
print('''1. Snake
2. Water
3. Gun''')
user_choice = input("Enter 1, 2 or 3 only!: ")
while user_choice != "1" and user_choice != "2" and user_choice != "3":
    print("Choices are 1, 2 or 3 only!")
    user_choice = input("Enter 1, 2 or 3 only!: ")
computer_choice = random.choice(list_robot)

if (computer_choice == "snake" and user_choice=="1"):
    print("User: Snake")
    print("Computer: ",computer_choice)
    print("\nTie")
elif (computer_choice == "water" and user_choice=="2"):
    print("User: Water")
    print("Computer: ",computer_choice)
    print("\nTie")
elif (computer_choice == "gun" and user_choice=="3"):
    print("User: Gun")
    print("Computer: ",computer_choice)
    print("\nTie")
elif (computer_choice == "gun" and user_choice=="1"):
    print("User: Snake")
    print("Computer: ",computer_choice)
    print("\nComputer Wins")
elif (computer_choice == "snake" and user_choice=="2"):
    print("User: Water")
    print("Computer: ",computer_choice)
    print("\nComputer Wins")
elif (computer_choice == "water" and user_choice=="3"):
    print("User: Gun")
    print("Computer: ",computer_choice)
    print("\nComputer Wins")
elif (computer_choice == "gun" and user_choice=="2"):
    print("User: Water")
    print("Computer: ",computer_choice)
    print("\nUser Wins")
elif (computer_choice == "snake" and user_choice=="3"):
    print("User: Gun")
    print("Computer: ",computer_choice)
    print("\nUser Wins")
elif (computer_choice == "water" and user_choice=="1"):
    print("User: Snake")
    print("Computer: ",computer_choice)
    print("\nUser Wins")
