def facEL(listOfNum):

    for j in listOfNum:
        fac = 1
        for jj in range(1,j+1):
            fac *= jj
        print("fac "+str(j)+" : "+str(fac))

# tedad = int(input("Enter Tedad Numbers : "))
# numbers = []

# for i in range(tedad):
#     numbers.append(int(input("Enter Number "+str(i+1)+" : ")))

# facEL(numbers)