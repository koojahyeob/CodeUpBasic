sum = int(input())

k = 0
for i in range(0,1001):
    k += i 
    if k >= sum :
        print(i)
        break
