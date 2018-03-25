print ("I'm thinking of a number between 1 and 100. You have 7 guesses")
from random import randint 
n = randint(1, 100)
n = int(n)
x = 0
x = int(x)
a = input("Have a free try! I don't know how to make it work without this line.Sorry.")
a = int(a)
if a < n :
  print("Too low")
if a > n :
  print("Too high")

 
while a != n : 
 a = input("Guess a number")
 a = int(a)
 
 if a < n :
  print("Too low")
  x = x+1
  if x == 7 :
   print("Sorry, you didn't guess it in 7 tries! You lose.")
   print("The number is")
   print(n)
   exit()
  continue

 if a > n :
  print("Too high")
  x = x+1 
  if x == 7 :
   print("Sorry, you didn't guess it in 7 tries! You lose.")
   print("The number is")
   print(n)
   exit()
  continue
  
 
if a == n :
 print("Yay!")