tedad = int(input("Enter Tedad Numbers : "))

numbers = []
SortNumber = []
isSort = False

for i in range(tedad):
    numbers.append(int(input("Enter Number "+str(i+1)+" : ")))
    SortNumber.append(numbers[i])

SortNumber.sort()

for num in range(len(numbers)):
    if(numbers[num] == SortNumber[num]):
        isSort = True
    else:
        isSort = False
        break
    
if(isSort):
    print("is sorted")
else:
    print("not sorted")
    
