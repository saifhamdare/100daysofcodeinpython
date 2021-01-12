#computer choosing a no.
import random
from art import logo1
from art import gameover
from art import win
number =  random.randint(1,101)
print(logo1)
should_continue= False
easy=10
hard=5


def difficulty():
  option=input("choose difficulty easy or hard")
  if option=="easy":
    attempt=easy
  elif option=="hard":
    attempt=hard
  else:
    print("invalid entry try again")
  return attempt
#selecting a easy hard Mode.
attempt=difficulty()
while not should_continue:
  #accepting a no by User.50

  if attempt==0:
    print(number)
    print(gameover)
    break

  guess=int(input("enter your guess"))
  
  if guess>100 or guess<0:
    print("invalid entry")
    print(f"{attempt} attempt left")
  else:
  #compare guessed no with compile
    attempt=attempt-1
    print(f"{attempt} attempt left")
    if guess == number:
      print("you guessed it right")
      print(win)
      break
    elif guess> number:
      print("too high")
      print("guess again")
      
    elif guess<number:
      print ("too low")
      print("guess again")
    
