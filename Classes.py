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
