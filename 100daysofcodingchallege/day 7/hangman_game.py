import random
from replit import clear
from hangman_art import logo
end_of_game=False
word_list= ["captainamerica","ironman","thor","blackpanther","spiderman","hulk","bucky","doctorstrange","blackwidow","antman"]

choosen_word=random.choice(word_list)
lives=6
from hangman_art import logo,stages,gameover
print(logo)
display=[]
for letter in range(len(choosen_word)):
  display += "_"
while not end_of_game:
  guess= input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed the {guess}")
    clear()
  for position in range(len(choosen_word)):
    letter = choosen_word[position]
    #print(f"Current position: {position}\n Currentletter: {letter} \n Guessed letter :{guess}")
    if letter == guess:
      display[position]=letter
  if guess not in choosen_word:
    print(f"You guessed {guess}, that's not in the word.You loose a life")
    lives-=1
    if lives==0:
      end_of_game=True
      print("You Lose.")
      print(gameover)
  print(f" {' '.join(display)}")

  if "_" not in display:
    end_of_game=True
    print("You Win.")
    print(gameover)
  print(stages[lives])
