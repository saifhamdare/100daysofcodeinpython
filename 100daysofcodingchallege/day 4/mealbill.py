import random
random.seed(test)

namesCSV=input("give me everyone's name, seperatrted by comma")
names=namesCSV.split(", ")
print(names)import random
test=int(input("create a seed number"))
random.seed(test)

namesCSV=input("give me everyone's name seperatrted by comma")
names=namesCSV.split(", ")
x=len(names)
no=random.randint(0,x-1)

print(names[no]+" is going to pay the bill")
#saif, saad, naved, aaris