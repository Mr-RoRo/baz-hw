number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
number3 = int(input("Enter Number 3 : "))

if (number1 > number2 and number1 > number3):
    print(number1)
elif (number2 > number1 and number2 > number3):
    print(number2)
elif (number3 > number1 and number3 > number2):
    print(number3)
