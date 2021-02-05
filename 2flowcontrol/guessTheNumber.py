import random

secretNumber = random.randint(1, 20);

print ("I am thinking of a random number between 1 and 20.")

for guessesTaken in range(1, 7):
  print("Take a guess.")
  guess = int(input())

  if guess < secretNumber:
    print("Your guess is too low.")
    print("You have taken " + str(guessesTaken) + " guesses.")
  elif guess > secretNumber:
    print("Your guess is too high.")
    print("You have taken " + str(guessesTaken) + " guesses.")
  else:
    break

if guess == secretNumber:
  print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
  print("Nope! The number I was thinking of was " + str(secretNumber))