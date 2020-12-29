year=int(input("enter the year to check wheather it is a leap year or not: "))
if(0==year%4):
  print("year {year} is a leap year")
elif(0!=year%100):
  print("year {year} is a leap year")
elif(0==year%400):
  print("year {year} is a leap year")
else:
  print("year {year} is not leap year")
