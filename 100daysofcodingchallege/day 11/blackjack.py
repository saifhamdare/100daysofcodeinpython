import random
from replit import clear
from art import logo
def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "Lose,opponent has Blackjack"
  elif user_score==0:
    return "win with a BlackJack"
  elif user_score>21:
    return "You went over. You Lose"
  elif computer_score>21:
    return "opponent went over. You win"
  elif user_score> computer_score:
    return "You win."
  else:
    return "You Lose."
def playgame():
  print(logo)
  user_cards = []
  computer_cards = []
  is_gameover=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_gameover:
    def calculate_score(card):
      if sum(card)==21 and len(card)==2:
        return 0 
      if 11 in card and sum(card)> 21:
        card.remove(11)
        card.append(1)
      return sum(card)
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards} current_score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]} ")

    if user_score==0 or computer_score==0 or user_score>21:
      is_gameover= True
    else: 
      user_should_deal=input("type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal=="y":
        user_cards.append(deal_card()) 
      else:
        is_gameover=True
  while computer_score != 0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(f" Your final hand: {user_cards}, Final score: {user_score} ")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play a gamme of Blackjack? Type y or n: ")=="y":
   clear()
   playgame()