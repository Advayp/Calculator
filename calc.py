# Imports a module called math which has many interesting functions
# relating to trigonometry, pi, and calculus
import math

# Imports a module called cmath which has multiple functions
# relating to complex numbers
import cmath
#! Important info: the "*" tag on a comment summarizes the job of the line below it
#! The "?" tag answers some questions people might have about the code


# *Assigns initial input to a random value so that a while loop
# *can run
initial_input = 'asdfasdf'

# *Initializes a list which has the acceptable functions of this calculator
acceptedValues = ['add', 'subtract', 'multiply',
                  'divide', 'trig', 'exponent', 'log', 'complex', 'permutation', 'combination', 'factorial']

# *This while loop runs if the initial_input is not in acceptedValues.
# ?Explanation of.lower() and .strip() functions on the first if statement in this calculator.
while not (initial_input.lower()).strip() in acceptedValues:

    # ?Prompts the user for the function they want to enter
    initial_input = input(
        "Enter the operation you want to do (add, subtract, multiply, divide, exponent, trig, log, complex, permutation, combination, factorial): ")

# ?Initializes 4 variables to a random value so that a while loop can run
addNums = -1

subtractNums = -1

multiNums = -1

divideNums = -1
# *Checks if the user typed in add
# ?The.lower() function converts all characters in the string to lowercase
# ?The .strip() function removes the spaces from the end and beginning from the string.
# ?Eg: " HELLO " --> "hello". This transformation happens after the .lower() and .strip() functions
if (initial_input.lower()).strip() == 'add':

    # This while loop make sures the user types in a valid input
    while addNums < 2:
        # This line prompts the user for input
        addNums = int(
            input("How many numbers would you like to add together? "))

    # This line intializes a variable called sum and sets it to 0
    sum = 0

    # This for-loop runs a certain number of times (Specifically: addNums number of times. See line 17)
    for i in range(addNums):

        # This line takes an input from the user
        placeNum = float(input(
            "Enter the number you want to add to this list (This is number " + str(i + 1) + "): "))

        # This line adds the input from the user to the variable sum
        sum += placeNum

    # This line outputs the sum of the numbers the user typed in.
    print("The sum of your number(s) is " + str(sum))

# Checks if user typed in 'subtract'
# Uses same .lower() and .strip() functions
elif (initial_input.lower()).strip() == 'subtract':

    # {
    # *The lines of code below make sure that the
    # *number the user types in is valid for subtraction
    # }
    while subtractNums < 2:
        # *This line of code prompts the user for input
        subtractNums = int(
            input("How many number(s) would you like to subtract? "))

    # *Intializes a variable called 'difference' and sets it to 0
    differnce = 0

    # *Intializes a variable called 'difCalc' and sets it to 0
    difCalc = 0

    # *Prompts the user for input.
    placeDif = float(input("Enter the number you want to subtract " +
                           str(subtractNums - 1) + " number(s) from: "))

    # *This for-loop runs 'subtractNums - 1' number of times.
    for i in range(subtractNums - 1):

        # *Prompts the user for an integer that they want to subtract from 'placeDif'
        placeDif2 = float(
            input("Enter the number(s) you want to subtract from " + str(placeDif) + ": "))

        # *Adds the number the user entered for the previous prompt to a variable called 'difCalc'
        difCalc += placeDif2

    # {
    #  *Takes the first number the user entered(placeDif) and subtracts the sum of
    #  *the numbers the user entered in the for-loop (difCalc)
    # }
    differnce = placeDif - difCalc

    # *Output
    print("The final difference is " + str(differnce) + ".")


elif (initial_input.lower()).strip() == 'multiply':
    while multiNums < 2:
        multiNums = int(
            input("How many numbers would you like to multiply together? "))

    firstMultnum = float(input(
        "Enter the number you want to multiply " + str(multiNums) + " number(s) by: "))

    product = 1

    for i in range(multiNums - 1):

        multiBy = float(
            input("Enter the number(s) you want to multiply " + str(firstMultnum) + " by: "))

        product *= multiBy

    print("The product is " + str(product) + '.')


elif (initial_input.lower()).strip() == 'divide':
    while divideNums < 2:
        divideNums = int(input("How many numbers do you want to divide? "))

    quotient = float(input("Enter the dividend: "))

    for i in range(divideNums - 1):

        divisor = float(input("Enter divisor #" + str(i + 1) + ": "))

        quotient /= divisor

    print('The quotient is ' + str(quotient) + ".")


elif (initial_input.lower()).strip() == 'exponent':

    base = float(input("Enter the base: "))

    exponent = float(input("Enter the exponent: "))

    finalExpo = base ** exponent

    print("The answer is " + str(finalExpo) + '.')

elif (initial_input.lower()).strip() == 'trig':
    trigPrompt = input(
        "Enter the trig function you want to use (sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, arctanh): ")

    acceptedTrig = ['sin', 'cos', 'tan']

    acceptedTrigh = ['sinh', 'cosh', 'tanh']

    acceptedArcTrig = ['arcsin', 'arccos', 'arctan']

    acceptedArcTrigHyp = ['arcsinh', 'arccosh', 'arctanh']

    if (trigPrompt.lower()).strip() in acceptedTrig:
        angle1 = float(
            input("Enter the angle you want to find the sin, cos, or tan of (degrees): "))
        angleInfo = math.radians(angle1)

        print("The sine of " + str(round(angle1)) + " ~= " + str(round(
            math.sin(angleInfo), 3)) + '.')

        print("The cosine of " + str(round(angle1)) + " ~= " + str(round(
            math.cos(angleInfo), 3)) + '.')

        print("The tangent of " + str(round(angle1)) + " ~= " + str(round(
            math.tan(angleInfo), 3)) + '.')

    elif (trigPrompt.lower()).strip() in acceptedTrigh:
        angleHyp = float(
            input('Enter the angle you want to find the sinh, cosh, or tanh of (degrees): '))

        angleHyp_info = math.radians(angleHyp)

        print('The sinh of ' + str(round(angleHyp)) + ' ~= ' + str(round(
            math.sinh(angleHyp_info), 3
        )) + '.')

        print('The cosh of ' + str(round(angleHyp)) + ' ~= ' + str(round(
            math.cosh(angleHyp_info), 3
        )) + '.')

        print('The tanh of ' + str(round(angleHyp)) + ' ~= ' + str(round(
            math.tanh(angleHyp_info), 3
        )) + '.')

    elif (trigPrompt.lower()).strip() in acceptedArcTrig:
        ratioNorm = float(
            input("Enter the ratio (In decimal form) you want to get the arcsin, arccos, or arctan of: "))

        arctanNorm = 1

        if ratioNorm >= -1 and ratioNorm <= 1:

            arcsineNorm = math.degrees(math.asin(ratioNorm))

            arccosNorm = math.degrees(math.acos(ratioNorm))

            arctanNorm = math.degrees(math.atan(ratioNorm))

            print('The arcsine of ' + str(ratioNorm) +
                  ' is ' + str(arcsineNorm) + ' degrees')

            print('The arccosine of ' + str(ratioNorm) +
                  ' is ' + str(arccosNorm) + ' degrees.')

            print('The arctan of ' + str(ratioNorm) +
                  ' is ' + str(arctanNorm) + ' degrees.')
        else:
            arctanNorm = math.degrees(math.atan(ratioNorm))
    elif (trigPrompt.lower()).strip() in acceptedArcTrigHyp:

        ratioHyp = float(input(
            "Enter the ratio (In decimal form) that you want to get the arcsinh, arccosh, or arctanh of: "))

        if ratioHyp >= 1:

            arccoshHyp = math.degrees(math.acosh(ratioHyp))

            arcsinhHyp = math.degrees(math.asinh(ratioHyp))

            arctanhHyp = math.degrees(math.at.anh(ratioHyp))

            print("The arcsine of " + str(ratioHyp) +
                  " in degrees is " + str(arcsinhHyp) + ".")

            print("The arccosh of " + str(ratioHyp) +
                  " in degrees is" + str(arccoshHyp) + ".")

            print("The arctan of " + str(ratioHyp) +
                  "in degrees is " + str(arctanhHyp) + ".")
elif (initial_input.lower()).strip() == 'log':

    logId = float(input("Enter the number you want to take the log of: "))

    baseCheck = input("Do you want your base to be e? (y or n) ")

    if (baseCheck.lower()).strip() == 'y':

        print("The answer is: " + str(math.log(logId)))

    elif (baseCheck.lower()).strip() == 'n':

        base = float(input("Enter the base of your logarithm: "))

        print("The answer is " + str(math.log(logId, base)))
elif (initial_input.lower()).strip() == 'complex':

    complexInput = 'placeholder'
    acceptedComplex = ['add', 'subtract',
                       'multiply', 'divide', 'exponent', 'trig', 'log']

    while not complexInput in acceptedComplex:
        complexInput = input(
            "COMPLEX NUMBERS: Enter which opeartion you want to do (add, subtract, multiply, divide, exponent, trig, log): ")

    if (complexInput.lower()).strip() == 'add':
        numsComplex_add = 1
        complexSum = 0

        while numsComplex_add < 2:
            numsComplex_add = int(
                input("Enter the number of complex numbers you want to add: "))

        for i in range(numsComplex_add):
            real_part = int(
                input("Enter the real part of complex number #" + str(i + 1) + ': '))
            imaginary_part = int(
                input("Enter the imaginary part of complex number #" + str(i + 1) + ': '))
            z = complex(real_part, imaginary_part)
            complexSum += z
        print("The sum of the complex number is (j = sqrt(-1)) " +
              str(complexSum) + '.')
    elif (complexInput.lower()).strip() == 'subtract':
        complexSub_nums = -1

        complexDif = 0
        compDifCalc = 0

        while complexSub_nums < 2:
            complexSub_nums = int(
                input("How many complex numbers would like to subtract? "))

        placeDifcomp_r = int(input("Enter the real part of the complex number you would like to subtract " +
                                   str(complexSub_nums) + " complex numbers from: "))
        placeDifcomp_i = int(input("Enter the imaginary part of the complex number you would like to subtrat" +
                                   str(complexSub_nums) + " complex numbers from: "))
        placeDifcomp = complex(placeDifcomp_r, placeDifcomp_i)
        for i in range(complexSub_nums):
            realPartSub = int(
                input("Enter the real part of complex number #" + str(i + 1) + ". "))
            imagPartSub = int(
                input("Enter the imaginary part of complex number #" + str(i + 1) + '. '))
            complexNumSub = complex(realPartSub, imagPartSub)
            complexDif = placeDifcomp - complexNumSub
        print("The final difference is " + str(complexDif) + ".")
    elif (complexInput.lower()).strip() == 'multiply':

        product = 1
        multComplexnums = -1

        while multComplexnums < 2:
            multComplexnums = int(
                input("How many complex numbers do you want to multiply? "))

        for i in range(multComplexnums):
            mult_real = int(
                input("Enter the real part of complex number #" + str(i + 1) + ": "))
            mult_imaginary = int(
                input("Enter the imaginary part of complex number #" + str(i + 1) + ": "))
            product *= complex(mult_real, mult_imaginary)

        print("Product: " + str(product) + ".")
    elif (complexInput.lower()).strip() == 'divide':

        divideCompnums = -1
        while divideCompnums < 2:
            divideCompnums = int(
                input("How many numbers would you like to divide? "))

        firstCompdivNum_real = int(input(
            "Enter the real part of the number you would like to divide  " + str(divideCompnums) + "complex numbers by: "))
        firstCompdivNum_imaginary = int(input(
            "Enter the imaginary part of the number you would like to divide " + str(divideCompnums) + " complex numbers by: "))
        firstCompdivNum = complex(
            firstCompdivNum_real, firstCompdivNum_imaginary)

        for i in range(divideCompnums):
            placeComp_real = int(
                input("Enter the real part of the divisor #" + str(i + 1) + ": "))
            placeComp_imaginary = int(
                input("Enter the imaginary part of the divisor #" + str(i + 1) + ": "))

            placeComp = complex(placeComp_real, placeComp_imaginary)

            firstCompdivNum /= placeComp

        print("Quotient: " + str(firstCompdivNum) + ".")

    elif (complexInput.lower()).strip() == 'exponent':
        complexExp_real = float(input("Enter the real part of the exponent: "))
        complexExp_imaginary = float(
            input("Enter the imaginary part of the exponenet: "))

        complexExp = complex(complexExp_real, complexExp_imaginary)
        complexBase_real = float(
            input("Enter the real part of the base of the exponent: "))
        complexBase_imaginary = float(
            input("Enter the imaginary of the base of the exponent: "))

        complexBase = complex(complexBase_real, complexBase_imaginary)

        finalExpoComplex = complexBase ** complexExp

        print("The answer is: " + str(finalExpoComplex) + ".")
    elif (complexInput.lower()).strip() == 'trig':
        # TODO Write Trig functions here.

        acceptedComplexTrig = ['sin', 'cos', 'tan']
        acceptedComplexArcTrig = ['asin', 'acos', 'atan']
        acceptedComplexHyp = ['sinh', 'cosh', 'tanh']
        acceptedComplexArcHyp = ['asinh', 'acosh', 'atanh']

        complexTriginput = input(
            'Enter the trig function that you want to do with complex numbers (sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, atanh, acosh): ')

        if complexTriginput in acceptedComplexTrig:
            complexTrig_real = int(input(
                "Enter the real part of the complex number you want to find the sine, cosine, or tangent of: "))
            complexTrig_imaginary = int(input(
                "Enter the imaginary part of the complex number you want to find the sine, cosine, or tangent of: "))
            complexTrig = complex(complexTrig_real, complexTrig_imaginary)

            print("The sine of " + str(complexTrig) +
                  " is " + str(cmath.sin(complexTrig)) + ".")
            print("The cosine of " + str(complexTrig) +
                  " is " + str(cmath.cos(complexTrig)) + ".")
            print("The tangent of " + str(complexTrig) +
                  " is " + str(cmath.tan(complexTrig)) + ".")
        elif (complexTriginput.lower()).strip() in acceptedComplexArcTrig:
            complexArcTrig_real = int(input(
                "Enter the real part of the complex number you want to find the arcsine, arccosine, or arctangent of: "))
            complexArcTrig_imaginary = int(input(
                "Enter the imaginary part of the complex number you want to find the arcsine, arccosine, or arctangent of: "))
            complexArcTrig = complex(
                complexArcTrig_real, complexArcTrig_imaginary)

            print("The arcsine of " + str(complexArcTrig) +
                  " is " + str(cmath.asin(complexArcTrig)) + ".")

            print("The arccosine of " + str(complexArcTrig) +
                  " is " + str(cmath.acos(complexArcTrig)) + ".")

            print("The arctangent of " + str(complexArcTrig) +
                  " is " + str(cmath.atan(complexArcTrig)) + ".")
        elif (complexTriginput.lower()).strip() in acceptedComplexHyp:
            complexHyp_real = int(input(
                'Enter the real part of the complex number that you want to find the sinh, cosh, or tanh of:'))
            complexHyp_imaginary = int(input(
                'Enter the imaginary part of the complex number that you want to find the sinh, cosh, or tanh of: '))

            complexHyp = complex(complexHyp_real, complexHyp_imaginary)

            print('The sinh of ' + str(complexHyp) +
                  ' is ' + str(cmath.sinh(complexHyp)) + ".")

            print("The cosh of " + str(complexHyp) +
                  " is " + str(cmath.cosh(complexHyp)) + ".")

            print("The tanh of " + str(complexHyp) +
                  " is " + str(cmath.tanh(complexHyp)) + ".")
        elif (complexTriginput.lower()).strip() in acceptedComplexArcHyp:
            complexArcHype_real = int(input(
                "Enter the real part of the complex number that you want to find the arcsinh, arccosh, or arctanh of: "))

            complexArcHype_imaginary = int(input(
                "Enter the imaginary part of the complex number that you want to find the arcsinh, arcosh, or arctanh of: "))

            complexArcHype = complex(
                complexArcHype_real, complexArcHype_imaginary)
    elif (complexInput.lower()).strip() == 'log':
        complexLog_real = int(input(
            "Enter the real part of the complex number that you want to take the logarithm of: "))
        complexLog_imaginary = int(input(
            "Enter the imaginary part of the complex number that you want to take the logarithm of: "))
        complexLog = complex(complexLog_real, complexLog_imaginary)

        complexBaseLog_real = int(
            input("Enter the real part of the base of your logarithm: "))
        complexBaseLog_imaginary = int(
            input("Enter the imgainary part of the base of your logarithm: "))
        complexBaseLog = complex(complexBaseLog_real, complexBaseLog_imaginary)

        print("Answer: " + str(cmath.log(complexLog, complexBaseLog)))
elif (initial_input.lower()).strip() == 'permutation':
    n = int(input("Enter the number of items you want to choose k items from with order and without reputation: "))
    k = int(input(
        "Enter the number of items you want to choose from " + str(n) + " items: "))
    print(f"Answer: {str(math.perm(n, k))}")
elif (initial_input.lower()).strip() == 'combination':
    nC = int(input("Format: nCk. Enter n: "))
    kC = int(input("Enter k: "))
    print(f"Answer: {str(math.comb(nC, kC))}")
elif (initial_input.lower()).strip() == 'factorial':
    fact = int(input('Enter the number that you want to take the factorial of: '))
    print(f"Answer: {str(math.factorial(fact))}")
