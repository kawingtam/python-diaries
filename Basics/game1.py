"""Then, you can try to create a game!
Create a program that allows you to play a game of rock, paper, scissors with the computer
The computer should choose randomly between rock, paper, scissors on every turn. 
You should choose one of rock, paper, scissors. And then the regular rules apply.
You must keep track of the score (whether you or the computer is winning).
You should ask the user after each turn if they wish to exit. 
If they choose to continue playing, initiate the next turn. 
The first player (computer or you) to reach 5 points wins)"""

import random
user_win = 0
computer_win = 0
print("The first player (computer or you) to reach 5 points wins)")

while user_win < 5 and computer_win < 5:
    my_list = ['rock', 'paper', 'scissors']
    computer = random.choice(my_list)


    user = input("Choose between rock, paper, scissors: ")


    if user == computer:
        print("Draw")
        print("User Points: ",user_win)
        print("Computer Points: ",computer_win)

    elif user == "rock" and computer == "scissors":
        print("User win")
        user_win += 1
        print("User Points: ",user_win)
        print("Computer Points: ",computer_win)

    elif user == "paper" and computer == "rock":
        print("User win")
        user_win += 1
        print("User Points: ",user_win)
        print("Computer Points: ",computer_win)

    elif user == "scissors" and computer == "paper":
        print("User win")
        user_win += 1
        print("User Points: ",user_win)
        print("Computer Points: ",computer_win)

    else:
        computer_win +=1
        print("Computer win")
        print("User Points: ",user_win)
        print("Computer Points: ",computer_win)

    if user_win == 5:
        print("User Win!")
        break
        
    if computer_win == 5:
        print("Computer Win!")
        break
        
    ask = input("Play or exit: ")
    if ask == "exit":
        break
