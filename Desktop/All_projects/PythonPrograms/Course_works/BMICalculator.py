'''
As the name suggests, this program  calculates the Body Mass Index (BMI) for an user
It prompts the user to enter their weight( Kg) and heights(meters.
After the user has entered the required fields, the program calculates Body Mass Index (BMI).
It determines which Body Mass Index category you are following in.
'''

print("** Body Mass Index (BMI) calculator **")
weights = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))
BMI = (weights / (height * height))
       
if BMI < 18.5:
    print("You're underweight")
elif BMI >= 25:
    print("You're overweight")
else:   
    print("You've a normal weight.")
print("Your Body Mass Index: ",round(BMI,2))

'''
A program that checked if a year is a leap year or not...
Example: 1998 % 4 == 
'''
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
  print("Wow! That's leap year!")
else:
  print("Ohh no, it is not a leap year!")
