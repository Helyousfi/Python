
import math
import argparse

parser = argparse.ArgumentParser(description = 'Calculate volume of a cylinder')
parser.add_argument('--radius', '--r', type = int, required = True, help = "Radius of the cylinder")
parser.add_argument('--height', '--ht', type = int, required = True, help = "Height of the cylinder")
parser.add_argument('--fibNum', '--fib', type = int, required = True, help = "Fibonacci number")
args = parser.parse_args()

def cylinder_volume(radius, height):
    volume = (math.pi * radius**2) * height
    return volume

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    print(f"the cylinder volume is : {cylinder_volume(args.radius,args.height)}")
    result = fib(args.fibNum)
    print(f"the {args.fibNum}th fibonacci number is {result}")
