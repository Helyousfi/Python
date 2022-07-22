# Decorators : add new functionality to an existing 
# object without modifying its structure.

def logged(function):
    def wrapper(*args, **kwargs):
        fun_name = function.__name__
        ret = function(*args, **kwargs)
        with open("logs.txt", "a+") as f:
            f.write(f"{fun_name} returned {ret} \n")
            print(f"{fun_name} returned {ret} \n")
    return wrapper

@logged
def printFull(fname, lname):
    return fname + " " + lname

@logged
def add(a, b):
    return a + b

add(3, 5)
printFull("Ham", "You")
"""
def myDecorator(fun):
    def wrapper():
        print("Wrapper called")
        fun()
    return wrapper

@myDecorator
def function():
    print("hello world")    

function()
"""