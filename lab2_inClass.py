import random

choices = ["Rock", "Paper", "Scissors"]


def getRandomChoice(a, b):
    return random.randint(a, b)


def printChoice(choices, index, msg):
    print(msg + " " + choices[index])


def chooseWiner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        print("It's a tie")
    elif (playerChoice == 0 and computerChoice == 2) \
            or (playerChoice == 2 and computerChoice == 1) \
            or (playerChoice == 1 and computerChoice == 0):
        print("Player wins!")
    else:
        print("Computer wins!")


def main():
    try:
        userInput = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        if userInput not in choices:
            raise ValueError("Invalid input! Please enter Rock, Paper, Scissors")
        playerChoice = choices.index(userInput)
        printChoice(choices, playerChoice, "Player choice is")
        computerChoice = getRandomChoice(0, 2)
        printChoice(choices, computerChoice, "Computer choice is")
        chooseWiner(playerChoice, computerChoice)
    except ValueError as e:
        print(f"Error {e}")


main()
