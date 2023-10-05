fibonachi = [0]
f0 = 0
f1 = 1
sum = 0
num = int(input("Enter Number : "))
for i in range(12):

    f1 = f0 + f1
    f0 += f1

    fibonachi.append(f1)
    fibonachi.append(f0)
    
fibonachi.remove(1)

for fibo in fibonachi:
    if(fibo % num == 0):
        sum += 1

print(sum)