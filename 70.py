
for num in range(56,1985):
    for maghsom in range(1,num):
        if(num % maghsom == 0):
            print(num," : ",maghsom)