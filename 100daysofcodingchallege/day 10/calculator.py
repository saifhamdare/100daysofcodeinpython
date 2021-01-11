#Calculator
from art import logo

#add 
def add(n1,n2):
  return n1+n2

#subtract
def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  num1= float(input("1st number= "))
  for signs in operations:
    print(signs)
  should_continue =True
  while should_continue:
    operation_sign= input("Pick an operation ")
    calculation_function= operations[operation_sign]
    num2= float(input("Next number= "))
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation_sign} {num2} = {answer}" )
    if input("do you want to continue type Y or N"):
      num1=answer
    else:
      should_continue=False
      calculator()
    
calculator()