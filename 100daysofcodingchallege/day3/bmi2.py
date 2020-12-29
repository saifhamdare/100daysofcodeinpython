print("**welcome to the BMI calculator**\n")  
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
h=float(height)
w=float(weight)
bmi=w/(h*h)
bmi=float(bmi)
if(bmi<18.5):
  print(f"your BMI is{bmi}you are under weight")
elif(bmi>18.5):
  print(f"your BMI is{bmi}you have a normal weight")
elif(bmi>25):
  print(f"your BMI is{bmi}you are over weight")
elif(bmi>30):
  print(f"your BMI is{bmi}you are obese ")
elif(bmi>35):
  print(f"your BMI is{bmi}you are clinically obese")
else:
  print("print a valid details")