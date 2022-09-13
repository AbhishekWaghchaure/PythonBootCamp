# class myClass():
#     def method1(self):
#         print("myClass method1")
#
#     def method2(self, someString):
#         print("myClass method2" + someString)
#
#
# def main():
#     c = myClass()
#     c.method1()
#     c.method2("Jay bhavani")

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def function(self):
        print("Hello my name is " + self.name)


p1 = Person("Slim shady", 23)
p1.function()
print(p1.age)

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)

x = Person("Abhishek", "Waghchaure")
x.printName()

# class Student(Person):
#     pass
#     def printRandom(self):
#         print("in random method of child class")
#
# s = Student("xyz","abc")
# s.printName()
# s.printRandom()

class Student(Person):
    def __init__(self, firstName, lastName, domain, year):
        Person.__init__(self, firstName, lastName)
        self.domain = domain
        self.year = year

    def print(self):
        print(self.firstName,self.lastName, self.domain, self.year)

s = Student("Ram", "krishna", "DSA", "2022")
s.print()
