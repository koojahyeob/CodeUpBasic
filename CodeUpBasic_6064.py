a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b :
    if c > b :
        print(b)
    elif c < b :
        print(c)

elif b > c :
    if a > c : 
        print(c)
    elif a < c :
        print(a)

elif c > a :
    if b > a : 
        print(a)
    elif b < a :
        print(b)

elif a == b == c :
    print(a)
