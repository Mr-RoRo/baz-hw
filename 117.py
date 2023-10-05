string = input("Enter String : ").split(" ")


for i in string:
    print(i[0].upper()+i[1:])