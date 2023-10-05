number1 = input("Enter Number 1 : ")
number2 = input("Enter Number 2 : ")

if(number1 == "111" and number2 == "111"):
    print("1110")
elif(number1 == "111" and number2 == "110" or number2 == "111" and number1 == "110"):
    print("1101")
elif(number1 == "111" and number2 == "100" or number2 == "111" and number1 == "100"):
    print("1011")
elif(number1 == "111" and number2 == "101" or number2 == "111" and number1 == "101"):
    print("1100")
elif(number1 == "111" and number2 == "101" or number2 == "111" and number1 == "101"):
    print("1100")

