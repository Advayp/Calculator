import math
import random

intial_input = input("Enter the operation you want to do (add, subtract, multiply, divide, exponentation, trigonometry): ")
number_of_numbers = -1
subtractNums = -1
if (intial_input.lower()).strip() == 'add':
    while number_of_numbers < 2:
        number_of_numbers = int(input("How many numbers would you like to add together? "))
    
    sum = 0
    for i in range(number_of_numbers):
        placeNum = int(input("Enter the number you want to add to this list (This is number " + str(i + 1) + "): "))
        sum += placeNum
    print("The sum of your number(s) is " + str(sum))
if (intial_input.lower()).strip() == 'subtract':
    while subtractNums < 2:
        subtractNums = int(input("How many number(s) would you like to subtract? "))
    differnce = 0
    difCalc = 0
    placeDif = int(input("Enter the number you want to subtract " + str(subtractNums - 1) + " number(s) from: "))

    for i in range(subtractNums - 1):
        placeDif2 = int(input("Enter the number(s) you want to subtract from " + str(placeDif) + ": "))
        difCalc += placeDif2
    differnce = placeDif - difCalc    
    print("The final difference is " + str(differnce) + ".")