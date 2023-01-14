import random 
import sys

range_top = input("Type a number: ")



if range_top.isdigit():
    range_top = int(range_top)

    if range_top <= 0:
        print("Please type a number larger than 0")
        sys.exit()
else:
        print("Please type a number next time")
        sys.exit()
        
        
randomNumber = random.randint(0, range_top)  
guesses = 0

while True:
    
    guesses += 1
    
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("please type a number next time")
        continue
    
    if user_guess == randomNumber:
        print("congratulations you got it right")
        break
    
    elif user_guess > randomNumber:
        print("Too high")
    
    else:
        print("too low")
        
print("You got it in", guesses, "guesses")