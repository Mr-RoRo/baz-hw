def ave(listOfNumbers):
    sum = 0
    for num in listOfNumbers:
        sum += num
    average = sum / 5
    for num in listOfNumbers:
        if(num + 3 == average or num - 3 == average):
            print(num)

# numbers = []

# for i in range(5):
#     numbers.append(int(input("Enter Number : ")))

# ave(numbers)