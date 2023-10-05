number1 = input("Enter Number : ")

sum = 0

for i in range(len(number1)):

    if(number1[i] == "0"):
        sum += 1

print(sum)