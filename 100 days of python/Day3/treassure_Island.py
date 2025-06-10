print("Welcome to the Treasure Island")
print("Your mission is to find the Treasure.")
choice1 = input("You're at a cross road. Where do you want to go ?\n Type 'left' or 'right': \n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an Island in the middle of the lake.\n " \
    "Type 'wait' to wait for the boat. Type 'swim' ro swim across").lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed. \
                        There is house with 3 doors. One red, one yellow , one blue. Which color do you choose?").lower()
        
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasur. You Win!")
        elif choice3 == "blue":
            print("You enter room full of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exit. Game Over")

    else:
        print("You got attacked by an angry trout. Game Over")    
else:
    print("You fell into a hole. Game Over")







