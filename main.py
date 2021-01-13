import random
import math
 # Taking Inputs
lower = int(input("Enter Lowest number:- ")) 
 
upper = int(input("Enter highest number:- "))  
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
 
 # Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
     
     # taking guessing number as input
    guess = int(input("Guess a number:- ")) 
     
    # Condition testing
    if x == guess:  
       print("You won now go", count, " try")
       # Once guessed, loop will break 
       break
    elif x > guess:
       print("Sorry you guessed to low!")
    elif x < guess:
       print("Sorry you guessed to high")
 
# If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(upper - lower + 1, 2):
   print("\nThe number is %d"%x)
   print("\tYou lost get out")
 
# Better to use This source Code on pycharm!56263500
