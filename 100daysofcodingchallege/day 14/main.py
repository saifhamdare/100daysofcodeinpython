#modules calls
import random
from replit import clear
from art import vs,logo
from game_data import data
score_bar=0
should_continue= False
account_b=random.choice(data)
def formate_data(account):
    account_name=account["name"]
    account_des=account["description"]
    account_country=account["country"]
    return(f"{account_name} a {account_des} from {account_country}")
def check_result(guess , a_followers,b_followers):
    if a_followers> b_followers:
        return guess=="A"
    else:
        return guess=="B"

#repetative while block

#logo
print(logo)
should_continue=True
while should_continue:
#score bar a
    account_a=account_b
    account_b=random.choice(data)
    if account_a== account_b:
        account_b=random.choice(data)
    #value call one
    print(F"Compare A: {formate_data(account_a)}")
    #vs
    print(vs)
    #valur call two
    print(F"Against B: {formate_data(account_b)}")
    guess=input("who has more followers? Type 'A' or 'B': ").upper()
    a_followers_count=account_a["follower_count"]
    b_followers_count=account_b["follower_count"]
    is_correct=check_result(guess, a_followers_count, b_followers_count)
    clear()
    print(logo)
    if is_correct:
        score_bar+=1
        print(f"You are Right! Current Score {score_bar}")
    else:
        should_continue=False
        print(f"Sorry! You are Wrong.Final Score {score_bar}")

#if correct incease score by 1

#else game over show final score and 


# exit