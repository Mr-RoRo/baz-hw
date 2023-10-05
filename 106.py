def even(ListofNum):
    sum = 0
    for i in ListofNum:
        if(i % 2 == 0):
            sum += 1
    return sum

# numbers = []

# for i in range(5):
#     numbers.append(int(input("Enter Number : ")))

# print(even(numbers))