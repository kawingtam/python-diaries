"""create a function that returns the result of a dice-roll 
(number between 1 to 6 (both inclusive)

You must call the function in your main code 
Eg

def get_dice_roll():
      <Your-Implementation>
      return <dice-roll-val>

dice_roll_val = get_dice_roll()

Then you take user input of a num between 1 to 6. 
If it matches the dice roll, then the user wins. Else the computer wins."""

import random

def get_dice_roll ():
    dice = [1,2,3,4,5,6]
    dice_roll = random.choice(dice)
    return dice_roll

user = int(input("Enter a number between 1 to 6: "))
print(get_dice_roll())

if user == get_dice_roll():
    print("User wins!")
else:
    print("Computer wins!")

