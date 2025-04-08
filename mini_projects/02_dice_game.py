# Dice Game: User vs computer, first to 5 points wins
from random import randrange

print("THE DICE GAME")

user_score = 0
computer_score = 0

while True:
    try:
        print("-----")
        print("OPTIONS")
        print("-----")
        print("0. Exit the game")
        print("1. Play your turn")
        print("2. Check the score board")
        print("3. Reset scores")
        print("-----")
        option = int(input("Enter an option (0/1/2/3): "))
    
        if option == 1:
                user_dice = randrange(1, 7)
                computer_dice = randrange(1, 7)
                if user_dice == 5:
                    user_score += 1
                    print("-----")
                    print(f"Your rolled... {user_dice}")
                    print("Yay!! You are the winner 🎉")
                    print(f"Your score: {user_score}")
                    print(f"Computer score: {computer_score}")
                    print("-----")
                elif computer_dice == 5:
                    computer_score += 1
                    print("-----")
                    print(f"Your rolled... {user_dice}")
                    print(f"And computer's dice rolled... {computer_dice}")
                    print("Oh no, computer wins this time!")
                    print(f"Your score: {user_score}")
                    print(f"Computer score: {computer_score}")
                    print("Enter 1 if you want another try!")
                    print("-----")
                else:
                    print("-----")
                    print(f"Your rolled... {user_dice}")
                    print(f"And computer's dice rolled... {computer_dice}")
                    print("It looks like you are both out of luck! Enter 1 to play again") 
                    print("-----")

        elif option == 2:
            print("-----")
            print(f"Your score: {user_score}")
            print(f"Computer score: {computer_score}")
            print("-----")

        elif option == 3:
            user_score = 0
            computer_score = 0
            print("-----")
            print("New game, scores are back to zero!")
            print(f"Your score: {user_score}")
            print(f"Computer score: {computer_score}")
            print("-----")

        elif option == 0:
            break

    except ValueError:
        print("Please enter a valid option(0/1/2/3)")