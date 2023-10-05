numbers = []
fibonachi = [0]
f0 = 0
f1 = 1
sum = 0

for i in range(100):

    f1 = f0 + f1
    f0 += f1

    fibonachi.append(f1)
    fibonachi.append(f0)

    numbers.append(int(input("Enter Number : ")))
    
fibonachi.remove(1)

for num in numbers:
    for fibo in range(len(fibonachi)):
        if(num % 2 != 0 and num == fibonachi[fibo]):
            sum += 1

print(sum)
