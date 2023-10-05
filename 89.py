numbers = []
avalNumbers = []

for i in range(10):
    
    numbers.append(int(input("Enter Number : ")))

    if numbers[i] == 1:
        continue 
 
    maghsom = 2
    isAval = True
    while maghsom*maghsom <= numbers[i]:
        if(numbers[i] % maghsom == 0):
            isAval = False
        maghsom +=1
    if(isAval):
        avalNumbers.append(numbers[i])
        
print(avalNumbers)