import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#implement main function to print welcome message




def main():
    print("Welcome to my calculator")
    print("This calculator can perform basic mathematical operations")
    print("Please enter your first number")
    a = int(input())
    print("Please enter your second number")
    b = int(input())
    print("Please enter your operation")
    operation = input()
    if operation == "+":
        print(add(a,b))
        
    elif operation == "-":
        print(subtract(a,b))
        
    elif operation == "*":
        print(multiply(a,b))
        
    elif operation == "/":
        print(divide(a,b))
        
    else:
        print("Invalid operation")

        
# implement function multiply to multiply two numbers
print (multiply(3,3))
def multiply(a,b):
    return a*b

# write a testcase for multiply function

def test_multiply():
    assert (multiply(3, 3) == 9)
    assert (multiply(3, 4) == 13)





# implement function divide to divide two numbers

def divide(a,b):
    return a/b


# implement function add to add two numbers

def add(a,b):
    return a+b
    
# implement function subtract to subtract two numbers

def subtract(a,b):
    return a-b


