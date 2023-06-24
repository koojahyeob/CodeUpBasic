n = int(input())
k = input().split()

for i in range(n) :
    k = list(map(int, k))

min_num = min(k)

print(min_num)
    
