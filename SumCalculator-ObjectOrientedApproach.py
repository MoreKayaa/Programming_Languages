#Favian Mokaya Imbera SCT211-0022/2021

#Enter your name,first number and second number

class Person:
#Person class with an initializer, a method to calculate the sum of two numbers, and a method to greet the person
    def __init__(self, name, num1, num2):
        self.name = name
        self.num1 = num1
        self.num2 = num2

    def calculate_sum(self):
        sum = self.num1 + self.num2
        return sum

    def greet(self):
        print(f"Hello, {self.name}.The sum of {self.num1} and {self.num2} is {self.calculate_sum()}")


#Enter your name and two numbers
name = str(input())
num1 = int(input())
num2 = int(input())

person = Person(name, num1, num2)
person.greet()
#This greet method prints a greeting message that includes the person's name and the sum of the two numbers.
