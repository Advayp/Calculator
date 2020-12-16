import math
import random

intial_input = input("Enter the operation you want to do (add, subtract, multiply, divide, exponentation, trigonometry): ")
number_of_numbers = -1
if intial_input.lower() == 'add':
    while number_of_numbers < 2:
        number_of_numbers = int(input("How many numbers would you like to add together? "))
    
    sum = 0
    for i in range(number_of_numbers):
        placeNum = int(input("Enter the number you want to add to this list (This is number " + str(i + 1) + "): "))
        sum += placeNum
    print("The sum of your number(s) is " + str(sum))
elif intial_input.lower == 'subtract':
    subtractNums = int(input("How many number would you like to subtract? "))