# Imports a module called math which has many interesting functions
# relating to trigonometry, pi, and calculus
import math

# Assigns initial input to a random value so that the while loop on line 9
# can run
initial_input = 'asdfasdf'

# Initializes a list which has the acceptable functions of this calculator
acceptedValues = ['add', 'subtract', 'multiply', 'divide', 'trig', 'exponent'] 

# This while loop runs if the initial_input is not in acceptedValues.
# Explanation of.lower() and .strip() functions on the first if statement in this calculator.
while  not (initial_input.lower()).strip() in acceptedValues:

    # Prompts the user for the function they want to enter
    initial_input = input("Enter the operation you want to do (add, subtract, multiply, divide, exponent, trig): ")

# Initializes 4 variables to a random value so that a while loop can run
addNums = -1

subtractNums = -1

multiNums = -1

divideNums = -1
# Checks if the user typed in add
# The.lower() function converts all characters in the string to lowercase
# The .strip() function removes the spaces from the end and beginning from the string.
# Eg: " HELLO " --> "hello". This transformation happens after the .lower() and .strip() functions
if (initial_input.lower()).strip() == 'add':

    # This while loop make sures the user types in a valid input
    while addNums < 2:
        # This line prompts the user for input
        addNums = float(input("How many numbers would you like to add together? "))

    # This line intializes a variable called sum and sets it to 0
    sum = 0

    # This for-loop runs a certain number of times (Specifically: addNums number of times. See line 17)
    for i in range(addNums):

        #This line takes an input from the user
        placeNum = float(input("Enter the number you want to add to this list (This is number " + str(i + 1) + "): "))

        # This line adds the input from the user to the variable sum
        sum += placeNum
    
    #This line outputs the sum of the numbers the user typed in.
    print("The sum of your number(s) is " + str(sum))

# Checks if user typed in 'subtract'
# Uses same .lower() and .strip() functions
if (initial_input.lower()).strip() == 'subtract':

    #{
    # The lines of code below make sure that the
    # number the user types in is valid for subtraction
    # }
    while subtractNums < 2:
        # This line of code prompts the user for input
        subtractNums = float(input("How many number(s) would you like to subtract? "))
    
    # Intializes a variable called 'difference' and sets it to 0
    differnce = 0

    # Intializes a variable called 'difCalc' and sets it to 0
    difCalc = 0

    # Prompts the user for input.
    placeDif = float(input("Enter the number you want to subtract " + str(subtractNums - 1) + " number(s) from: "))

    # This for-loop runs 'subtractNums - 1' number of times.
    for i in range(subtractNums - 1):
        
        # Prompts the user for an integer that they want to subtract from 'placeDif'
        placeDif2 = float(input("Enter the number(s) you want to subtract from " + str(placeDif) + ": "))

        # Adds the number the user entered for the previous prompt to a variable called 'difCalc'
        difCalc += placeDif2
    
    #{
    #  Takes the first number the user entered(placeDif) and subtracts the sum of
    #  the numbers the user entered in the for-loop (difCalc)
    # } 
    differnce = placeDif - difCalc   

    # Output 
    print("The final difference is " + str(differnce) + ".")


if (initial_input.lower()).strip() == 'multiply':
    while multiNums < 2:
        multiNums = float(input("How many numbers would you like to multiply together? "))
    firstMultnum = float(input("Enter the number you want to multiply " + str(multiNums) + " number(s) by: "))
    product = 1

    for i in range(multiNums - 1):
        multiBy = float(input("Enter the number(s) you want to multiply " + str(firstMultnum) + " by: "))
        product *= multiBy
    print("The product is " + str(product) + '.')


if (initial_input.lower()).strip() == 'divide':
    while divideNums < 2:
        divideNums = float(input("How many numbers do you want to divide? "))
    quotient = float(input("Enter the dividend: "))

    for i in range(divideNums - 1):
        divisor = float(input("Enter divisor #" + str(i + 1) + ": "))
        quotient /= divisor
    print('The quotient is ' + str(quotient) + ".")


if (initial_input.lower()).strip() == 'exponent':
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    finalExpo = base ** exponent
    print("The answer is " + str(finalExpo) + '.')

if (initial_input.lower()).strip() == 'trig':
    trigPrompt = input("Enter the trig function you want to use (sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, arctanh): ")
    acceptedTrig = ['sin', 'cos', 'tan']
    if (trigPrompt.lower()).strip() in acceptedTrig:
        angle1 = float(input("Enter the angle you want to find the sin, cos, or tan (degrees): "))
        angleInfo = math.radians(angle1)

        print("The sine of " + str(round(angle1)) + " = " + str(round(math.sin(angleInfo), 3)) + '.')
        print("The cosine of " + str(round(angle1)) + " = " + str(round(math.cos(angleInfo), 3)) + '.')
        print("The tangent of " + str(round(angle1)) + " = " + str(round(math.tan(angleInfo), 3)) + '.')


