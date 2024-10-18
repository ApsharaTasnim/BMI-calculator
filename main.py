height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in cm:"))

BMI=weight/(height/100)**2

print("Your BMI is:")

if BMI<=18.4:
    print("You are under weight")
elif BMI<=24.5:
   print("You have perfect BMI")
elif BMI<=29.5:
   print("You are overweight")
elif BMI<=34.9:
   print("You are severly overweight")
elif BMI<=39.9:
   print("You are obese")
else:

   print("You are severly obese.")


