x = input()
x= ord(x) #ord : 알바벳 문자 a의 정수값은 ord('a')로
a = ord('a')

while a <= x :
    print(chr(a), end=" ") #chr 값으로 유니코드 문자 출력
    a = a+1
