''' Name : Gatmach Yuol Nyuon
# Reg No: SCT211-0504/2021
'''

print(" BMI Calculator: ")
weights = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))
BMI = (weights / (height * height))
       
if BMI < 18.5:
    print("you are underweight")
elif BMI >= 25:
    print("you are overweight")
else:   
    print("you have normal weight.")

BMI = (weights /(height * height))
#print("Your weight is ",weights," and your height is ",height)
print("your BMI is ",round(BMI,2))

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
  print("The year is a leap year!")
else:
  print("The year is not a leap year!")
