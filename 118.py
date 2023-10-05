string = input("Enter String : ")

sum = ""

for i in string:
    if(i.isdigit()):
        sum += i

print(sum)