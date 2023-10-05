tedad = int(input("Enter Tedad Numbers : "))

numbers = []
max = 0

for i in range(tedad):
    numbers.append(int(input("Enter Number "+str(i+1)+" : ")))
    if(numbers[i] > max):
        max = numbers[i]

print(max)