# 🚨 Don't change the code below 👇
print("welcome to tip calculator")
bill = input("enter bill amount: ")
bill=float(bill)
# 🚨 Don't change the code above 👆
tip=input("enter the amount you want to tip 10 12 15: ")
tip=int(tip)
people=input("enter the no of people need to split in: ")
people=int(people)
####################################
#Write your code below this line 👇
tip=tip/100
tbill=bill*tip
bill=tbill+bill
lastbill=bill/people
lastbill=round(lastbill,2)
print(lastbill)
