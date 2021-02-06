
print("Tell us a number, dearie.")

try:
  number = int(input())
  while number > 1:
    if number % 2 == 0:
      number = number/2
      print(number)
    else:
      number = number * 3 + 1
      print(number)
except:
  print("Sorry, that is not a valid integer.")