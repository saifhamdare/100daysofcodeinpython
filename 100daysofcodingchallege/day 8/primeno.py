#Write your code below this line 👇
def prime_checker(number):
  if number%2==0 and number%3==0:
    print(f"{number} is not a prime no")
  else:
    print(f"{number} is a prime no")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



