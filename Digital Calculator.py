''' Name: Gatmach Yuol Nyuon
# Registration No: SCT211-0504/2021   
'''
print("Sum Calculator")
name = input("What is your name?\n")
print("Welcome to",name,"Electronic Calculator...")

num1 =int(input("Please enter the first  digit : "))
num2 = int(input("Please enter the second  digit : "))
sum = num1 + num2
print("Sum = ",sum)
yearOfBirth = int(input("Enter the year you were born:"))
monthOfBirth = str(input("Enter the month you were born:"))
dateOfBirth=int(input("Enter the date you were born: "))
age = int(2023- yearOfBirth)
ageInMonth = age * 12
ageInDay = age *12 * 365
print("Age: ", age)
print("AgeInMonth: ", ageInMonth)
print("ageInDay: ", ageInDay)
print("I was born on", dateOfBirth,"/", monthOfBirth ,"/",yearOfBirth,".")

def calculateTheBill(total_bill, tip_percentage, num_people):
    tip = total_bill * (tip_percentage / 100)
    totalTip = total_bill + tip
    amountPerPerson =  totalTip  / num_people
    return amountPerPerson

total_bill = float(input("Enter the total bill amount: "))

while True:
    tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
    if tip_percentage in [10, 12, 15]:
        break
    else:
        print("Invalid input. Please choose 10, 12, or 15.")

num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the amount each person should pay
amount_per_person = calculateTheBill(total_bill, tip_percentage, num_people)

# Display the result rounded to two decimal points
print(f"Each person should pay: ${amount_per_person:.2f}")

