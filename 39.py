number1 = int(input("Enter Number : "))

numberBedonZero = 0
jaegha = 1

for i in range(4):
    ragham = number1 % 10
    number1 //= 10
    if(ragham != 0):
        ragham *= jaegha
        numberBedonZero += ragham
        jaegha *=10

print(numberBedonZero)