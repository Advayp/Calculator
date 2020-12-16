import math
import random

intial_input = input("Enter the operation you want to do (add, subtract, multiply, divide, exponent, trig): ")
addNums = -1
subtractNums = -1
multiNums = -1
divideNums = -1

# Checks if the user typed in add
# The.lower() function converts all characters in the string to lowercase
# The .strip() function removes the spaces from the end and beginning from the string.
# Eg: " HELLO " --> "hello". This transformation happens after the .lower() and .strip() functions
if (intial_input.lower()).strip() == 'add':

    # This while loop make sures the user types in a valid input
    while addNums < 2:
        addNums = int(input("How many numbers would you like to add together? "))

    # This line intializes a variable called sum and sets it to 0
    sum = 0

    # This for loop runs a certain number of times (Specifically: addNums number of times. See line 17)
    for i in range(addNums):

        #This line takes an input from the user
        placeNum = int(input("Enter the number you want to add to this list (This is number " + str(i + 1) + "): "))

        # This line adds the input from the user to the variable sum
        sum += placeNum
    
    #This line outputs the sum of the numbers the user typed in.
    print("The sum of your number(s) is " + str(sum))

# Checks if user typed in 'subtract'
# Uses same .lower() and .strip() functions
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


if (intial_input.lower()).strip() == 'multiply':
    while multiNums < 2:
        multiNums = int(input("How many numbers would you like to multiply together? "))
    firstMultnum = int(input("Enter the number you want to multiply " + str(multiNums) + " number(s) by: "))
    product = 1

    for i in range(multiNums):
        multiBy = int(input("Enter the number(s) you want to multiply " + str(firstMultnum) + " by: "))
        product *= multiBy
    print("The product is " + str(product) + '.')


if (intial_input.lower()).strip() == 'divide':
    while divideNums < 2:
        divideNums = int(input("How many numbers do you want to divide? "))
    quotient = int(input("Enter the dividend: "))
    