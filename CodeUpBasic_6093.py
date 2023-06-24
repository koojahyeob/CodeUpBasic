n = int(input())
a = input().split()

for i in range(n) :
    a = list(map(int,a))

for i in reversed(range(n)) :
    print(a[i], end=" ")

# reversed 대신 range(n-1, -1, -1) 가능