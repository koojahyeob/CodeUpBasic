a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

k = int()

for i in range(n) :
     a = a*m+d

# n= 1 = a
# n = 2 = a*m+d
# n = 3 = (a*m+d)*m+d
# n = 4 = ((a*m+d)*m+d)*m+d
