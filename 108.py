        
def adadAval(listOfNum):

    avalNumbers = []

    for i in listOfNum:
        
        if i == 1:
            continue 
    
        maghsom = 2
        isAval = True
        while maghsom*maghsom <= i:
            if(i % maghsom == 0):
                isAval = False
            maghsom +=1
        if(isAval):
            avalNumbers.append(i)

    print(avalNumbers)

# tedad = int(input("enter n : "))
# numbers = []

# for i in range(tedad):
#     numbers.append(int(input("Enter Number : ")))

# adadAval(numbers)