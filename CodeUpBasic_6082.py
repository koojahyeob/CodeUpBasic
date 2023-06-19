n = int(input())

for i in range(1,n+1) :
    if i%10 == 3 or i%10 == 6 or i%10 == 9 :
        print("X" ,end=' ')
    else :
        print(i, end=' ')
        
# 차근차근 먼저 기본적인 123456789 먼저 출력 코드 입력해보고
# 추가로 어떤걸 해야 X를 넣을 수 있을지 순서대로 생각하기