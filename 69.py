number1 = input("Enter Number : ")

newNumber = ""

for i in range(len(number1)):

    if(number1[i] != "0"):
        newNumber += number1[i]

print(newNumber)
