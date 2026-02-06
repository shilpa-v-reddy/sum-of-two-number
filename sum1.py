def getSum(number1, number2):
    return number1 + number2

def invoke_getSum():
    sum = getSum(5,5)
    print("sum of two numbers is", sum)

    sum1 = getSum(1.5, 1.5)
    print("sum of two numbers is", sum1)

    sum2= getSum("Hello", "World")
    print("sum of two numbers is", sum2)

invoke_getSum()

