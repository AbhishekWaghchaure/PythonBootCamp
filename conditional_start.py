# def main():
#     # x = 1000
#     # y = 100
#     x,y = 1000,100
#
#     #conditional flow uses if, elif, else
#     if (x < y):
#         st = "x is less than y"
#     elif (x == y):
#         st = "x is equal to y"
#     else:
#         st = "x is greater than y"
#
#     print(st)
#
#     st = "x is less than y" if (x,y) else "x is greater or same as y"
#     print(st)

age = input("enter your age")
mage =int(age)

if mage >= 18:
    print("You are an adult")
    print("you can vote")
elif mage < 18 and mage >3:
    print("you are in school")
else:
    print("you are kid")
print("ThankYou")