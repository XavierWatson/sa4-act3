lives = 3
number = 10
while lives > 0:
   print("I'm thinking of a number...")
   guess = int(input("What number am I thinking of? "))

   if guess == number:
      print("Congratulations! You guessed the right number.")
   if guess > number:
      print("Sorry, your guess was too high, the number was", number)
      lives -= 1
   elif guess < number:
      print("Sorry, your guess was too low, the number was", number)
      lives -= 1
   else:
      print(f"Sorry! The number was {number}.")
      lives -= 1
if lives == 0:
   print("Sorry no more guesses for you :(")
