number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))
if guess > number:
   print("Sorry, your guess was too high, the number was", number)
elif guess < number:
   print("Sorry, your guess was too low, the number was", number)
else:
   print("Congratulations! You guessed the right number.")