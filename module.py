# Example python module that contains two classes

class math:
    # Class varibles are common for all the instances of class
    # They can be refrenced inside class methods if self is passed
    name = "Math class"
    operation = "Basic addition, subtraction, multiplication and division"

    # A method has the first argument (self) as the object to which it is bound.
    # Python automatically passes the bound object to the method as the first argument. By convention, its name is self.

    # Class methods (self is passed)
    def describe(self):
        print("This class is named : ", self.name)
        print("It performs : {}".format(self.operation))

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    # Static methods : (self is not passed) are not bound to class objects
    # it means that they cannot access or change object's state
    # static method example
    @staticmethod
    def add(a, b):
        add = a + b
        return add

    @staticmethod
    def sub(a, b):
        sub = a - b
        return sub



class employee:
    # __init__ is used to initialize private attributes/variables when creating an instance from class
    # These attributes are specific to the object and cannot be used across class objects
    # To initialize the class object >> employee(name, age) will be used
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def weekly_salary(self, hourly_salary, hours_worked):
        weekly_sal = hourly_salary * hours_worked
        print("Employee {} is {} years old. \n His weekly salary is : {}".format(self.name, self.age, weekly_sal))
