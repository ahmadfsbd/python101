# Example python module that contains a class

class math:
    # Class varibles
    name = "Math class"
    operation = "Basic addition, subtraction, multiplication and division"


    # Static methods (self is not passed)
    @staticmethod 
    def add(a, b):
        add = a + b
        return add
    
    @staticmethod
    def sub(a, b):
        sub = a - b
        return sub

    # Class methods (self is passed)
    def describe(self):
        print("This class is named : ", self.name)
        print("It performs : {}".format(self.operation))

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def weekly_salary(self, hourly_salary, hours_worked):
        weekly_sal = hourly_salary * hours_worked
        print("Employee {} is {} years old. \n His weekly salary is : {}".format(self.name, self.age, weekly_sal))

