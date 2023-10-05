tedad = int(input("Enter Tedad Numbers : "))

numbers = []

for i in range(tedad):
    numbers.append(int(input("Enter Number "+str(i+1)+" : ")))
        
numbers.sort(reverse=True)

print(numbers)
