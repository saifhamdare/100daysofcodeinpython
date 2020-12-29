print("welcome to the roller coster ride")
height=int(input("enter your height in cm: "))

bill =0
if (height>=120):
  print("you are eligiable for the ride")
  age=int(input("enter your age: "))
  if(age<12):
    bill=5
    print("your ticket cost is $5 for ride")
  elif(age<=18):
    bill=7
    print("your ticket cost is $7 for ride")
  else:
    bill=12
    print("your ticket cost is $12 for ride")
  photo=input("Do you like to have a photo of it ? Y or N: ")
  if photo=="Y":
    bill+=3
  print(f"your final bill is {bill} ")
else:
  print("sorry! you are not eligiable for the ride")
print("next!!")