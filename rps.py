# Rock, Paper, Scissors Game
import random 


#options for the player
options = ["rock", "paper", "scissors"]



while True:
    computer = options[random.randint(0,2)]
    player = input("Rock, Paper, and Scissors? (or Avangers End Game?)").lower()
    if player == "End Game":
        print("Thank you for playing!!!")
        break
    elif player == computer:
        print ("Game Tied!")

    elif player == "rock":
        if computer == "paper":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)

    elif player == "paper":
        if computer == "scissors":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    
    elif player == "scissors":
        if computer == "rock":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)

    else:
        print("Invaild Input! Please choose correct options!!!!!!")
