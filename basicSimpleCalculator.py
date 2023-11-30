# Gatmach Yuol Nyuon
# SCT211-0504/2021
class Calculator:
    def __init__(self):
        self.number1 = None
        self.number2 = None
        # assert number1 >=f"the number1 is {number1} less than or equal to zero."
        # assert number2 >=f"the number1 is {number2} less than or equal to zero."
    def get_integer_value(self):
        try:
            self.number1 = int(input("enter first number:"))
            self.number2 = int(input("enter second number:"))
        except ValueError as e:
            print ("pleae enter valid integer value!")
            self.get_integer_value()
            
    def add_two_numbers(self):
        print(f'{self.number1 + self.number2}')
    def subtract_two_numbers(self):
        self.total = self.number1 - self.number2
        return self.total
    def divide_two_numbers(self):
        try:
            self.total = self.number1 / self.number2
            return self.total
        except ZeroDivisionError as ae:
            print('Division error')

    def multiply_two_numbers(self):
        self.total = self.number1 * self.number2
        return self.total
    def modulo_two_numbers(self):
        self.total = self.number1 % self.number2
        return self.total

    # passNone


calculator1=Calculator()
calculator1.get_integer_value()
calculator1.add_two_numbers()
# print(calculator1.add_two_numbers())
print(calculator1.subtract_two_numbers())
print(calculator1.divide_two_numbers())
print(calculator1.multiply_two_numbers())
print(calculator1.modulo_two_numbers())






