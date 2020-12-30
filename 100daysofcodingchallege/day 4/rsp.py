import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option=[rock,paper,scissors]
player=int(input("choose your option 0 for rock 1 for paper 2 for scissors\n"))
if player>=3 or player<0:
  print("invalid entry try again")
else:
  print(option[player])

  cpu=random.randint(0,2)
  print("computer choose:")
  print(option[cpu])
  if player> 3 or player<0:
    print("invalid entry try again")
  elif player==0 and cpu==2:
    print("you win")
  elif player==2 and cpu==0:
    print("you loose")
  elif cpu>player:
    print("you lose")
  elif cpu<player:
    print("you win")
  elif cpu==player:
    print("it's a draw")

