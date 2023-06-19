n = int(input())
sum = 0

for i in range(0,10000000000) :
    sum += i
    if sum >= n :
        break

print(sum)