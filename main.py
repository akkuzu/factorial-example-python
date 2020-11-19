
'''

Functions are blocks of code that can be used over and over again to perform a specific action.

As we know, in Python, there are print (), len () etc. Many available functions are defined.

We can use it in our own code by providing access to functions defined in libraries, modules and packages.
These are called predefined functions, embedded functions (built-in) or library functions.
We can use ready-made functions as well as create our own functions. (User-defined)

Functions prevent code repetition and our code stays more modular and organized.


def "function_name"(parameter1,parameter2,..):

"Do something"

return "return something" (depends on functionality)

'''

def hello():
    print("Hello Everyone")

def hello(name):
    print("Hello " + name)

hello("Ipek")

def func_in_func(name1):
    return hello(name1)
func_in_func("Ipek")

def func1():
    print("Hello World!")

def summ (a,b):
    summ=a+b
    print(summ)

summ(6.0,7.5)
print(summ)


def func(x):
  if x > 0:
    return ("Positive")
  elif x < 0:
    return ("Negative")
  else:
    return ("Zero")

for i in [-2,5,6,0,-4,-7]:
  print(func(i))

def factorial(num):
  factorial = 1
  if (num == 0 or num == 1):
    print("Factorial: ", factorial)
  else:
    while (num >= 1):
      factorial = factorial * num
      num -= 1
    print("Factorial: ", factorial)

print(factorial(5))

#using for loop

def factorial2(num2):
  factorial2 = 1
  if (num2 == 0 or num2 == 1):
    print("Factorial: ", factorial2)
  else:
    for i in range(factorial2, num2+1):
        factorial2 *= i
    print("Factorial: ", factorial2)

def factorial3(nums):
  factorial3 = 1
  if (nums == 0 or nums == 1):
    return ("Factorial: ", factorial3)
  else:
    for i in range(factorial3, nums+1):
       factorial3 *= i
    return (factorial3)

def hello2(name, capLetter = False):
  if capLetter:
    print("Hello " + name.upper())
  else:
    print("Hello " + name)

hello2("Ipek")

'''
Let's write a function that returns a random word from a list.
Modules
import numpy

import tensorflow as tf

import myModules

myModules.myFunc()

from myModules import *

myFunc()
'''

'''
Methods
Functions are called by name, it can take parameters inside and optionally the resulting value can be used outside of the function.

Methods are also called by name, in many ways they are like functions, but calling is performed through an object such as a String or list.

object.methodName(parameter)
'''

