import random

stone = 1
scissors = 2
paper = 3
while True:
    member_choice = int(input("Stone(1), Scissors(2), Paper(3): "))
    if member_choice not in [stone, scissors, paper]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue
    computer_choice = random.randint(1, 3)
    if member_choice == computer_choice:
        print("Draw!")
    elif (member_choice == stone and computer_choice == scissors) or \
            (member_choice == scissors and computer_choice == paper) or \
            (member_choice == paper and computer_choice == stone):
        print("You Won!!!")
    else:
        print("You Lose!!!")
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print("Thanks for playing!")
    break
