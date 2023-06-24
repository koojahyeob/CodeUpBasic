list = []
for i in range(20) :
    list.append([])
    for j in range(20) :
        list[i].append(0)

n = int(input())

for i in range(n) :
    x, y = map(int, input().split())
    list[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(list[i][j], end= " ")

    print()
    
