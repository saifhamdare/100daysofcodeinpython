name1=input("enter your name 1: ")
name2=input("enter your name 2: ")
name1=name1.lower()
name2=name2.lower()
name=name1+name2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=l+o+v+e
print(f"{true}{love}")name1=input("enter your name 1: ")
name2=input("enter your name 2: ")

name=name1+name2
name=name.lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=l+o+v+e
true *=10
tl=true+love
if tl<10 or tl>90:
  print(f"your love score is {tl}, you go together like coke and mentos")
elif tl>40 and tl<50:
  print(f"your score is {tl}, you are alright together")
else:
  print(f"your score is {tl}")
