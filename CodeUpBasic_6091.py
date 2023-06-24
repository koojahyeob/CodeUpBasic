a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

day = 1

while day%a != 0 or day%b !=0 or day%c !=0 :
    day += 1
    
print(day)

# 최소공배수로만 생각을 할 수 있는데, 반대로 생각해보기
# a b c로 각각 나눴을 때 나머지가 없는, 나머지가 0인 제일 작은 값이 답
# 따라서 나머지가 하나라도 0이 아닐 경우에는 day 하루씩 늘리기
