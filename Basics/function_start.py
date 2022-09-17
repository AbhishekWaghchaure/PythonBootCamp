def fun():
    print("i am a function")
    
# fun()
# print(fun())
# print(fun)

#function with parameters
def func2(arg1, arg2):
    print(arg1,"", arg2)
    
func2(1,2)

def cube(x):
    return x*x*x

print(cube(3))

def multiAdd(*args):
    x=0
    for y in args :
        x = x + y
    return x
print(multiAdd(3,5,2,1))