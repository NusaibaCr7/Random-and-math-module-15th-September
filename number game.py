import random

playing = True
number = random.randint(10,20)

print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = int(input("Give your best guess: "))
    
    if number == guess:
        print("You win this game!")
        print("The number was", number)
        playing = False
        
    else:
        print("Your guess isn't quite right, try again.\n")