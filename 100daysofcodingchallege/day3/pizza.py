print(">>>>>>>>>>>>>>>>welcome<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>>>>>>to<<<<<<<<<<<<<<<<<<<")
print(">>>>>>>>>>>>>pizza station<<<<<<<<<<<<<")
import time
print("--------------->Welcome<---------------")
print("------------------>To<-----------------")
print("------------->Pizza Station<------------\n")

price=0
size=input("what size of pizza would you like to have\n S for Small M for Medium L for Large: ")
if size == "S":
  size = 15
elif size=="M":
  size =20
elif size=="L":
  size=25
else:
  print("invalid entry try again!!")
pepperoni=input("Want Extra pepperoni ? Y or N : ")
if pepperoni=="Y":
  if size== 15:
    pepperoni= 2
  elif size>=15:
    pepperoni=3
  price =size+pepperoni
else:
 price+=0
cheese=input("Do you want extra cheese ? Y or N : ")
if cheese== "Y":
  price= size
else:
  price= size
print(f"your bill will be ${price}")
confirm=input("confirm your Order Y for Yes N for No: ")
if confirm=="Y":
  print("excellent choice wait for 30 minutes")
  time.sleep(1.0)
  print("have a good day!!")
  time.sleep(1.0)
  print('enjoy Your Pizza')
else:
  print("try again")